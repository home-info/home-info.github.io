// Funktion zur Berechnung der Kalenderwoche (Freitag-Donnerstag)
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

    const weekNumber = Math.ceil(((referenceDate - firstWeekStart) / (7 * 24 * 60 * 60 * 1000)) + 1);
    return weekNumber;
}

// Dynamisch den Link erzeugen
function generateLink() {
    const weekNumber = getCustomWeek();
    const baseUrl = "./woche-";
    const link = `<a href="${baseUrl}${weekNumber}.html">Aktuelle Woche</a>`;
    document.getElementById("speiseplan-link2").innerHTML = link;
}

// Sobald die Seite geladen ist, den Link erstellen
window.onload = generateLink;
