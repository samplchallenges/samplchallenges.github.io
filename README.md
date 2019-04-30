# SAMPL: Crowdsourcing challenges to improve prediction of protein-ligand interactions

This site, and repository, contains information, plans, and announcements relating to the Statistical Assessment of Modeling of Proteins and Ligands (SAMPL) series of blind predictive challenges.
This NIH-funded series of challenges tests computational models on predictions of properties related to challenges faced in a drug discovery setting.

If you are reading this file, it means you are visiting our GitHub repository. The contents of this repository are meant to be served instead via our [SAMPL website](samplchallenges.github.io), so please visit there instead.

## Site status

These pages are currently under construction and will be updated further in the immediate future with the latest SAMPL news and announcements. (Status date April 30, 2019).

## Contacts

If you have questions or concerns, please use our issue tracker here, or contact David L. Mobley

## Site administration

### Generate navigation
The subpages of [livecomsjournal.github.io](https://livecomsjournal.github.io) have a navigation column on the left (see [livecomsjournal.github.io/authors/policies/](https://livecomsjournal.github.io/authors/policies/) for an example). This navigation is read from `_data/navigation.yml` and is static, meaning that it needs to be re-generated whenever changes to the structure of a document are done. Specifically, the navigation consists of links to all first and second title levels (`# Title` and `## Title` in Markdown), and if any of those are changed, the navigation needs to be updated.

There is a script named `generate_navigation.py` which generates the content of the navigation file. Calling
```
python3 generate_navigation.py > _data/navigation.yml
```
regenerates the navigation file with the current state of the Markdown-files. It does so by reading through all `.md` files (except `index.md`) in the `_about_livecoms`, `_author_instructions` and `_editorial_policies` and generating a menu item for every first-level or second-level title. It also read the frontmatter of each file and rewrites it in case no `permalink` or no `sidebar` tag is found.

The script is helpful, but probably not fool-proof - a visual inspection of the result via `git diff`, or even better a check of the result in a local jekyll installation is highly recommended before pushing the new navigation file to the `master` branch.

### Testing Locally

First you will need to install the gem for `github-pages`. Run the following command:

```
gem install github-pages
```

This will install the github-pages gem and all dependencies (including jekyll).

Later, to update the gem, type:

```
gem update github-pages
```

To build a local copy, go into the directory and type:

```
jekyll build
```

This will create (or modify) a `_site/` directory, containing everything from `assets/`, and then the `index.md` and all `pages/*.md` files, converted to html. (So there’ll be `_site/index.html` and the various `_site/pages/*.html`.)

**Do not commit this directory in a Pull Request!! Github will compile this directory on its own.**

Type the following in order to “serve” the site. This will first run build, and so it does not need to be preceded by `jekyll build`.

```
jekyll serve
```

Now open your browser and go to http://localhost:4000

### Credits

This adapted from/based on the construction of the LiveCoMS Journal GitHub pages site based on the Jekyll Mininimal Mistakes theme.
