const $ = window.$;

const addItem = $('div#add_item');
const myList = $('ul.my_list');
const listElement = $('<li></li>').text('Item');

$(function () {
  addItem.on('click', () => myList.append(listElement));
});
