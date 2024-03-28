document.addEventListener('DOMContentLoaded', () => {
    fetch('/getItems')
    .then(response => response.json())
    .then(data => {
        let user = 'test';
        const items = document.querySelectorAll('.new-item');
        Object.entries(data).forEach(([key, value]) => {
            console.log(key);
            const catagory = document.createElement('h2');
            catagory.className = 'menu-category';
            catagory.textContent = key;
            items[0].appendChild(catagory);
            Object.entries(items).forEach(([item, itemUser]) => {
                if(itemUser === user) {
                    console.log(item);
                    const paragraph = document.createElement('p');
                    paragraph.className = 'menu-list';
                    paragraph.textContent = item;
                    items[0].appendChild(paragraph);
                }
            });
        });
    })
})