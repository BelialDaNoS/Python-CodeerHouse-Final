document.addEventListener('DOMContentLoaded', function() {
    console.log("Cargada la página de cuentas");

    // Validación de Formulario de Registro
    const signupForm = document.querySelector('#signupForm');
    if (signupForm) {
        signupForm.addEventListener('submit', function(event) {
            const passwordField = document.querySelector('#id_password1');
            if (passwordField.value.length < 8) {
                alert('La contraseña debe tener al menos 8 caracteres.');
                event.preventDefault();
            }
        });
    }

    // Mostrar/Ocultar Información del Perfil
    const toggleInfoButton = document.querySelector('#toggleInfoButton');
    const profileInfo = document.querySelector('#profileInfo');
    if (toggleInfoButton && profileInfo) {
        toggleInfoButton.addEventListener('click', function() {
            if (profileInfo.style.display === 'none') {
                profileInfo.style.display = 'block';
                toggleInfoButton.textContent = 'Ocultar Información';
            } else {
                profileInfo.style.display = 'none';
                toggleInfoButton.textContent = 'Mostrar Información';
            }
        });
    }
});


document.getElementById("id_username").addEventListener("keyup", function() {
    var username = this.value;
    
    if (username.length === 20) {
        alert('Has alcanzado el máximo de 20 caracteres.');
    }

    $.ajax({
        url: "{% url 'check_username' %}",
        data: {
            'username': username
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                alert('El nombre de usuario ya existe.');
            }
        }
    });
});

