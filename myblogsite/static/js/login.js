$(document).ready(function() {
    $('#loginForm').submit(function(e) {
        e.preventDefault(); // Evitar que el formulario se envíe de forma predeterminada
        $.ajax({
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: function(data) {
                if (data.error) {
                    // Mostrar pop-up de error
                    alert(data.error);
                } else {
                    // Redirigir al landing page
                    window.location.href = '/';
                }
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // Proporciona un poco más de información sobre el error en la consola.
            }
        });
    });
});

$.ajax({
    type: "POST",
    url: "/accounts/ajax_login/",
    data: {
        username: $('#username').val(),
        password: $('#password').val(),
    },
    beforeSend: function(xhr) {
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    },
    success: function(data) {
        // ...
    },
    error: function(xhr, status, error) {
        // ...
    }
});
