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

Challenges are currently closed; however, we are likely to soon frame a PHIP2 Stage 4 challenge involving affinity prediction. Additionally, data finalizatino for our next partitioning challenge is nearly complete.

## Challenges recently closed:

### SAMPL7 challenges
- Protein-ligand binding to the Pleckstrin homology domain interacting protein (PHIP) second bromodomain (PHIP2), in at least three phases.
- Host-guest binding on octa acid derivatives (Gibb lab); deadline was Nov. 1, 2019.
- Host-guest binding on modified cyclodextrin derivatives (Gilson lab); deadline was Nov. 1, 2019
- Host-guest binding on a glycouril clip-like host (Isaacs lab); deadline was Oct. 1, 2019

Details of these, along with submission formats, are available on the [SAMPL7 GitHub repository](https://github.com/mobleylab/SAMPL7). Submissions are accepted via our [AWS submission page](http://sampl-submission.us-west-1.elasticbeanstalk.com/submit/).

### More on the PHIP2 binding challenge

We are excited to announce a new set of SAMPL7 challenges focusing on protein-ligand binding, in partnership with the XChem facility for fragment screening at Diamond Light Source. The second bromodomain of PHIP (PHIP2) was targeted in an extensive X-ray crystallographic fragment screening experiment, leading to the 3D structures of multiple hits. This SAMPL7 challenge will take advantage of this dataset, addressing computational methods for the discrimination of binders from non-binders, binding pose predictions, and the unique opportunity to select new candidate ligands from a database, to be validated experimentally by X-ray crystallography at the Diamond Light Source (Harwell, UK).   

Details are on our SAMPL7 GitHub repository (github.com/samplchallenges/sampl7) and the SAMPL website (https://samplchallenges.github.io).

This challenge broke out into at least three phases on a tight timeline:
1) Identification of binders from fragment screening
2) Prediction of fragment binding modes
3) Selection of new compounds for screening from an experimental database


## Upcoming challenges

Several additional challenges are planned as part of the SAMPL7 series.
Most immediately, we are working with GSK on data collection for a partitioning challenge, and with NCATS on data collection for two potential protein-ligand binding challenges (on HSA and NanoLuc binding). Depending on data collection timescales these may comprise part of the SAMPL7 series, or may become part of SAMPL8.
As the GSK logD dataset is currently in the data collection phase, we tentatively expect it will be part of SAMPL7, likely in late 2019 or early 2020.
See our [roadmap](https://samplchallenges.github.io/roadmap/) pages for more details.

Please sign up for our [SAMPL7 e-mail list](http://eepurl.com/gpBBun) for e-mail announcements, and bookmark (and watch) our [SAMPL7 GitHub repository](https://github.com/MobleyLab/SAMPL7).

Note that, in contrast to SAMPL0-5, the SAMPL numbering system now corresponds to *phases* rather than individual challenges. So, rather than corresponding to a single challenge with a single deadline, SAMPL7 will involve multiple component challenges with multiple deadlines.


{% for collection in site.collections %}
  {% if collection.label == "current_challenges" %}
    {% for post in collection.docs %}
	  {% if post.layout != "archive" %}
        {% include archive-single.html %}
	  {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
