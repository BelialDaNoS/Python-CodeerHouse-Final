#"myblogsite\blog\views.py"
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def blog_list(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

@login_required
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'form': form})


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
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
        return redirect(reverse('landing'))
    else:
        return HttpResponse("You are not authorized to delete this blog.")

@login_required
def add_comment_to_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        text = request.POST.get('text')
        comment = Comment.objects.create(blog=blog, author=request.user, text=text)
        comment.save()
        return redirect('blog_detail', pk=blog.pk)
    return render(request, 'blog/add_comment.html', {'blog': blog})


def about(request):
    return render(request, 'about.html')
