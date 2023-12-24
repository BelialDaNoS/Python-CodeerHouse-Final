document.addEventListener('DOMContentLoaded', function() {
    var passwordForm = document.getElementById('profileForm');

    passwordForm.onsubmit = function(e) {
        // Si se está cambiando la contraseña, verifica que las nuevas contraseñas coincidan
        var newPassword1 = document.querySelector('input[name="new_password1"]');
        var newPassword2 = document.querySelector('input[name="new_password2"]');
        
        if (newPassword1.value || newPassword2.value) {
            if (newPassword1.value !== newPassword2.value) {
                alert('Las nuevas contraseñas no coinciden.');
                e.preventDefault(); // Prevenir el envío del formulario
            } else {
                // Aquí puedes añadir una llamada AJAX para cambiar la contraseña sin recargar la página
                alert('Contraseña cambiada correctamente.');
            }
        }
    };
});
