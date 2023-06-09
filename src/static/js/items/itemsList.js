function showPassword(itemId, isHidden, passwordElement, buttonElement) {
    if (isHidden) {
        fetch(`/items/show_password/${itemId}`).then(
            r => r.json()
        ).then(
            data => {
                passwordElement.textContent = data.item_password;
                buttonElement.textContent = "Cacher"
            }
        )
    } else {
        passwordElement.textContent = "••••••••••";
        buttonElement.textContent = "Afficher"
    }
}


const buttons = document.querySelectorAll(".button")
buttons.forEach(button => {
    let isHidden = true
    const id = button.parentElement.dataset.id
    const password = document.querySelector(`[data-id='${id}']`).querySelector('.password')
    button.addEventListener("click", () => {
        showPassword(id, isHidden, password, button)
        isHidden = !isHidden
    })
})
