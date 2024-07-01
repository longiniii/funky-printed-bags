let navCartOpenButton = document.getElementById('nav-cart-open-button')
let navCartCloseButton = document.getElementById('nav-cart-close-button')
let cartSlider = document.getElementById('cart-slider')
let searchInput = document.getElementById('item-search')
let searchResults = document.getElementById('nav-product-search-results')
let productsData = document.querySelectorAll('.nav-search-product')
let searchedProducts = productsData
let cartProductDelete = document.querySelectorAll(".cart-product-delete")
let cartCheckout = document.getElementById("cart-checkout")


if (navCartOpenButton != null) { // incase user is not logged in and doe snot have a cart
    navCartOpenButton.addEventListener('click', function() {
        cartSlider.style.right = '0'
        cartSlider.classList.add('cart-slider-opening-animation')
        cartSlider.classList.remove('cart-slider-closing-animation')
    })
    
    navCartCloseButton.addEventListener('click', function() {
        cartSlider.style.right = '-30rem'
        cartSlider.classList.add('cart-slider-closing-animation')
        cartSlider.classList.remove('cart-slider-opening-animation')
    })
    
}




searchInput.addEventListener('click', function() {
    checkIfFocused()
})

searchInput.addEventListener('keyup', function(event) {
    if (event.key == "Enter") {
        let searchTerm = searchInput.value
        window.location = "/" + "?search=" + searchTerm
    }
})


let checkIfFocused = () => {
    let isMouseOverResults = false;
    searchResults.addEventListener('mouseenter', () => {
        isMouseOverResults = true;
        searchResults.style.display = 'block';
    });
    searchResults.addEventListener('mouseleave', () => {
        isMouseOverResults = false;
        if (document.activeElement !== searchInput) {
            searchResults.style.display = 'none';
        }
    });
    let focusInterval = setInterval(() => {
        if (document.activeElement == searchInput || isMouseOverResults) {
            searchResults.style.display = 'block';
        } else {
            searchResults.style.display = 'none';
            clearInterval(focusInterval)
        }
    }, 20);
}


if (cartProductDelete != null) { // incase user is not logged in and doe snot have a cart
    cartProductDelete.forEach(item => {
        item.addEventListener("click", function() {
            let cartProductId = item.getAttribute("cartProductId")
            fetch(`/api/delete-cart-product/${cartProductId}`, {
                method: "delete"
            })
            .then(res => res.text())
            .then(data => {
                item.parentElement.parentElement.style.display = "none"
            })    
        })
    });
}
if (cartCheckout != null) { // incase user is not logged in and doe snot have a cart
    cartCheckout.addEventListener("click", function() {
        fetch(`/api/delete-cart-product/-1`, {
            method: "delete"
        })
        .then(res => res.text())
        .then(
            setTimeout(() => {
                location.reload()
            }, 200)
        ) 
    })
}