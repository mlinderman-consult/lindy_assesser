
// Improved dashboard_scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Initialize Materialize components
    M.AutoInit();

    // Enhanced event listeners for the dashboard cards
    const cards = document.querySelectorAll('.dashboard-card');

    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            // Adding subtle hover effect
            this.style.boxShadow = '3px 4px 10px rgba(0, 0, 0, 0.2)';
        });

        card.addEventListener('mouseleave', function() {
            // Removing hover effect
            this.style.boxShadow = '';
        });

        card.addEventListener('click', function() {
            // Future navigation or modal functionality
            console.log('Navigating to:', this.querySelector('.card-title').innerText);
            // Placeholder for modal or navigation logic
        });
    });
});
