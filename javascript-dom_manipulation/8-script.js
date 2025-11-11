window.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      this.document.querySelector('#hello').textContent = data.hello;
    })
    .catch(error => {
      document.querySelector('#hello').textContent = 'Erreur lors de la requête';
      console.error(error);
    });
});
