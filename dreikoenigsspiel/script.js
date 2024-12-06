// script.js
document.addEventListener('DOMContentLoaded', () => {
    const headers = document.querySelectorAll('.accordion-header');
    
    headers.forEach(header => {
        header.addEventListener('click', () => {
            // Alle anderen Inhalte schließen
            const allContents = document.querySelectorAll('.accordion-content');
            allContents.forEach(content => {
                if (content !== header.nextElementSibling) {
                    content.style.display = 'none';
                }
            });

            // Sichtbarkeit des aktuellen Inhalts toggeln
            const content = header.nextElementSibling;
            if (content.style.display === 'block') {
                content.style.display = 'none';
            } else {
                content.style.display = 'block';
            }
        });
    });
});
