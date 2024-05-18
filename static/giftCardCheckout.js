let checkout = document.getElementById('checkout')
let header = document.getElementById('header2')
let qQuantity = document.getElementById('summary-quantity-text')
let gcdPrice = document.getElementById('price')
let gcdQuantity = document.getElementById('details-quantity')
let gcdAmount = document.getElementById('amount')
let satSubtotal = document.getElementById('subtotal')
let satTax = document.getElementById('tax')
let satTotal = document.getElementById('total-text')

qQuantity.innerText = `Order summary(${sessionStorage.getItem('quantity')})`
gcdPrice.innerText = `$${sessionStorage.getItem('price')}`
gcdQuantity.innerText = `Qty:${sessionStorage.getItem('quantity')}`
gcdAmount.innerText = `$${sessionStorage.getItem('amount')}`
satSubtotal.innerText = `$${sessionStorage.getItem('price')}`
satTax.innerText = `$${Math.round(sessionStorage.getItem('price') / 12) / 10}`
satTotal.innerText = `$${Number(satTax.innerText.slice(1)) + Number(satSubtotal.innerText.slice(1))}`