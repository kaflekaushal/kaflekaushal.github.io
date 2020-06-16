---
layout: page
permalink: /publications
---

<div class="publication-list container">

  <h2>Conference Papers</h2>

  <ul>
    {% for entry in site.data.bibentries %}
    {% assign authors= entry.author | split: " and "%}
    {% if entry.type=='conference' %}
    <li class="paper-title"> {{ entry.title }} </li>
    <ul>
      <li class="paper-authors">
        {% for author in authors %}
        {% if author=="Kaushal Kafle" %}
        <strong> {{ author }}, </strong>
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
        <div class="bd-clipboard">
          <button class="btn-clipboard" type="button" data-original-title="Copy to clipboard">Copy</button>
        </div>
        <figure class="highlight">
          <pre>{{ entry.bib }} </pre>
        </figure>
      </li>
    </ul>
    {% endif %}
    {% endfor %}
  </ul>

  <div class="other-publication">
    <h4>Undergraduate Publication</h4>

    <ul>
      {% for entry in site.data.bibentries %}
      {% assign authors= entry.author | split: " and "%}
      {% if entry.type=='undergrad' %}
      <li class="paper-title"> {{ entry.title }} </li>
      <ul>
        <li class="paper-authors">
          {% for author in authors %}
          {% if author=="Kaushal Kafle" %}
          <strong> {{ author }}, </strong>
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
          <div class="bd-clipboard">
            <button class="btn-clipboard" type="button" data-original-title="Copy to clipboard">Copy</button>
          </div>
          <figure class="highlight">
            <pre>{{ entry.bib }} </pre>
          </figure>
        </li>
      </ul>
      {% endif %}
      {% endfor %}
    </ul>
  </div>

  <div class="news-coverage">
    <h2 id="press_coverage">Press Coverage</h2>
    <ul>
      <li><strong>Radio</strong>: <a href="https://wina.com/podcasts/hacking-your-smart-home-kaushal-kafle/" target="_blank">WINA</a> </li>

      <li><strong>TV</strong>: <a href="https://www.13newsnow.com/article/news/local/smart-home-devices-can-be-vulnerable-to-hacking/291-5e4a614c-8bcb-46b0-914e-e1f9e3ac5bf4" target="_blank">13NewsNow</a> </li>

      <li> <strong>News Sites</strong>: <a href="https://www.wm.edu/news/stories/2018/smart-home-security-devices-may-be-vulnerable-to-smart-hackers.php">WM Press</a>, <a
          href="https://www.nbcnews.com/tech/tech-news/i-m-your-baby-s-room-nest-cam-hacks-show-n950876" target="_blank">NBC News</a>, <a
          href="https://www.washingtonpost.com/local/computer-scientists-study-security-threats-to-smart-homes/2018/12/28/243a1e6e-0b10-11e9-8942-0ef442e59094_story.html?utm_term=.c8aff4c0b379">Washington Post</a>, <a
          href="https://qz.com/1493748/how-one-lightbulb-could-allow-hackers-to-burgle-your-home/amp/" target="_blank">Quartz</a>, <a href="https://www.dailypress.com/news/science/dp-nws-evg-smart-home-invasion-20181211-story.html"
          target="_blank">DailyPress</a>, <a href="https://www.sfgate.com/news/article/Computer-scientists-study-security-threats-to-13496624.php">SF Gate</a>, <a href="https://www.the-ambient.com/features/new-smart-home-attack-nest-hue-1237">The
          Ambient</a>, <a href="https://www.insurancejournal.com/news/national/2019/01/03/513394.htm">Insurance Journal</a>, <a href="https://www.claimsjournal.com/news/national/2018/12/31/288513.htm">Claims Journal</a>, <a
          href="https://www.dailymail.co.uk/sciencetech/article-6487237/Study-Burglars-hack-smart-sprinkler-disable-alarm.html">Daily Mail</a> </li>
    </ul>
  </div>

</div>
