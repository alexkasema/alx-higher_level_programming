const $ = window.$;

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const character = $('DIV#character');

$.get(url, (data, textStatus) => {
  if (textStatus === 'success') {
    character.text(data.name);
  } else {
    character.text('Not found');
  }
});
