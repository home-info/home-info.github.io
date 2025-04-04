document.addEventListener("DOMContentLoaded", function() {
  // Die JSON-Datei mit den Veranstaltungseinträgen laden
  fetch('events.json')
    .then(response => response.json())
    .then(events => {
      // Den Container für die Veranstaltungen holen
      const eventsContainer = document.getElementById('events-list');

      // Die Veranstaltungen dynamisch hinzufügen
      events.forEach(event => {
        const eventElement = document.createElement('div');
        eventElement.classList.add('border-l-4', 'border-[var(--rot)]', 'pl-4', 'mb-4');

        eventElement.innerHTML = `
          <p class="font-semibold">${event.date}, ${event.time} Uhr</p>
          <p class="italic">${event.title}</p>
          <p>Mit ${event.speaker}<br>Ort: ${event.location}</p>
        `;

        eventsContainer.appendChild(eventElement);
      });
    })
    .catch(error => {
      console.error('Fehler beim Laden der Veranstaltungen:', error);
    });
});
