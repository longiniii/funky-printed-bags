let giftCard = document.getElementById('gift-card')
let header = document.getElementById('header')
let informationPrice = document.getElementById('price')
let quantityDivSubtract = document.getElementById('subtract')
let quantityDivQuantity = document.getElementById('quantity')
let quantityDivAdd = document.getElementById('add')
let amountLabel = document.querySelectorAll('.amount-label')
let activeAmount = amountLabel[0]
let forSomeoneElse = document.getElementById('for-someone-else')
let forMyself = document.getElementById('for-myself')
let forSomeoneElseAndMyself = document.querySelectorAll('.for-someone-else-or-for-myself-input-and-label')
let paqSubmit = document.getElementById('submit')
quantityDivSubtract.disabled = true
quantityDivSubtract.style.cursor = 'default'
sessionStorage.setItem('amount',25)

amountLabel.forEach(element => {
    element.addEventListener('click', function() {
        this.style.color = 'red'
        amountLabel.forEach(item => {
            if (item !== this) item.style.color = 'black'
        })
        sessionStorage.setItem('amount',this.innerText.slice(1))
        activeAmount = this
        informationPrice.innerText = `$${activeAmount.innerText.slice(1) * quantityDivQuantity.innerText}`
        sessionStorage.setItem('price', informationPrice.innerText.slice(1))
    });
});


quantityDivSubtract.addEventListener('click', subtract = () => {
    quantityDivQuantity.innerText--
    informationPrice.innerText = `$${activeAmount.innerText.slice(1) * quantityDivQuantity.innerText}`
    sessionStorage.setItem('quantity',quantityDivQuantity.innerText)
    sessionStorage.setItem('price', informationPrice.innerText.slice(1))
    inRange(quantityDivQuantity.innerText)
})
quantityDivAdd.addEventListener('click', subtract = () => {
    quantityDivQuantity.innerText++
    informationPrice.innerText = `$${activeAmount.innerText.slice(1) * quantityDivQuantity.innerText}`
    sessionStorage.setItem('quantity',quantityDivQuantity.innerText)
    sessionStorage.setItem('price', informationPrice.innerText.slice(1))
    inRange(quantityDivQuantity.innerText)
})
let inRange = (n) => {
    if (n == 1) {
        quantityDivSubtract.disabled = true
        quantityDivSubtract.style.cursor = 'default'
    } else if (n == 10) {
        quantityDivAdd.disabled = true
        quantityDivAdd.style.cursor = 'default'
    } else {
        quantityDivSubtract.disabled = false
        quantityDivAdd.disabled = false
        quantityDivSubtract.style.cursor = 'pointer'
        quantityDivAdd.style.cursor = 'pointer'
    }
}
forMyself.addEventListener('click', function() {
    forSomeoneElseAndMyself.forEach(element => {
        element.style.display = 'none'
    });
    forMyself.style.backgroundColor = 'black'
    forMyself.style.color = 'white'
    forSomeoneElse.style.backgroundColor = 'white'
    forSomeoneElse.style.color = 'black'
    paqSubmit.style.top ='28.5%'
})
forSomeoneElse.addEventListener('click', function() {
    forSomeoneElseAndMyself.forEach(element => {
        element.style.display = 'block'
    });
    forSomeoneElse.style.backgroundColor = 'black'
    forSomeoneElse.style.color = 'white'
    forMyself.style.backgroundColor = 'white'
    forMyself.style.color = 'black'
    paqSubmit.style.top ='83%'
})
paqSubmit.addEventListener('click',function() {
    window.location.assign('/gift-card-checkout')
})