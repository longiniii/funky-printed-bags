let images = document.querySelectorAll('.every-image')
let mainImage = document.getElementById('main-image')
let quantity = document.getElementById('quantity')
let add = document.getElementById('add')
let addToCart = document.getElementById("add-to-cart")
let remove = document.getElementById('remove')
let ratingLabel = document.querySelectorAll(".rating-label")
let ratingSubmitButton = document.querySelectorAll(".rate")[0]
let deleteReview = document.querySelectorAll(".delete-review")
let cartSlider = document.getElementById('cart-slider')
let buy = document.getElementById("buy-now")
//let foundReviewhelpful = document.querySelectorAll(".yes-or-no")

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
    if (quantity.value > 1) quantity.value = Number(quantity.value) - 1
})

addToCart.addEventListener('click', function() {
    let currentProductId;
    currentProductId = window.location.href.split('/')[window.location.href.split('/').length - 1]
    fetch('/api/add-to-cart', {
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(
            {
                productQuantity: quantity.value,
                productId: currentProductId
            }
        ),
        method: 'post'
    })
    .then(res => res.text())
    .then(location.reload())
    .then(
        //.style.right = '0',
        //cartSlider.classList.add('cart-slider-opening-animation'),
        //cartSlider.classList.remove('cart-slider-closing-animation')
    )
})

ratingSubmitButton.disabled = true

ratingLabel.forEach(item => {
    item.addEventListener("click", function() {
        ratingSubmitButton.disabled = false
        ratingLabel.forEach(element => {
            if (item.id.includes("rating-label-solid-")) {
                if (element.id.includes("rating-label-solid-")) {
                    if (element.id.split("rating-label-solid-")[1] <= item.id.split("rating-label-solid-")[1])  {
                        element.style.display = "inline-block"
                    }
                    if (element.id.split("rating-label-solid-")[1] > item.id.split("rating-label-solid-")[1])  {
                        element.style.display = "none"
                    }
                } else {
                    if (element.id.split("rating-label-")[1] > item.id.split("rating-label-solid-")[1])  {
                        element.style.display = "inline-block"
                    }
                }
            } else {
                if (element.id.split("rating-label-solid-")[1] <= item.id.split("rating-label-")[1])  {
                    element.style.display = "inline-block"
                } else { 
                    if (element.id.split("rating-label-")[1] <= item.id.split("rating-label-")[1])  {
                        element.style.display = "none"
                    }
                }
            }
        });
    })
});

deleteReview.forEach(item => {
    item.addEventListener("click", function() {
        let userId = item.getAttribute("userId")
        let reviewId = item.getAttribute("reviewId")
        fetch(`/api/delete-review/${userId}/${reviewId}`, {
            method: "delete"
        })
        .then(res => res.text())
        .then(data => {
            item.parentElement.style.display = "none"
        })
    })
});

// foundReviewhelpful.forEach(item => {
//     item.addEventListener("click", function() {
//         let reviewId = item.getAttribute("reviewId")
//         let isHelpful = item.getAttribute("isHelpful")
//         console.log(Boolean(parseInt(isHelpful)))
//         fetch(`/api/was-review-helpful`, {
//             headers: {
//                 "Content-Type": "application/json",
//             },
//             body: JSON.stringify({
//                 reviewId: reviewId,
//                 isHelpful: Boolean(parseInt(isHelpful))
//             }),
//             method: "POST"
//         })
//         .then(res => res.text())
//         .then()    
//     })
// });

buy.addEventListener("click", function() {
    location.reload()
})