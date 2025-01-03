// Globale Variable für die aktuelle Woche
let currentWeek = getCustomWeek();

// Funktion zum Laden und Einfügen des HTML-Codes
function loadHTML(filePath, targetElementId) {
    fetch(filePath)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP-Fehler: ${response.status}`);
            }
            return response.text();
        })
        .then(htmlContent => {
            const targetElement = document.getElementById(targetElementId);
            if (targetElement) {
                targetElement.innerHTML = htmlContent;
            } else {
                console.error(`Element mit ID "${targetElementId}" nicht gefunden.`);
            }
        })
        .catch(error => {
            console.error(`Fehler beim Laden des HTML-Codes...: ${error.message}`);
        });
}

// Funktion zur Berechnung der aktuellen Woche (Freitag-Donnerstag)
function getCustomWeek() {
    const today = new Date();
    const dayOfWeek = today.getDay(); // Sonntag = 0, Montag = 1, ..., Samstag = 6

    // Anpassung für Freitag-Donnerstag-Woche
    const adjustment = (dayOfWeek >= 5) ? 0 : (dayOfWeek + 2);
    const referenceDate = new Date(today);
    referenceDate.setDate(today.getDate() - adjustment);

    // Berechnung der ISO-Woche
    const jan4 = new Date(referenceDate.getFullYear(), 0, 4);
    const firstWeekStart = new Date(jan4);
    firstWeekStart.setDate(jan4.getDate() - (jan4.getDay() || 7) + 1);

    const weekNumber = Math.ceil((referenceDate - firstWeekStart) / (7 * 24 * 60 * 60 * 1000));
    return weekNumber;
}

// Dynamisch den Link erzeugen
function generateLink(weekNumber) {
    const baseUrl = "./woche-";
    const link = `${baseUrl}${weekNumber}.html`;
    return link;
}

// Funktion zum Laden einer Woche
function loadWeek(weekOffset, targetElementId) {
    currentWeek += weekOffset; // Woche aktualisieren
    const htmllink = generateLink(currentWeek);
    loadHTML(htmllink, targetElementId);
}

// Funktion zum Laden der aktuellen Woche
function loadCurrentWeek(targetElementId) {
    currentWeek = getCustomWeek(); // Woche neu berechnen
    const htmllink = generateLink(currentWeek);
    loadHTML(htmllink, targetElementId);
}

// Initialen Inhalt laden
loadWeek(0, 'content');

// Event-Listener für Buttons hinzufügen
document.getElementById('prevButton').addEventListener('click', () => loadWeek(-1, 'content'));
document.getElementById('nextButton').addEventListener('click', () => loadWeek(1, 'content'));
document.getElementById('currentWeekButton').addEventListener('click', () => loadCurrentWeek('content'));
