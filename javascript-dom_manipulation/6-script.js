// URL de l'API SWAPI
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Récupérer le nom du personnage et l'afficher dans #character
fetch(url)
  .then(response => response.json())
  .then(data => {
    const name = data.name;
    document.querySelector('#character').textContent = name;
  })
  .catch(error => {
    document.querySelector('#character').textContent = 'Erreur lors de la requête';
    console.error(error);
  });
