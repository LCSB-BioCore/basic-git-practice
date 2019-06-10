# How to get started?

Here is a list of course attendees:

{% for attendee in site.attendees %}
  <h2>
  {{ forloop.index }}.<a href="{{ attendee.url }}">
      {{ attendee.name }} - {{ attendee.position }}
    </a>
  </h2>
  <p>{{ attendee.content | markdownify }}</p>
{% endfor %}
