async function loadServices(){

let r = await fetch("services.json")

let data = await r.json()

let html=""

data.forEach(s=>{

if(s.enabled){

html+=`
<div class="card">
<h3>${s.name}</h3>
<p>${s.description}</p>
<p>₹${s.price}</p>
<a href="order.html?service=${s.name}&price=${s.price}">
<button>Order</button>
</a>
</div>
`

}

})

document.getElementById("servicesList").innerHTML=html

}

async function loadCourses(){

let r = await fetch("courses.json")

let data = await r.json()

let html=""

data.forEach(c=>{

if(c.enabled){

html+=`
<div class="card">
<h3>${c.name}</h3>
<p>${c.description}</p>
<p>₹${c.price}</p>
<button>Buy</button>
</div>
`

}

})

document.getElementById("coursesList").innerHTML=html

}

async function loadEbooks(){

let r = await fetch("ebooks.json")

let data = await r.json()

let html=""

data.forEach(e=>{

if(e.enabled){

html+=`
<div class="card">
<h3>${e.name}</h3>
<p>${e.description}</p>
<p>₹${e.price}</p>
<button>Buy</button>
</div>
`

}

})

document.getElementById("ebooksList").innerHTML=html

}

loadServices()
loadCourses()
loadEbooks()