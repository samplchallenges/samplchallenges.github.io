---
layout: single
sidebar:
  nav: plans.md
title: Plans for upcoming challenges
excerpt: Plans for upcoming SAMPL challenges and phases
permalink: /roadmap/plans/
---

## SAMPL overview, SAMPL7-10

As of SAMPL7-10, our NIH funding allows us to be somewhat more strategic in planning challenges, so we plan a series of challenges encompassing:
- Physical property prediction (e.g. pKa, logP, logD, etc.)
- Host-guest binding
- Protein-ligand binding

SAMPL is now broken into phases, each running roughly a year, with each phase encompassing several component challenges. [Workshop plans](https://samplchallenges.github.io/current/workshops/) are detailed separately. In some cases SAMPL phases may overlap slightly; e.g. we're wrapping up SAMPL7 with a physical property challenge while launching the first SAMPL8 host-guest challenge as of July 2020.

The Gibb and Isaacs groups, focusing on host-guest binding, plan to collect regular data on host-guest binding, and protein-ligand binding assays are coming online in the Chodera lab. Physical property data, however, relies on planned industry internships and other partnerships.

For physical property prediction, we will likely revisit partitioning and distribution prediction at least two more times. As discussed in the recent [SAMPL6 logP virtual workshop](https://www.youtube.com/watch?v=FWUPXG8U3UE), predicting distribution between a polar phase (like octanol) and water involves at least three problems:

- pKa prediction
- neutral species partitioning
- charged species partitioning, as it is known that significant ratios of ions can partition into the octanol phase.

For nonpolar solvents (e.g. dodecane, heptane, cyclohexane) the third problem is minimal. Thus it is likely we will revisit nonpolar to water distribution in SAMPL7, and polar-to-water distribution in subsequent challenges. We also plan to progress in terms of pKa, initially providing pKa values (if we can get these measured) and later transitioning to requiring participants to predict pKa values.

Moving forward, we will also work on running an automated arm of SAMPL challenges to run methods head-to-head without human intervention. To accomplish this, we will use containerized [Docker](https://www.docker.com/resources/what-container) methods.

## SAMPL7 plans (concluded in 2020)

[SAMPL7](https://github.com/samplchallenges/sampl7) is complete, having included:
- Host-guest binding challenges on Isaacs' TrimerTrip, Gibb's GDCC's, and cyclodextrin derivatives from the Gilson lab
- PHIPA fragment binding prediction, though analysis is still wrapping up.
- Physical property prediction for a congeneric series; participants may predict (octanol-water) logP, pKa, or both. PAMPA permeability values are also optional. This is a partnership with the Ballatore lab at UCSD.


## SAMPL8 plans (beginning 2021)

- NanoLuc binding challenge (date TBD pending delays at NCATS)
- ~~HSA binding challenge, Winter 2020~~ (scrapped due to experimental limitations)
- Physical properties challenge, described below, beginning shortly early 2021
- Host-guest challenges, Summer 2020 onwards:
    - We concluded a SAMPL8 host-guest challenge on CB8
    - A GDCC challenge is currently ongoing, ending February, 2021
    - Data collection on modified cyclodextrins is ongoing and will hopefully lead to a challenge in 2021.
- Containerized challenges

### The NanoLuc challenges

We are collaborating with the National Center for Advancing Translational Sciences (NCATS), to use standard assays to measure binding affinities of large compound libraries to an engineered form of luciferase known as NanoLuc.
This data will be divided into sets of similar ligand complexities for sequential blind challenges. NanoLuc can also be expressed in E. coli, so future challenges will potentially involve mutated forms.

The NanoLuc challenge will likely involve prediction of affinities of drug-like molecules to a single binding site.
However, since NCATS has screened hundreds of thousands of compounds for binding to NanoLuc, the binding affinity prediction component may be preceded by a virtual screening challenge that involves attempting to pick active compounds out of a library of verified nonbinders.


### The SAMPL8 physical property challenge

The SAMPL8 physical property challenge focuses on pKa and logD. Data just cleared legal review at GSK and the challenge is now live; see our [current challenges page for more details](https://samplchallenges.github.io/current/).


## SAMPL9 plans (2022?)

- Physical property challenge (likely on pKa with Paul Czodrowski; late 2020); whether we revisit logD again will depend on the outcomes of SAMPL7 and 8.
- Host-guest binding challenges, summer 2021
- Protein-ligand binding challenge TBD

## SAMPL10 plans (2023-2024?)

- Physical property challenge
- Host-guest binding challenge
- Protein-ligand binding challenge

## Other datasets possibly en route
- With Scott Lokey (UCSC) we are exploring a potential challenge on cyclic peptide logP between water and hydrocarbons. Some of the Lokey lab's data is particularly interesting as conformational effects play a major role in partitioning.

# Properties of interest

Properties of particular interest for future SAMPL challenges include:

- Solubility (absolute thermodynamic solubility, but also relative solubilities for the same solute in different solvents)
- LogP and logD data
- pKa
- Passive membrane permeability
- Tautomer ratio prediction (estimated 2021)


We are exploring internships to generate such data, but if you have suitable resources and would like to contribute we would potentially love your help.
