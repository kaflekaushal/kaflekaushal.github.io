---
layout: page
permalink: /publications
title: Publications
---

<div class="publication-list container">
<div class="journal-papers">
  <h2>Journal</h2>
  <ul class="conference-paper-list">
    {% for entry in site.data.bibentries %}
    {% assign authors= entry.author | split: " and "%}
    {% if entry.type=='journal' %}
    <div class="paper-entry">
      <li class="paper-title"> {{ entry.title }} </li>
      <ul class="paper-metadata">
        <li class="paper-authors">
          {% for author in authors %}
          {% if author=="Kaushal Kafle" %}
          <strong> {{ author }}, </strong>
          {% elsif author== authors.last %}
          {{ author }}
          {% else %}
          {{ author }},
          {% endif %}
          {% endfor %}
        </li>
        <li class="paper-venue">{{ entry.venue }}</li>
        <li class="paper-publish-date">{{ entry.date }}</li>
        {% if entry.note %}
        <li class="paper-special-note">{{ entry.note }} </li>
        {% endif %}
        {% if entry.link or entry.press or entry.website %}
        <li class="paper-links">
          {% if entry.link %}
          <a href="{{entry.link | append: '.pdf' | relative_url }}">[PDF]</a>
          {% endif %}
          {% if entry.website%}
          <a href="{{entry.website}}" target="_blank">[Website]</a>
          {% endif %}
          {% if entry.press %}
          <a href="{{entry.press}}">[Press Coverage]</a>
          {% endif %}
        </li>
        {% endif %}
        <li class="bibtex">
          <button type="button" class="bib-collapsible btn btn-info btn-sm rounded-pill">Bibtex</button>
          <div class="bib-button-content">
            <figure class="full-bib highlight">
              <pre>{{ entry.bib | rstrip }} </pre>
            </figure>
          </div>
        </li>
      </ul>
    </div>
    {% endif %}
    {% endfor %}
  </ul>
</div>
  <div class="conference-papers">
    <h2>Conference Papers</h2>
    <ul class="conference-paper-list">
      {% for entry in site.data.bibentries %}
      {% assign authors= entry.author | split: " and "%}
      {% if entry.type=='conference' %}
      <div class="paper-entry">
        <li class="paper-title"> {{ entry.title }} </li>
        <ul class="paper-metadata">
          <li class="paper-authors">
            {% for author in authors %}
            {% if author=="Kaushal Kafle" %}
            <strong> {{ author }}, </strong>
            {% elsif author== authors.last %}
            {{ author }}
            {% else %}
            {{ author }},
            {% endif %}
            {% endfor %}
          </li>
          <li class="paper-venue">{{ entry.venue }}</li>
          <li class="paper-publish-date">{{ entry.date }}</li>
          {% if entry.note %}
          <li class="paper-special-note">{{ entry.note }} </li>
          {% endif %}
          {% if entry.link or entry.press or entry.website %}
          <li class="paper-links">
            {% if entry.link %}
            <a href="{{entry.link | append: '.pdf' | relative_url }}">[PDF]</a>
            {% endif %}
            {% if entry.website%}
            <a href="{{entry.website}}" target="_blank">[Website]</a>
            {% endif %}
            {% if entry.press %}
            <a href="{{entry.press}}">[Press Coverage]</a>
            {% endif %}
          </li>
          {% endif %}
          <li class="bibtex">
            <button type="button" class="bib-collapsible btn btn-info btn-sm rounded-pill">Bibtex</button>
            <div class="bib-button-content">
              <figure class="full-bib highlight">
                <pre>{{ entry.bib | rstrip }} </pre>
              </figure>
            </div>
          </li>
        </ul>
      </div>
      {% endif %}
      {% endfor %}
    </ul>
  </div>

  <div class="other-publications">
    <h4>Undergraduate Publication</h4>

    <ul class="undergrad-paper-list">
      {% for entry in site.data.bibentries %}
      {% assign authors= entry.author | split: " and "%}
      {% if entry.type=='undergrad' %}
      <div class="paper-entry">
        <li class="paper-title"> {{ entry.title }} </li>
        <ul class="paper-metadata">
          <li class="paper-authors">
            {% for author in authors %}
            {% if author=="Kaushal Kafle" %}
            <strong> {{ author }}, </strong>
            {% elsif author== authors.last %}
            {{ author }}
            {% else %}
            {{ author }},
            {% endif %}
            {% endfor %}
          </li>
          <li class="paper-venue">{{ entry.venue }}</li>
          <li class="paper-publish-date">{{ entry.date }}</li>
          {% if entry.note %}
          <li class="paper-special-note">{{ entry.note }} </li>
          {% endif %}
          {% if entry.link or entry.press or entry.website %}
          <li class="paper-links">
            {% if entry.link %}
            <a href="{{entry.link | append: '.pdf'}}">[PDF]</a>
            {% endif %}
            {% if entry.website%}
            <a href="{{entry.website}}" target="_blank">[Website]</a>
            {% endif %}
            {% if entry.press %}
            <a href="{{entry.press}}">[Press Coverage]</a>
            {% endif %}
          </li>
          {% endif %}
          <li>
            <button type="button" class="bib-collapsible btn btn-info btn-sm rounded-pill">Bibtex</button>
            <div class="bib-button-content">
              <figure class="full-bib highlight">
                <pre>{{ entry.bib | rstrip }} </pre>
              </figure>
            </div>
          </li>
        </ul>
      </div>
      {% endif %}
      {% endfor %}
    </ul>
  </div> <!--other publications-->

  <div class="news-coverage">
    {% include press_coverage.html %}
  </div>

</div>
