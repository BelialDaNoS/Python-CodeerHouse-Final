#"myblogsite\myblogsite\views.py"
from django.shortcuts import render, redirect
from blog.models import Blog
from django.contrib.auth.decorators import login_required

def landing(request):
    blogs = Blog.objects.order_by('-date')[:2]
    return render(request, 'landing.html', {'blogs': blogs})


@login_required
def publish_blog(request):
    if request.method == 'POST':
        # Asumiendo que tienes un formulario para crear/editar el blog
        # Puedes usar un formulario de Django o manejar los datos directamente
        title = request.POST.get('title')
        content = request.POST.get('content')
        # ... cualquier otro dato del formulario

        # Crear o actualizar el blog
        blog, created = Blog.objects.update_or_create(
            id=request.POST.get('blog_id'),  # Si es una edición, 'blog_id' debería estar presente
            defaults={'title': title, 'content': content, 'author': request.user}
        )

        # Redirigir a la página de detalles del blog
        return redirect('blog_detail', blog_id=blog.id)
    else:
        return render(request, 'blog_edit.html')