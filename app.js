fetch('./data.json')
.then(response => response.json())
.then(data =>  products(data))
let store = document.getElementById('store')
let header = document.getElementById('header')
store.style.marginTop = header.offsetHeight + 48 + 'px'
let product;
let productImage;
let add;
let discount;
let topSeller;
let timeLeft = document.getElementById('tl-main')
let days = document.getElementById('d-days')
let hours = document.getElementById('h-hours')
let minutes = document.getElementById('m-minutes')
let seconds = document.getElementById('s-seconds')
let products = (d) => {
    d.forEach((item, index) => {
        store.innerHTML +=
        `<div class="s-product">
            <div class="p-image-div">
                <div class="id-top-seller"><p>Top Seller</p></div>
                <img class="id-image" src="${item.images[0]}" alt="">
                <div class="id-discount"><p>Discount!!</p></div>
            </div>
            <div class="p-text">
                <p class="t-name">${item.name}</p>
                <p class="t-cost">$${item.cost - 0.01}</p>
                <button class="t-add">Add to Cart</button>
            </div>
        </div>`
        product = document.querySelectorAll('.s-product')
        productImage = document.querySelectorAll('.id-image')
        add = document.querySelectorAll('.t-add')
        discount = document.querySelectorAll('.id-discount')
        topSeller = document.querySelectorAll('.id-top-seller')
        if (!item.topSeller) {
            topSeller[index].style.display = 'none'
        }
        if (!item.discount) {
            discount[index].style.display = 'none'
        }
    });
    product.forEach((element, index) => {
        console.log(element)
        element.addEventListener('mouseover', function() {
            productImage[index].setAttribute('src',`${d[index].images_patterns[0]}`);
        });
        element.addEventListener('mouseout', function() {
            productImage[index].setAttribute('src',`${d[index].images[0]}`);
        });
        element.addEventListener('mouseover', function() {
            add[index].style.display = 'block'
        });
        element.addEventListener('mouseout', function() {
            add[index].style.display = 'none'
        });
    });
}
var countDownDate = new Date("Mar 03, 2024 00:00:000").getTime();

let x = setInterval(function() {
    let now = new Date().getTime();
    let distance = countDownDate - now;
    if (distance <= 0) {
        timeLeft.innerText = 'THE BIGGEST SALE OF THE YEAR HAS BEGUN'
        clearInterval(x)
    } else {
        days.innerText = Math.floor(distance / (1000 * 60 * 60 * 24));
        hours.innerText = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        minutes.innerText = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        seconds.innerText = Math.floor((distance % (1000 * 60)) / 1000);
        console.log(days + "d " + hours + "h " + minutes + "m " + seconds + "s ");
    }
}, 1000);