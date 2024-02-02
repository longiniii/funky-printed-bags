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