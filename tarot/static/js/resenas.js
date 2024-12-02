// Capturar la reseña y mostrarla en el carrusel
document.getElementById('resenaForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevenir la recarga de la página al enviar el formulario

    // Obtener los valores del formulario
    const nombre = document.getElementById('nombreCliente').value;
    const calificacion = document.getElementById('calificacion').value;
    const resena = document.getElementById('resena').value;

    // Crear el HTML de la reseña
    const resenaHTML = `
      <div class="carousel-item ${document.querySelectorAll('.carousel-item').length === 0 ? 'active' : ''}">
        <div class="d-block w-100 text-center">
          <h5>${nombre}</h5>
          <p class="text-warning">${'★'.repeat(calificacion)}${'☆'.repeat(5 - calificacion)}</p>
          <p>${resena}</p>
        </div>
      </div>
    `;

    // Agregar la reseña al carrusel
    document.getElementById('reseñasCarruselInner').insertAdjacentHTML('beforeend', resenaHTML);

    // Limpiar el formulario después de enviar
    document.getElementById('resenaForm').reset();
  });