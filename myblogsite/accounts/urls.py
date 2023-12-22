from django.urls import path
from . import views
from .views import signup


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('ajax_login/', views.ajax_login, name='ajax_login'),
]
