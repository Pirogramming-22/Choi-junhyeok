// Fetch the items from the JSON file
function loadItems(){
    return fetch('data/data.json')
    .then(response=>response.json())
    .then(json=>json.items);
}

// Update the list with the given items
function displayItems(items){
    const container=document.querySelector('.items');
    container.innerHTML=items.map(item=>createHtmlString(item)).join('');
}

// Create HTML list item from the given data item
function createHtmlString(item){
    return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item__thumbnail">
        <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `;
}

function setEventListener(items){
    const logo=document.querySelector('.logo');
    const buttons=document.querySelector('.buttons');
    logo.addEventListener('click',()=>displayItems(items));
    buttons.addEventListener('click',()=>onButtonClick(event, items));
}

function onButtonClick(event,items){
    const dataset=event.target.dataset;
    const key=dataset.key;
    const value=dataset.value;

    if (key==null || value==null){
        return;
    }
    displayItems(items.filter(item=>item[key]===value));
}

// Make the items matching {keys:value} invisible.
function updateItems(items,key,value){
    items.forEach(item=>{
        if (item.dataset[key]==value){
            item.classList.remove('invisible');
        }
        else{
            item.classList.add('invisible');
        }
    });
}

//main
loadItems()
    .then(items=>{
    displayItems(items);
    setEventListener(items);
})
.catch(console.log);