// Funktion zum Laden und Einfügen des HTML-Codes
function loadHTML(filePath, targetElementId) {
    // Abrufen der Datei mit fetch
    fetch(filePath)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP-Fehler: ${response.status}`);
            }
            return response.text(); // HTML-Inhalt als Text zurückgeben
        })
        .then(htmlContent => {
            // Einfügen des HTML-Inhalts in das Ziel-Element
            const targetElement = document.getElementById(targetElementId);
            if (targetElement) {
                targetElement.innerHTML = htmlContent;
            } else {
                console.error(`Element mit ID "${targetElementId}" nicht gefunden.`);
            }
        })
        .catch(error => {
            console.error(`Fehler beim Laden des HTML-Codes: ${error.message}`);
        });
}

// Beispiel: HTML-Datei laden und in ein Div mit der ID "content" einfügen
loadHTML('./woche-03.html', 'content');
