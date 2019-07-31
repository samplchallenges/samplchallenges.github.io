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
Currently we are running three host-guest binding challenges, with tentative submission deadlines of Oct. 1, 2019, including:
- Host-guest binding on octa acid derivatives (Gibb lab)
- Host-guest binding on modified cyclodextrin derivatives (Gilson lab)
- Host-guest binding on a glycouril clip-like host (Isaacs lab)
Details of these are available on the [SAMPL7 GitHub repository](https://github.com/mobleylab/SAMPL7).

## Upcoming challenges

Several additional challenges are planned as part of the SAMPL7 series. 
Most immediately, we working with GSK on data collection for a partitioning challenge, and with NCATS on data collection for two potential protein-ligand binding challenges (on HSA and NanoLuc binding). Depending on data collection timescales these may comprise part of the SAMPL7 series, or may become part of SAMPL8.
As the GSK logD dataset is currently in the data collection phase, we tentatively expect it will be part of SAMPL7, likely in late 2019 or early 2020.
See our [roadmap](https://samplchallenges.github.io/roadmap/) pages for more details.

Please sign up for our [SAMPL7 e-mail list](http://eepurl.com/gpBBun) for e-mail announcements, and bookmark (and watch) our [SAMPL7 GitHub repository](https://github.com/MobleyLab/SAMPL7).

Note that, in contrast to SAMPL0-5, the SAMPL numbering system now corresponds to *phases* rather than individual challenges. So, rather than corresponding to a single challenge with a single deadline, SAMPL7 will involve multiple component challenges with multiple deadlines.

## Wrapping up SAMPL6

SAMPL6 Part II, which is currently in the analysis phase, focused on an octanol-water log P prediction challenge. The Log P prediction challenge will be followed by a joint D3R/SAMPL workshop in San Diego, Aug 22-23, 2019, immediately before the San Diego ACS National Meeting; a virtual workshop is planned for May 16, 2019 (contact David Mobley if you are interested in attending). [A special issue of JCAMD is planned](https://samplchallenges.github.io/roadmap/specialissues/) with a submission deadline of Sept. 15. Join our [SAMPL6 e-mail list](http://eepurl.com/gaAA0H) if you would like announcements pertaining to these events.


{% for collection in site.collections %}
  {% if collection.label == "current_challenges" %}
    {% for post in collection.docs %}
	  {% if post.layout != "archive" %}
        {% include archive-single.html %}
	  {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
