let giftCard = document.getElementById('gift-card')
let header = document.getElementById('header')
let informationPrice = document.getElementById('i-price')
let quantityDivSubtract = document.getElementById('qd-subtract')
let quantityDivQuantity = document.getElementById('qd-quantity')
let quantityDivAdd = document.getElementById('qd-add')
let amountLabel = document.querySelectorAll('.paq-amount-label')
let activeAmount = amountLabel[0]
let forSomeoneElse = document.getElementById('paq-for-someone-else')
let forMyself = document.getElementById('paq-for-myself')
let forSomeoneElseAndMyself = document.querySelectorAll('.paq-for-someone-else-or-for-myself-input-and-label')
let paqSubmit = document.getElementById('paq-submit')
giftCard.style.marginTop = header.offsetHeight + 'px'
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
