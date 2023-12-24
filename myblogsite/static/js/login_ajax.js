$(document).ready(function() {
    $('#loginButton').click(function() {
        var username = $('[name="username"]').val();
        var password = $('[name="password"]').val();
        
        $.ajax({
            url: '/accounts/ajax_login/',
            data: {
                'username': username,
                'password': password
            },
            dataType: 'json',
            type: 'POST',
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            success: function(response) {
                if(response.success) {
                    window.location.href = '/';  // Redirige al landing page
                } else {
                    alert(response.error);  // Muestra el pop-up de error
                }
            }
        });
    });
    
    // Función para obtener el CSRF token de las cookies
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
