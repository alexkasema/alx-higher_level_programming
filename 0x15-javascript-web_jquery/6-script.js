const $ = window.$;

const header = $('header');
const updateHeader = $('DIV#update_header');

updateHeader.on('click', () => header.text('New Header!!!'));
