# generate_references.py

# pip install pyzotero
from pyzotero import zotero
import subprocess
import argparse
import os

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
    if item["data"]["DOI"] == "":
        return None
    if "," in item["data"]["DOI"]:
        return "doi:" + item["data"]["DOI"].split(",")[0]
    else:
        return "doi:" + item["data"]["DOI"]

def get_isbn(item):
    if "ISBN" not in item["data"].keys():
        return None
    else:
        return "isbn:" + item["data"]["ISBN"]


def get_url(item):
    if "url" not in item["data"].keys():
        return None
    else:
        return "url:" + item["data"]["url"]

if __name__ == "__main__":
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--tag", help="Zotero library tag", required=False)
    ap.add_argument("--lib-id", help="Zotero user ID from https://www.zotero.org/settings/keys", required=True)
    ap.add_argument("--api-key", help="Zotero API key from https://www.zotero.org/settings/keys/new", required=True)
    ap.add_argument("--outfile", help="Filename for Markdown output", required=False)
    ap.add_argument("--headerfile", help="Header file for Markdown output", required=False)
    ap.add_argument("--header", help="Header text for Markdown output", required=False)

    args = vars(ap.parse_args())
    

    library_type = "user"
    zot = zotero.Zotero(args["lib_id"], library_type, args["api_key"])

    if args["tag"]:
        zot.add_parameters(tag=args["tag"], sort="date")
    else:
        raise NotImplementedError

    items = zot.items()
    string_of_identifiers = ""

    for item in items:
    	title = item["data"]["title"]

    	identifer = get_doi(item)
    	if not identifer:
    		identifer = get_isbn(item)
    	if not identifer:
    		identifer = get_url(item)
    	if not identifer:
        	print(f"{title[0:30]:<40}... Error finding DOI, ISBN, or URL for item.")
        	continue
    	string_of_identifiers += identifer
    	string_of_identifiers += " "

    ofile = None
    tempfile = "temp.md"
    if args["outfile"] and (args["headerfile"] or args['header']):
        ofile = tempfile
    if args["outfile"] and not args["headerfile"]:
        ofile = args["outfile"]

    command = get_manubot_command(ofile, string_of_identifiers)
    print(command)

    subprocess.call(command, shell=True)

    # if a header is specified, create a markdown file with header
    if args["outfile"] and args["headerfile"]:
        create_markdown_file_from_headerfile(ofile, args["outfile"], args["headerfile"])

    elif args["outfile"] and args["header"]:
        create_markdown_file_with_header(ofile, args["outfile"], args["header"])

    if ofile and os.path.isfile(ofile):
        os.remove(ofile)
