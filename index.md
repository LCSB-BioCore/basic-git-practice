## How to get started?

**Goal**: add your personal page to this site!


## List of course attendees

{% for attendee in site.attendees %}
  <h2>
  {{ forloop.index }}.<a href="{{ attendee.url | prepend: site.baseurl }}">
      {{ attendee.name }} - {{ attendee.position }}
    </a>
  </h2>
{% endfor %}
