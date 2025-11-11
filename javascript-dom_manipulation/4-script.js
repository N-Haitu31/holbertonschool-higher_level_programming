const addItem = document.querySelector('#add_item');

addItem.addEventListener('click', function () {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';

  const myList = document.querySelector('.my_list');

  myList.appendChild(newLi);
})
