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

**SAMPL history**: (Under construction)

{% for collection in site.collections %}
  {% if collection.label == "history" %}
    {% for post in collection.docs %}
	  {% if post.layout != "archive" %}
        {% include archive-single.html %}
	  {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
