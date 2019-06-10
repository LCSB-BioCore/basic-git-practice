# R3.school - Basic git course

## How to get started?

Follow carefully the instructions given during the course.

**Goal**: add your personal page to this site!

## List of course attendees

{% for attendee in site.attendees %}
  <h2>
  {{ forloop.index }}.<a href="{{ attendee.url | prepend: site.baseurl }}">
      {{ attendee.name }} - {{ attendee.position }}
    </a>
  </h2>
{% endfor %}
