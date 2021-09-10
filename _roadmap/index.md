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
## The SAMPL Roadmap

In general, the SAMPL roadmap is in flux depending on whether there are snags in data collection or new and exciting opportunities, but we try to keep the links below updated with the latest on our expectations for the future.

**Data donation**: In general we seek assistance in obtaining high quality data along the lines described in the roadmap above. Some of the measurements will be conducted in our own laboratories, but for others, we rely on donations of data, internships with industry partners, etc., and we are delighted to have help in this regard. Please contact [David L. Mobley](https://mobleylab.org/people/david-mobley/) at dmobley (you know what symbol) mobleylab.org if you have ideas or can help. Properties of particular interest include log P and log D values (between water and alternate solvents, or between diverse solvents), pKa, solubility, binding to well-understood or simple model systems, and selected protein-ligand binding data.

**Containerization**: We are pushing in the direction of containerization of submissions, introducing a new category of challenge where participants submit *methods* rather than *predictions*. This will allow fully automated methods to be tested on completely equal footing, head-to-head, and also potentially allow methods to be tested on proprietary datasets. Containerized methods will also be fully reproducible, allowing any other researcher to easily utilize the exact method employed with no limitations from operating system compatibility issues. Currently, we plan on using [Docker containers](https://www.docker.com/resources/what-container) for our first challenges (protein-ligand docking challenge and a LogD challenge) to test this submission method. For more information on how we will use containerization, please see our [github](https://github.com/samplchallenges/SAMPL-containers/tree/main/tutorials).


{% for collection in site.collections %}
  {% if collection.label == "roadmap" %}
    {% for post in collection.docs %}
	  {% if post.layout != "archive" %}
        {% include archive-single.html %}
	  {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
