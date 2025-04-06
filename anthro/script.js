document.addEventListener("DOMContentLoaded", function () {
  // Die JSON-Datei mit den Veranstaltungseinträgen laden
  fetch('events.json')
    .then(response => {
      if (!response.ok) {
        throw new Error('Fehler beim Laden der Veranstaltungen');
      }
      return response.json();
    })
    .then(events => {
      const now = new Date();
      const currentDate = new Date(now.getFullYear(), now.getMonth(), now.getDate()); // Heute um 00:00 Uhr

      // Nur zukünftige Veranstaltungen (einschließlich heute) filtern
      const upcomingEvents = events.filter(event => {
        const eventDate = new Date(event.date);
        return eventDate >= currentDate;
      });

      const eventsContainer = document.getElementById('events-list');

      if (upcomingEvents.length === 0) {
        // Nachricht anzeigen, wenn keine Veranstaltungen vorhanden sind
        eventsContainer.innerHTML = `
          <p>
            Aktuell sind keine Veranstaltungen geplant. Wir würden uns freuen, Sie bei einer zukünftigen Veranstaltung begrüßen zu dürfen.
            Nehmen Sie gerne Kontakt zu uns auf, um mehr zu erfahren.
          </p>`;
      } else {
        // Veranstaltungen nach Datum sortieren
        upcomingEvents.sort((a, b) => new Date(a.date) - new Date(b.date));

        // Veranstaltungen dynamisch erstellen
        upcomingEvents.forEach(event => {
          const eventElement = document.createElement('div');
          eventElement.classList.add(
            'border-l-4',
            'border-[var(--akzent)]',
            'mb-4',
            'shadow-md',
            'bg-white',
            'rounded',
            'p-4'
          );

          const formattedDate = formatDate(event.date);

          eventElement.innerHTML = `
            <p class="font-bold">${formattedDate} | ${event.time} Uhr</p>
            <p class="font-semibold text-[var(--akzent)]">${event.title}</p>
            <p class="font-semibold">${event.subtitle}</p>
            <p>${event.location}</p>
          `;

          // Modal nur öffnen, wenn Beschreibung vorhanden ist
          if (event.description) {
            eventElement.classList.add('cursor-pointer', 'hover:bg-gray-50', 'transition');
            eventElement.addEventListener('click', () => {
              openModal(event);
            });
          }

          eventsContainer.appendChild(eventElement);
        });
      }
    })
    .catch(error => {
      console.error('Fehler beim Laden der Veranstaltungen:', error);
    });
});

// Funktion zum Formatieren des Datums inkl. deutschem Wochentag
function formatDate(dateString) {
  const date = new Date(dateString);
  const weekdays = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"];
  const weekday = weekdays[date.getDay()];
  const day = String(date.getDate()).padStart(2, '0');
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const year = date.getFullYear();
  return `${weekday}, ${day}.${month}.${year}`;
}

// Funktion zum Öffnen des Modals mit Veranstaltungsdetails
function openModal(event) {
  const modal = document.getElementById('event-modal');
  const modalContent = document.getElementById('modal-content');
  const formattedDate = formatDate(event.date);

  modalContent.innerHTML = `
    <h2 class="text-2xl font-semibold text-[var(--akzent)] mb-2">${event.title}</h2>
    <p class="mb-1">${event.subtitle}</p>
    <p class="mb-1"><span style="font-family: 'Noto Color Emoji';">🗓️</span> ${formattedDate} | ${event.time} Uhr</p>
    <p class="mb-3"><span style="font-family: 'Noto Color Emoji';">📍</span> ${event.location}</p>
    ${event.description ? `<p class="text-gray-700"><span style="font-family: 'Noto Color Emoji';">ℹ️</span> ${event.description}</p>` : ''}
  `;

  modal.classList.remove('hidden');
}

// Modal schließen
document.getElementById('close-modal').addEventListener('click', () => {
  document.getElementById('event-modal').classList.add('hidden');
});
