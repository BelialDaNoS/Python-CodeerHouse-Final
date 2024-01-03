#"myblogsite\myblogsite\views.py"
from django.shortcuts import render, redirect
from blog.models import Blog
from django.contrib.auth.decorators import login_required
from blog.forms import BlogForm 

def landing(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'landing.html', {'blogs': blogs})


@login_required
def publish_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()  # Crea una instancia de BlogForm para pasar al contexto
    return render(request, 'blog/blog_edit.html', {'form': form})