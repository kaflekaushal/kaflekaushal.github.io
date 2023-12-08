---
layout: page
permalink: /publications
title: Publications
---

<div class="publication-list container">
  <div class="conference-papers">
    <h3>Conference</h3>
    <ul class="conference-paper-list">
      {% for entry in site.data.bibentries-conference %}
      {% assign authors= entry.author | split: " and "%}
      {% if entry.type=='conference' %}
      <div class="paper-entry">
        <li class="paper-title"> {{ entry.title }} </li>
        <ul class="paper-metadata">
          <li class="paper-authors">
            {% for author in authors %}
            {% if author=="Kaushal Kafle" %}
             <strong>{{ author }}</strong>, 
            {% elsif author== authors.last %}
            {{ author }}
            {% else %}
            {{ author }},
            {% endif %}
            {% endfor %}
          </li>
          {% if entry.note %}
          <li class="paper-venue">{{ entry.venue }}, {{entry.date}}, {{ entry.note }} </li>
          {% else %}
          <li class="paper-venue">{{ entry.venue }}, {{entry.date}} </li>
          {% endif %}
          {% if entry.link or entry.press or entry.website %}
          <li class="paper-links">
            {% if entry.link %}
            <a href="{{entry.link | relative_url }}">[PDF]</a>
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
  <h3>Conference - Tool Demo</h3>
  <ul class="conference-paper-list">
    {% for entry in site.data.bibentries-tool %}
    {% assign authors= entry.author | split: " and "%}
    {% if entry.type=='tooldemo' %}
    <div class="paper-entry">
      <li class="paper-title"> {{ entry.title }} </li>
      <ul class="paper-metadata">
        <li class="paper-authors">
          {% for author in authors %}
          {% if author=="Kaushal Kafle" %}
           <strong>{{ author }}</strong>, 
          {% elsif author== authors.last %}
          {{ author }}
          {% else %}
          {{ author }},
          {% endif %}
          {% endfor %}
        </li>
        {% if entry.note %}
          <li class="paper-venue">{{ entry.venue }}, {{entry.date}}, {{ entry.note }} </li>
        {% else %}
          <li class="paper-venue">{{ entry.venue }}, {{entry.date}} </li>
        {% endif %}
        {% if entry.link or entry.press or entry.website %}
        <li class="paper-links">
          {% if entry.link %}
          <a href="{{entry.link | relative_url }}">[PDF]</a>
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
  <h3>Journal</h3>
  <ul class="conference-paper-list">
    {% for entry in site.data.bibentries-journal %}
    {% assign authors= entry.author | split: " and "%}
    {% if entry.type=='journal' %}
    <div class="paper-entry">
      <li class="paper-title"> {{ entry.title }} </li>
      <ul class="paper-metadata">
        <li class="paper-authors">
          {% for author in authors %}
          {% if author=="Kaushal Kafle" %}
           <strong>{{ author }}</strong>, 
          {% elsif author== authors.last %}
          {{ author }}
          {% else %}
          {{ author }},
          {% endif %}
          {% endfor %}
        </li>
        {% if entry.note %}
          <li class="paper-venue">{{ entry.venue }}, {{entry.date}}, {{ entry.note }} </li>
        {% else %}
          <li class="paper-venue">{{ entry.venue }}, {{entry.date}} </li>
        {% endif %}
        {% if entry.link or entry.press or entry.website %}
        <li class="paper-links">
          {% if entry.link %}
          <a href="{{entry.link | relative_url }}">[PDF]</a>
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
  <h3>Poster</h3>
  <ul class="conference-paper-list">
    {% for entry in site.data.bibentries-poster %}
    {% assign authors= entry.author | split: " and "%}
    {% if entry.type=='poster' %}
    <div class="paper-entry">
      <li class="paper-title"> {{ entry.title }} </li>
      <ul class="paper-metadata">
        {% if entry.note %}
          <li class="paper-venue">{{ entry.venue }}, {{entry.date}}, {{ entry.note }} </li>
        {% else %}
          <li class="paper-venue">{{ entry.venue }}, {{entry.date}} </li>
        {% endif %}
        {% if entry.link or entry.press or entry.website %}
        <li class="paper-links">
          {% if entry.link %}
          <a href="{{entry.link | relative_url }}">[PDF]</a>
          {% endif %}
          {% if entry.website%}
          <a href="{{entry.website}}" target="_blank">[Website]</a>
          {% endif %}
          {% if entry.press %}
          <a href="{{entry.press}}">[Press Coverage]</a>
          {% endif %}
        </li>
        {% endif %}
      </ul>
    </div>
    {% endif %}
    {% endfor %}
  </ul>
</div>

  <!-- <div class="conference-papers">
    <h4>Undergraduate Publication</h4>

    <ul class="undergrad-paper-list">
      {% for entry in site.data.bibentries-others %}
      {% assign authors= entry.author | split: " and "%}
      {% if entry.type=='undergrad' %}
      <div class="paper-entry">
        <li class="paper-title"> {{ entry.title }} </li>
        <ul class="paper-metadata">
          <li class="paper-authors">
            {% for author in authors %}
            {% if author=="Kaushal Kafle" %}
             <strong>{{ author }}</strong>, 
            {% elsif author== authors.last %}
            {{ author }}
            {% else %}
            {{ author }},
            {% endif %}
            {% endfor %}
          </li>
          {% if entry.note %}
          <li class="paper-venue">{{ entry.venue }}, {{entry.date}}, {{ entry.note }} </li>
        {% else %}
          <li class="paper-venue">{{ entry.venue }}, {{entry.date}} </li>
        {% endif %}
          {% if entry.link or entry.press or entry.website %}
          <li class="paper-links">
            {% if entry.link %}
            <a href="{{entry.link }}">[PDF]</a>
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
  </div>  -->
  <!--other publications-->

  <div class="news-coverage">
    {% include press_coverage.html %}
  </div>

</div>
