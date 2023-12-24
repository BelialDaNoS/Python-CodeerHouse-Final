//"myblogsite\static\js\login_ajax.js"
$(document).ready(function() {
    $('#loginForm').submit(function(e) {
        e.preventDefault(); // Evitar que el formulario se envíe de forma predeterminada
        $.ajax({
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: function(data) {
                if (data.error) {
                    alert(data.error);
                } else {
                    window.location.href = '/';
                }
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // Proporciona un poco más de información sobre el error en la consola.
            }
        });
    });
});

