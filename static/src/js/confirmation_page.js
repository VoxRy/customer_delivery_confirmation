document.addEventListener("DOMContentLoaded", function() {
    let nameField = document.getElementById("customer_name");
    let kvkkCheckbox = document.getElementById("kvkk_agreement");
    let confirmButton = document.getElementById("confirmButton");

    function checkForm() {
        if (nameField && kvkkCheckbox && confirmButton) { // Ensure elements exist
            let isNameFilled = nameField.value.trim().length > 0;
            let isChecked = kvkkCheckbox.checked;

            if (isNameFilled && isChecked) {
                confirmButton.removeAttribute("disabled");
                confirmButton.style.backgroundColor = "#007bff"; // Active button
                confirmButton.style.cursor = "pointer";
            } else {
                confirmButton.setAttribute("disabled", "disabled");
                confirmButton.style.backgroundColor = "#6c757d"; // Inactive button
                confirmButton.style.cursor = "not-allowed";
            }
        }
    }

    if (nameField) nameField.addEventListener("input", checkForm);
    if (kvkkCheckbox) kvkkCheckbox.addEventListener("change", checkForm);
});
