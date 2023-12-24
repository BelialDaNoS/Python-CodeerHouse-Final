//"myblogsite\accounts\static\js\edit_profile_script.js"
document.addEventListener('DOMContentLoaded', function() {
    var profileForm = document.getElementById('profileForm');

    if (profileForm) {
        profileForm.onsubmit = function(e) {
            e.preventDefault(); // Prevenir el envío del formulario por defecto

            var newPassword1 = document.querySelector('input[name="new_password1"]');
            var newPassword2 = document.querySelector('input[name="new_password2"]');
            var oldPassword = document.querySelector('input[name="old_password"]');

            // Validación de coincidencia de contraseñas nuevas
            if (newPassword1.value !== newPassword2.value) {
                alert('Las contraseñas nuevas no coinciden.');
                return;
            }

            // Validación para asegurar que la nueva contraseña no es la misma que la antigua
            if (newPassword1.value === oldPassword.value) {
                alert('La nueva contraseña no puede ser la misma que la anterior.');
                return;
            }

            var formData = new FormData(profileForm);

            fetch('/accounts/edit_profile/', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (response.redirected) {
                    window.location.href = response.url;
                } else {
                    return response.json();
                }
            })
            .then(data => {
                if (data && !data.success) {
                    alert("Error: " + data.errors); // Mostrar mensaje de error
                } else if (data) {
                    alert('Contraseña cambiada correctamente.');
                    // Aquí puedes agregar una redirección o actualización de la página, si es necesario
                }
            });
        };
    }
});
