---
title: "The SAMPL challenges"
layout: archive
permalink: /roadmap/
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/hosts.jpg
excerpt: "The long-term roadmap"
---

{% for collection in site.collections %}
  {% if collection.label == "roadmap" %}
    {% for post in collection.docs %}
	  {% if post.layout != "archive" %}
        {% include archive-single.html %}
	  {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
