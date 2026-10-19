---
lang: en
translation_key: gcp
title: Clinical Trials / GCP
nav:
  order: 5
  tooltip: Clinical Trials and GCP
---

# {% include icon.html icon="fa-solid fa-notes-medical" %}Clinical Trials / GCP

Clinical studies conducted or supported by our group in rheumatology and immunology, including innovative approaches such as cell therapies and T-cell engagers.

{% include section.html %}

{% include i18n.html %}

{% assign trials = site.data.trials | sort: "sequence" %}
{% assign product_types = trials | map: "product_type" | uniq %}

<div class="trial-list" data-trial-list lang="{{ site_lang }}">
  <div class="trial-filters" role="group" aria-label="{{ ui.filter_trials }}" hidden>
    <button type="button" class="button trial-filter" data-filter-all aria-pressed="true" aria-controls="trial-grid">{{ ui.all }}</button>
    {% for product_type in product_types %}
    <button type="button" class="button trial-filter" data-product-type="{{ product_type | escape }}" aria-pressed="false" aria-controls="trial-grid">{{ product_type | escape }}</button>
    {% endfor %}
  </div>
  <div class="trial-grid" id="trial-grid">
    {% for trial in trials %}
    {% include trial-card.html trial=trial %}
    {% endfor %}
  </div>
</div>
