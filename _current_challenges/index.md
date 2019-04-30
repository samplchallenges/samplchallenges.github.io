---
title: "The SAMPL challenges"
layout: archive
permalink: /current/
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/hosts.jpg
excerpt: "Current and upcoming SAMPL challenges"
---

Several SAMPL7 challenges will launch in the immediate future, including:
- Host-guest binding on octa acid derivatives (Gibb lab)
- Host-guest binding on modified cyclodextrin derivatives (Isaacs lab)
- Host-guest binding on a glycouril clip-like host (Gilson lab)

We are also working with GSK on data collection for a partitioning challenge, and with NCATS on data collection for two potential protein-ligand binding challenges (on HSA and NanoLuc binding). Depending on data collection timescales these may comprise part of the SAMPL7 series, or may become part of SAMPL8. 

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
