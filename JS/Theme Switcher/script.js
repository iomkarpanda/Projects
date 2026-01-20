const button = document.getElementById("btn")


let theme = localStorage.getItem('theme') || 'dark'

applyTheme(theme)

button.addEventListener("click", () => {
    theme = (theme === 'dark') ? 'light' : 'dark'

    applyTheme(theme)
    localStorage.setItem('theme', theme)
})

function applyTheme(theme) {
    if (theme === 'dark') {
        document.body.style.backgroundColor = "rgb(30, 30, 30)" 
    } else {
        document.body.style.backgroundColor = 'white'
    }
}

