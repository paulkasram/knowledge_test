document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registrationForm');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm_password');
    const phone = document.getElementById('phone');
    const email = document.getElementById('email');

    form.addEventListener('submit', function (event) {
        // Basic validation for empty fields
        if (!email.value || !password.value || !confirmPassword.value || !phone.value) {
            alert("Please fill in all fields.");
            event.preventDefault();
            return;
        }

        // Password and confirm password match validation
        if (password.value !== confirmPassword.value) {
            alert("Passwords do not match.");
            event.preventDefault();
            return;
        }

        // Basic phone number validation (example: simple length check)
        const phoneRegex = /^\d{10}$/;  // Example: expect 10 digits for the phone number
        if (!phoneRegex.test(phone.value)) {
            alert("Please enter a valid phone number.");
            event.preventDefault();
            return;
        }
    });
});
