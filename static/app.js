let store = document.getElementById('store')
let header = document.getElementById('header')
let products = document.querySelectorAll('.product')
let productImages = document.querySelectorAll('.product-image')
let productImagesPatterns = document.querySelectorAll('.image-pattern')
let view = document.querySelectorAll('.view')
// let deleteProduct = document.querySelectorAll('.delete')
let timeLeftSection = document.getElementById('time-left')
let timeLeft = document.getElementById('time-left-main')
let timeLeftBoxes = document.querySelectorAll('.time-left-time')
let days = document.getElementById('d-days')
let hours = document.getElementById('h-hours')
let minutes = document.getElementById('m-minutes')
let seconds = document.getElementById('s-seconds')
let search = document.getElementById('item-search')
let pages = document.querySelectorAll(".page")

let bags;

products.forEach((element, index) => {
    element.addEventListener('mouseover', function() {
        productImages[index].style.display = 'none'
        productImagesPatterns[index].style.display = 'block'
    });
    element.addEventListener('mouseout', function() {
        productImagesPatterns[index].style.display = 'none'
        productImages[index].style.display = 'block'
    });        element.addEventListener('mouseover', function() {
        view[index].style.display = 'block'
        // deleteProduct[index].style.display = 'block'
    });
    element.addEventListener('mouseout', function() {
        view[index].style.display = 'none'
        // deleteProduct[index].style.display = 'none'
    });
});


var countDownDate = new Date("Jul 16, 2024 00:00:000").getTime();

let x = setInterval(function() {
    let now = new Date().getTime();
    let distance = countDownDate - now;
    if (distance <= 0) {
        timeLeftBoxes.forEach(item => {
            item.style.display = 'none'
        });
        timeLeftSection.style.height = '15rem'
        timeLeft.innerText = 'THE BIGGEST SALE OF THE YEAR HAS BEGUN'
        clearInterval(x)
    } else {
        days.innerText = Math.floor(distance / (1000 * 60 * 60 * 24));
        hours.innerText = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        minutes.innerText = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        seconds.innerText = Math.floor((distance % (1000 * 60)) / 1000);
    }
}, 1000);


let url = new URL(window.location.href);
let params = new URLSearchParams(url.search);
let page = params.get("page")
pages.forEach(item => {
    item.addEventListener("click", function() {
        console.log(url)
        params.set('page', item.innerText);
        url.search = params.toString();
        window.location = url.href
    })
    if (page == item.innerText) {
        item.style.backgroundColor = "black";
        item.style.color = "white"
    } else if (page == null) {
        pages[0].style.backgroundColor = "black"
        pages[0].style.color = "white"
    }
});