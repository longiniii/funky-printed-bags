let images = document.querySelectorAll('.every-image')
let mainImage = document.getElementById('main-image')
let quantity = document.getElementById('quantity')
let add = document.getElementById('add')
let remove = document.getElementById('remove')
mainImage.src = images[0].src
images[0].style.border = '2px solid black'

images.forEach(item => {
    let currentImage;
    item.addEventListener('click', function() {
        currentImage = item
        console.log(item.src)
        mainImage.src = item.src
        console.log(mainImage.src)
        item.style.border = '2px solid black'
        images.forEach(element => {
            if (item != element) {
                element.style.border = 'none'
            }
        });
    })
});

add.addEventListener('click', function() {
    quantity.value = Number(quantity.value) + 1
})

remove.addEventListener('click', function() {
    quantity.value = Number(quantity.value) - 1
})