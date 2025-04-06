document.addEventListener("DOMContentLoaded", function() {
  // Die JSON-Datei mit den Veranstaltungseinträgen laden
  fetch('events.json')
    .then(response => {
      if (!response.ok) {
        throw new Error('Fehler beim Laden der Veranstaltungen');
      }
      return response.json();
    })
    .then(events => {
      // Den aktuellen Zeitpunkt holen
      const now = new Date();
      const currentDate = new Date(now.getFullYear(), now.getMonth(), now.getDate()); // Heute um 00:00 Uhr


      // Nur zukünftige Veranstaltungen filtern
      const upcomingEvents = events.filter(event => {
      const eventDate = new Date(event.date);
      // Event auch anzeigen, wenn es heute ist
      return eventDate >= currentDate;
      });


      // Den Container für die Veranstaltungen holen
      const eventsContainer = document.getElementById('events-list');

      // Wenn keine Veranstaltungen vorhanden sind
      if (upcomingEvents.length === 0) {
        // Text anzeigen, wenn keine Veranstaltungen geplant sind
        eventsContainer.innerHTML = `<p>Aktuell sind keine Veranstaltungen geplant. Wir würden uns freuen, Sie bei einer zukünftigen Veranstaltung begrüßen zu dürfen. Nehmen Sie gerne Kontakt zu uns auf, um mehr zu erfahren.</p>`;
      } else {
        // Die Veranstaltungen nach Datum aufsteigend sortieren
        upcomingEvents.sort((a, b) => new Date(a.date) - new Date(b.date));

        // Die Veranstaltungen dynamisch hinzufügen
        upcomingEvents.forEach(event => {
          const eventElement = document.createElement('div');
          //eventElement.classList.add('border-l-4', 'border-[var(--rot)]', 'pl-4', 'mb-4');
          eventElement.classList.add('border-l-4', 'border-[var(--rot)]', 'pl-8', 'mb-4', 'shadow-md', 'bg-[var(--weiß)]', 'rounded');

          // Datum und Wochentag im Format TT.MM.JJJJ (mit Wochentag) umformatieren
          const formattedDate = formatDate(event.date);

          eventElement.innerHTML = `
            <p class="font-semibold">${formattedDate} | ${event.time} Uhr</p>
            <p class="font-semibold text-[var(--rot)]">${event.title}</p>
            <p class="italic">${event.subtitle}</p>
            <p>Ort: ${event.location}</p>
          `;

          eventsContainer.appendChild(eventElement);
        });
      }
    })
    .catch(error => {
      console.error('Fehler beim Laden der Veranstaltungen:', error);
    });
});

// Funktion zum Umformatieren des Datums und Hinzufügen des Wochentags
function formatDate(dateString) {
  const date = new Date(dateString); // Datum im ISO-Format (YYYY-MM-DD) umwandeln

  // Wochentag auf Deutsch ermitteln
  const weekdays = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"];
  const weekday = weekdays[date.getDay()]; // Wochentag ermitteln (0 = Sonntag, 1 = Montag, etc.)

  // Datum im Format TT.MM.JJJJ umformatieren
  const day = String(date.getDate()).padStart(2, '0'); // Tag (immer 2 Stellen)
  const month = String(date.getMonth() + 1).padStart(2, '0'); // Monat (immer 2 Stellen)
  const year = date.getFullYear(); // Jahr

  return `${weekday}, ${day}.${month}.${year}`; // Wochentag vor dem Datum hinzufügen
}
