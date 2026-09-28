---
title: GCP
nav:
  order: 5
  tooltip: Clinical Trials and GCP
---

# {% include icon.html icon="fa-solid fa-notes-medical" %}GCP

## Clinical Trials & Good Clinical Practice

Our laboratory conducts and participates in investigator-initiated and multicenter clinical studies, with a focus on innovative cellular and immune therapies for rheumatic and autoimmune diseases.

This section presents clinical research on CAR-T cell therapy and T-cell engager (TCE) therapy. Study details and recruitment information will be added as they become available.

{% include section.html %}

## Ongoing Trials

{% assign ongoing_trials = site.trials | where_exp: "trial", "trial.status == 'Recruiting' or trial.status == 'Active, not recruiting' or trial.status == 'Not yet recruiting'" | sort: "title" %}
{% if ongoing_trials.size > 0 %}
<div class="trial-grid">
{% for trial in ongoing_trials %}
{% include trial-card.html trial=trial %}
{% endfor %}
</div>
{% else %}
Details of ongoing studies will be published here when available.
{% endif %}

## Completed Trials

{% assign completed_trials = site.trials | where: "status", "Completed" | sort: "title" %}
{% if completed_trials.size > 0 %}
<div class="trial-grid">
{% for trial in completed_trials %}
{% include trial-card.html trial=trial %}
{% endfor %}
</div>
{% else %}
Completed study information will be added when available.
{% endif %}

{% assign other_trials = site.trials | where_exp: "trial", "trial.status != 'Recruiting' and trial.status != 'Active, not recruiting' and trial.status != 'Not yet recruiting' and trial.status != 'Completed'" | sort: "title" %}
{% if other_trials.size > 0 %}
## Other Studies

<div class="trial-grid">
{% for trial in other_trials %}
{% include trial-card.html trial=trial %}
{% endfor %}
</div>
{% endif %}

{% include section.html %}

## Trial Information

Each study page provides the available disease focus, therapy, study status, study type, study site, and registration information. Eligibility criteria and study contacts are listed when confirmed. Please refer to the individual study page for recruitment details.
