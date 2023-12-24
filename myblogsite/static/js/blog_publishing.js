//"myblogsite\static\js\blog_publishing.js"
function showLoginModal() {
    var modal = document.getElementById('login-modal');
    modal.style.display = 'block';
}

function closeModal() {
    var modal = document.getElementById('login-modal');
    modal.style.display = 'none';
}

window.onclick = function(event) {
    var modal = document.getElementById('login-modal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
