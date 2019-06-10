## What is this?

This page is an automatically generated page of the course attendees.

Add your name and your **personal page** to this site!


## List of course attendees

{% for attendee in site.attendees %}
  <h2>
  {{ forloop.index }}.<a href="{{ attendee.url | prepend: site.baseurl }}">
      {{ attendee.name }} - {{ attendee.position }}
    </a>
  </h2>
{% endfor %}
