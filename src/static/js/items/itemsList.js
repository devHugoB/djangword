function showPassword(itemId, isHidden, passwordElement, iconElement) {
    if (isHidden) {
        fetch(`/items/show_password/${itemId}`).then(
            r => r.json()
        ).then(
            data => {
                passwordElement.textContent = data.item_password;
                iconElement.classList.remove("fa-eye")
                iconElement.classList.add("fa-eye-slash")
            }
        )
    } else {
        passwordElement.textContent = "••••••••••";
        iconElement.classList.remove("fa-eye-slash")
        iconElement.classList.add("fa-eye")
    }
}


const icons = document.querySelectorAll(".button")
icons.forEach(icon => {
    let isHidden = true
    const id = icon.parentElement.dataset.id
    const password = document.querySelector(`[data-id='${id}']`).querySelector('.password')
    icon.addEventListener("click", () => {
        showPassword(id, isHidden, password, icon)
        isHidden = !isHidden
    })
})
