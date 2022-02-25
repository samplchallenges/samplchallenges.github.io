# generate_references.py

# pip install pyzotero
from pyzotero import zotero
import subprocess
import argparse
import os
import logging 
import shutil
import tempfile

LOG_LEVEL = logging.DEBUG
FORMAT = '[%(asctime)s-%(levelname)s] %(message)s'
logging.basicConfig(encoding='utf-8', level=LOG_LEVEL, format=FORMAT)

def create_markdown_file_from_headerfile(tempfile: str, outfile: str, headerfile: str):
    with open(outfile, 'w') as outf:
        with open(headerfile, 'r') as headerf:
            for line in headerf:
                if line.startswith("[//]: #"):
                    outf.write(line[7:])
                else:
                    outf.write(line)
            outf.write("\n\n")
        with open(tempfile, 'r') as tempf:
            for line in tempf:
                outf.write(line)

def create_markdown_file_with_header(tempfile: str, outfile: str, header: str):
    with open(outfile, 'w') as outf:
        outf.write(header)
        outf.write("\n")
        with open(tempfile, 'r') as tempf:
            for line in tempf:
                outf.write(line)

def get_manubot_command(outfile: str, string_of_idenfiers: str):
    command = "manubot cite --format=markdown "
    if outfile:
        command += f"--output={outfile} "
    return command + string_of_identifiers

def get_doi(item):
    if "DOI" not in item["data"].keys():
        return None
    if item["data"]["DOI"].strip() == "":
        return None
    if "," in item["data"]["DOI"]:
        return "doi:" + item["data"]["DOI"].split(",")[0]
    else:
        return "doi:" + item["data"]["DOI"]

def get_isbn(item):
    if "ISBN" not in item["data"].keys():
        return None
    elif item["data"]["ISBN"].strip() == "":
        return None
    else:
        return "isbn:" + item["data"]["ISBN"]


def get_url(item):
    if "url" not in item["data"].keys():
        return None
    elif item["data"]["url"].strip() == "":
        return None
    else:
        return "url:" + item["data"]["url"]

if __name__ == "__main__":
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--tag", help="Zotero library tag", required=False)
    ap.add_argument("--lib-id", help="Zotero ID (user or group) from https://www.zotero.org/settings/keys", required=True)
    ap.add_argument("--api-key", help="Zotero API key from https://www.zotero.org/settings/keys/new", required=True)
    ap.add_argument("--lib-type", help="Library type associated with the Zotero ID ('user' or 'group')", required=True)
    ap.add_argument("--outfile", help="Filename for Markdown output", required=False)
    ap.add_argument("--headerfile", help="Header file for Markdown output", required=False)
    ap.add_argument("--header", help="Header text for Markdown output", required=False)

    args = vars(ap.parse_args())
    
    # Connect to Zotero library and filter by tag
    zot = zotero.Zotero(args["lib_id"], args["lib_type"], args["api_key"])
    if args["tag"]:
        zot.add_parameters(tag=args["tag"], sort="date")
    else:
        raise NotImplementedError
    # must use zot.everything() to gather references otherwise results are
    # capped at 100 items
    items = zot.everything(zot.top())

    # Gather Reference Identifiers
    string_of_identifiers = ""
    identifier_ct = 0
    err_items = []
    for item in items:
        title = item["data"]["title"]

        identifer = get_doi(item)
        if not identifer:
            identifer = get_isbn(item)
        if not identifer:
            identifer = get_url(item)
        if not identifer:
            err_items.append(item)
            continue
        string_of_identifiers += identifer
        string_of_identifiers += " "
        identifier_ct += 1


    # Zotero Library Statistics Logging 
    unique_identifier_ct = len(set(string_of_identifiers.split()))
    logging.info("Total refs with tag \"%s\" = %d", args["tag"], len(items))
    logging.info("  Error refs count = %d", len(err_items))
    logging.info("  Total refs minus errors count = %d", identifier_ct)
    logging.info("    Included refs count = %d", unique_identifier_ct)
    logging.info("    Duplicate count = %d", identifier_ct - unique_identifier_ct)
    for item in err_items:
        logging.info("Error Ref (no DOI, ISBN, or URL): %s", item["data"]["title"])
    if identifier_ct == 0:
        logging.error("No references collected, exiting now")
        exit()


    # Set the Output file if applicable
    tempdir = None
    manubot_ofile = None
    if args["outfile"] and (args["headerfile"] or args['header']):
        tempdir = tempfile.mkdtemp()
        manubot_ofile = os.path.join(tempdir, "temp_02_allreferences.md")
    if args["outfile"] and not (args["headerfile"] or args['header']):
        manubot_ofile = args["outfile"]


    # Run Manubot on the Reference Identifiers 
    command = get_manubot_command(manubot_ofile, string_of_identifiers)
    subprocess.call(command, shell=True)

    
    # if a headerfile is specified, create a markdown file of references beginnning 
    # with the text from the header file
    if args["outfile"] and args["headerfile"]:
        create_markdown_file_from_headerfile(manubot_ofile, args["outfile"], args["headerfile"])


    # if a header string is specified, create a markdown file of references beginning
    # with the text from the header string
    elif args["outfile"] and args["header"]:
        create_markdown_file_with_header(manubot_ofile, args["outfile"], args["header"])


    # Clean up temporary directory
    if tempdir and os.path.isdir(tempdir):
        shutil.rmtree(tempdir)
