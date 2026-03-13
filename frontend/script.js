function generateOrderId(){
return "CF" + Math.floor(Math.random()*1000000)
}

let form = document.getElementById("orderForm")

if(form){

form.addEventListener("submit",function(e){

e.preventDefault()

let orderId = generateOrderId()

localStorage.setItem("orderId",orderId)

window.location="payment.html"

})

}

let btn = document.getElementById("whatsappBtn")

if(btn){

let orderId = localStorage.getItem("orderId")

let msg = "Hello I completed payment for order "+orderId

btn.href="https://wa.me/YOURNUMBER?text="+encodeURIComponent(msg)

}