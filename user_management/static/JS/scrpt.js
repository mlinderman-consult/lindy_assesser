// script.js
// Initialize Materialize Components
document.addEventListener('DOMContentLoaded', function() {
    M.AutoInit();
 
    // View/Hide Password
    const passwordInput = document.querySelector('#password');
    const passwordIcon = document.querySelector('.password-icon');
 
    passwordIcon.addEventListener('click', () => {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password'; 
        passwordInput.setAttribute('type', type);
        passwordIcon.classList.toggle('fa-eye-slash');
    });

});