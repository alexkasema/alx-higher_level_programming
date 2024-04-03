const $ = window.$;

$(document).ready(() => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  const divHello = $('DIV#hello');

  $.getJSON(url, (data, textStatus) => {
    if (textStatus === 'success') {
      divHello.text(data.hello);
    } else if (textStatus === 'error') {
      divHello.text('Error');
    }
  });
});
