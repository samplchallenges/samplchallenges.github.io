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

Several challenges will launch in the immediate future, including:
- Host-guest binding on octa acid derivatives (Gibb lab)
- Host-guest binding on modified cyclodextrin derivatives (Gilson lab)
- Host-guest binding on a glycouril clip-like host (Isaacs lab)


{% for collection in site.collections %}
  {% if collection.label == "current_challenges" %}
    {% for post in collection.docs %}
	  {% if post.layout != "archive" %}
        {% include archive-single.html %}
	  {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
