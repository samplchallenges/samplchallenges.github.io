---
title: "The SAMPL challenges"
layout: archive
permalink: /current/
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/hosts.jpg
excerpt: "Current and upcoming SAMPL challenges and meetings"
---

## Current challenges
We recently launched some of the [SAMPL8 challenges on host-guest binding](https://github.com/samplchallenges/SAMPL8), with our current challenge focusing on several guests binding to Gibb deep-cavity cavitands (GDCCs) (predictions due Feb. 4); a CB8 challenge has already concluded. As a part of SAMPL8, we are also planning test run of a containerized docking method challenge using [Docker containers](https://www.docker.com/resources/what-container); for more information, please see our [containerized docking tutorial](https://github.com/samplchallenges/SAMPL-containers/tree/main/tutorials). 


The SAMPL8 Physical Properties special issue still open for submission.

## Challenges recently closed:

### SAMPL8 challenges

#### Host-guest challenges:
- Host-guest binding for drugs of abuse binding to CB8; deadline was Sept., 2020.
- Host-guest binding for a series of compounds binding to Gibb deep cavity cavitand (GDCC) hosts; deadline Feb. 4, 2021.
- A GSK pKa/logD challenge (below)

Details of these are available on the [SAMPL8 GitHub repository](https://github.com/samplchallenges/SAMPL8).

#### The SAMPL8 physical properties challenge:
We recently finalized work with GSK on data collection for a physical properties challenge. The data recently cleared legal review at GSK and the challenge is live. We have collected:
- pKa data for 24 compounds
- pH-dependent solubility for these compounds
- logD for 11 of these compounds for distribution between different phases: water-octanol, water-cyclohexane, water-ethyl acetate, water-heptane, water-MEK, water-TBME, and cyclohexane-DMF. Not all combinations of distribution coefficient are available because of compound solubility in the different phases. The total number of data points/combinations of (compound)x(phase identities) is between 40 and 50. [Details on dataset collection are available in this talk from the GCC/EuroSAMPL workshop](https://dx.doi.org/10.5281/zenodo.4245127])

We will first run a pKa prediction challenge on the 24 compounds, and then a logD challenge. Deadlines are in summer 2021; refer to the SAMPL8 GitHub repository for details.

### SAMPL7 challenges
SAMPL7 has now concluded, and the physical properties special issue is closed for submission. 
- Protein-ligand binding to the Pleckstrin homology domain interacting protein (PHIP) second bromodomain (PHIP2), in three phases.
- Host-guest binding on octa acid derivatives (Gibb lab); deadline was Nov. 1, 2019.
- Host-guest binding on modified cyclodextrin derivatives (Gilson lab); deadline was Nov. 1, 2019
- Host-guest binding on a glycouril clip-like host (Isaacs lab); deadline was Oct. 1, 2019
- Physical property prediction (logP, pKa, permeability) for a congeneric series; deadline Sept. 15, 2020. **Analysis results are now available.**

Our [SAMPL7 host-guest virtual workshop](http://dx.doi.org/10.5281/zenodo.3674155) is available at this DOI: [10.5281/zenodo.3674155](http://dx.doi.org/10.5281/zenodo.3674155)

Details of these are available on the [SAMPL7 GitHub repository](https://github.com/samplchallenges/SAMPL7).


## Upcoming challenges

Details of the NanoLuc challenge are still being worked out with NCATS.
See our [roadmap](https://samplchallenges.github.io/roadmap/) pages for more details.


Note that, in contrast to SAMPL0-5, the SAMPL numbering system now corresponds to *phases* rather than individual challenges. So, rather than corresponding to a single challenge with a single deadline, SAMPL7 and onward involve multiple component challenges with multiple deadlines.


{% for collection in site.collections %}
  {% if collection.label == "current_challenges" %}
    {% for post in collection.docs %}
	  {% if post.layout != "archive" %}
        {% include archive-single.html %}
	  {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
