---
title: "The SAMPL challenges"
layout: archive
permalink: /history/
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/hosts.jpg
excerpt: "History and links to SAMPL datasets"
---

The SAMPL challenges provide data and test sets which prove valuable to the community long after the completion of any specific challenge. Data sets typically become standard test sets and are reutilized in a wide variety of downstream studies. Here, find links to data sets from previous SAMPL challenges as well as insights into key lessons learned.

## History

The SAMPL project, initiated in 2008, has traditionally included not only protein-ligand modeling, but also challenges based on smaller molecular systems, such as the hydration free energies of small molecules and the binding thermodynamics of host-guest systems. Compact model systems like these embody critical elements of the physical chemistry of protein-ligand binding, while making it far easier to probe the accuracy of computational tools used to model protein-ligand interactions, and to identify and correct sources of error. See the [SAMPL Wikipedia page](https://en.wikipedia.org/wiki/SAMPL_Challenge) for additional background information as well.

As of 2018, the NIH has funded the SAMPL project for four years and so challenges are expected to be more regular at least for that timeframe.

{% for collection in site.collections %}
  {% if collection.label == "history" %}
    {% for post in collection.docs %}
	  {% if post.layout != "archive" %}
        {% include archive-single.html %}
	  {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
