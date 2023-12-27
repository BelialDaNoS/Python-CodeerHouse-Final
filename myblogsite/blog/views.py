#"myblogsite\blog\views.py"
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk) 
    else:
        form = BlogForm()
    return render(request, 'blog/blog_edit.html', {'form': form})

@login_required
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_edit.html', {'form': form})

@login_required
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.user == blog.author:
        blog.delete()
        return redirect('blog_list')
    else:
        return HttpResponse("You are not authorized to delete this blog.")
