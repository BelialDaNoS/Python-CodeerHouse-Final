#"myblogsite\accounts\urls.py"
from django.urls import path
from . import views
from .views import signup, ajax_login
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('ajax_login/', ajax_login, name='ajax_login'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
