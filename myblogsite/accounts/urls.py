#"myblogsite\accounts\urls.py"
from django.urls import path
from . import views
from .views import signup, ajax_login


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('ajax_login/', ajax_login, name='ajax_login'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('check_username/', views.check_username, name='check_username'),
]
