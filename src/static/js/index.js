function showPassword(itemId) {
    const passwordField = document.getElementById('password-' + itemId);
    const passwordText = passwordField.getAttribute('data-password');
    passwordField.textContent = passwordText;
}