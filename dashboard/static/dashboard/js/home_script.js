const cards = document.querySelectorAll(".card")

cards.forEach((card) => {
    card.addEventListener("onmouseover", () => {
        removeCardActive()
        card.classList.add("active")
    })
})

function removeCardActive(){
    cards.forEach((card) => {
        card.classList.remove("active")
    })
}