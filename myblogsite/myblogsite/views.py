from django.shortcuts import render
from blog.models import Blog

def landing(request):
    blogs = Blog.objects.order_by('-date')[:2]  # Obtener los últimos 2 blogs
    return render(request, 'landing.html', {'blogs': blogs})
