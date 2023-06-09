function showPassword() {
    const buttonElement = document.getElementById("show-button")
    var passwordInput = document.getElementById("id_password");
    console.log(passwordInput)
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        buttonElement.textContent = "Cacher le mot de passe"
    } else {
        passwordInput.type = "password"
        buttonElement.textContent = "Afficher le mot de passe"
    }
}

const button = document.getElementById("show-button")
button.addEventListener("click", () => {
    showPassword()
})