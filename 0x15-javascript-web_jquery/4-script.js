const $ = window.$;

const header = $('header');
const toggleClassHeader = $('div#toggle_header');

toggleClassHeader.on('click', () => header.toggleClass('red green'));
