let navCartOpenButton = document.getElementById('nav-cart-open-button')
let navCartCloseButton = document.getElementById('nav-cart-close-button')
let cartSlider = document.getElementById('cart-slider')
let searchInput = document.getElementById('item-search')
let searchResults = document.getElementById('nav-product-search-results')


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


searchInput.addEventListener('click', function() {
    checkIfFocused()
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