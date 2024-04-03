const $ = window.$;

$(document).ready(() => {
  const addItem = $('DIV#add_item');
  const removeItem = $('DIV#remove_item');
  const clearList = $('DIV#clear_list');

  const myList = $('UL.my_list');

  addItem.on('click', () => {
    const item = $('<li></li>').text('Item');
    myList.append(item);
  });

  removeItem.on('click', () => {
    myList.children().last().remove();
  });

  clearList.on('click', () => {
    myList.empty();
  });
});
