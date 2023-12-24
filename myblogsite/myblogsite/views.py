#"myblogsite\myblogsite\views.py"
from django.shortcuts import render
from blog.models import Blog

def landing(request):
    blogs = Blog.objects.order_by('-date')[:2]
    return render(request, 'landing.html', {'blogs': blogs})
