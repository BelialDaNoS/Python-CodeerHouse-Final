#"myblogsite\blog\urls.py"
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('new/', views.blog_create, name='blog_new'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<int:pk>/edit/', views.blog_update, name='blog_edit'),
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
]
