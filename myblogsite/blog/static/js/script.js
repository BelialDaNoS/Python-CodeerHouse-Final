document.addEventListener('DOMContentLoaded', function() {
    // Ejemplo: Mostrar un mensaje de bienvenida en la consola
    console.log("Bienvenido al Blog!");

    // Ejemplo: Cambiar color de todos los títulos h1 al pasar el mouse
    const headings = document.querySelectorAll('h1');
    headings.forEach(heading => {
        heading.addEventListener('mouseover', () => {
            heading.style.color = 'blue';
        });
        heading.addEventListener('mouseout', () => {
            heading.style.color = 'black';
        });
    });

    // Ejemplo: Ocultar y mostrar contenido
    const toggleContentButton = document.getElementById('toggleContentButton');
    if (toggleContentButton) {
        toggleContentButton.addEventListener('click', () => {
            const content = document.getElementById('toggleContent');
            if (content.style.display === 'none') {
                content.style.display = 'block';
            } else {
                content.style.display = 'none';
            }
        });
    }
});
