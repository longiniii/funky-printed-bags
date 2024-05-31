let images = document.querySelectorAll('.every-image')
let mainImage = document.getElementById('main-image')
let quantity = document.getElementById('quantity')
let add = document.getElementById('add')
let addToCart = document.getElementById("add-to-cart")
let remove = document.getElementById('remove')

let cartSlider = document.getElementById('cart-slider')

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

addToCart.addEventListener('click', function() {
    let currentProductId;
    currentProductId = window.location.href.split('/')[window.location.href.split('/').length - 1]
    console.log(currentProductId)
    fetch('/api/add-to-cart', {
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(
            {
                userId: 122,
                productId: currentProductId
            }
        ),
        method: 'post'
    })
    .then(res => res.text())
    .then(data => console.log(data))
})


addToCart.addEventListener('click', function() {
    cartSlider.style.right = '0'
    cartSlider.classList.add('cart-slider-opening-animation')
    cartSlider.classList.remove('cart-slider-closing-animation')
    fetch('/api/add-to-cart', {
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(
            {
                userId: 122,
                productId: 12
            }
        ),
        method: 'post'
    })
    .then(res => res.text())
    .then(data => console.log(data))
})