async function loadServices(){

let r = await fetch("https://cashflow-inat.onrender.com/services")

let data = await r.json()

let html = ""

data.forEach(s=>{

html += `
<div class="card">

<h3>${s.name}</h3>

<p>${s.desc}</p>

<p>Price: ₹${s.price}</p>

<a href="order.html?service=${s.name}&price=${s.price}">
<button>Order Now</button>
</a>

</div>
`

})

document.getElementById("servicesList").innerHTML = html

}

loadServices()
