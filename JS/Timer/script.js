const date = new Date()

const weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

const dateElement = document.getElementById('date').innerText = `${date.getDate()} - ${date.getMonth() + 1} - ${date.getFullYear()}`
const dayElement = document.getElementById('day').innerHTML= `${weekdays[date.getDay()]}`
const timer = document.getElementById("time")


setInterval(fetchTime, 1000)

function fetchTime(){
    const now = new Date()
    const hours = now.getHours().toString().padStart(2, '0')
    const minutes = now.getMinutes().toString().padStart(2, '0')
    const seconds = now.getSeconds().toString().padStart(2, '0')
    timer.innerHTML = `${hours}:${minutes}:${seconds}`
}