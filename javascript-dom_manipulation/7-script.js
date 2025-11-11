// URL de l'API SWAPI films
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Sélectionne l'élément <ul>
const listMovies = document.querySelector('#list_movies');

// Fait la requête pour obtenir les films
fetch(url)
  .then(response => response.json())
  .then(data => {
    data.results.forEach(film => {
      const li = document.createElement('i');
      li.textContent = film.title;
      listMovies.appendChild(li);
    });
  })
  .catch(error => {
    const errorLi = document.createElement('li');
    errorLi.textContent = 'Erreur lors de la récupération des films';
    listMovies.appendChild(errorLi);
    console.error(error);
  });
