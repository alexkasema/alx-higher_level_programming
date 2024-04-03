const $ = window.$;

$(document).ready(() => {
  const language = $('INPUT#language_code').val();
  const translateBtn = $('INPUT#btn_translate');
  const displayTranslation = $('DIV#hello');

  translateBtn.on('click', () => {
    $.getJSON(`https://fourtonfish.com/hellosalut/hello/?lang=${language}`, (data, textStatus) => {
      if (textStatus === 'success') {
        displayTranslation.text(data.hello);
      } else if (textStatus === 'error') {
        displayTranslation.text('');
      }
    }).fail(() => displayTranslation.text('Translation not found'));
  });
});
