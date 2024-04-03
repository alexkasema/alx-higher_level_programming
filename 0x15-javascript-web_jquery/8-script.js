const $ = window.$;

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
const listMovies = $('UL#list_movies');

$.get(url, (data, textStatus) => {
  if (textStatus === 'success') {
    data.results.forEach(movie => {
      const element = $('<li></li>');
      element.text(movie.title);
      listMovies.append(element);
    });
  } else if (textStatus === 'error') {
    element.text('Error');
    listMovies.append(element);
  }
});
