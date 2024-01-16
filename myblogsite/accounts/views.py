# "myblogsite\accounts\views.py"
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm

def ajax_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None and user.is_active:
        login(request, user)
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False, "error": "Credenciales inválidas."})

def check_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado.')

            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Muy importante para mantener la sesión del usuario
                messages.success(request, 'Tu contraseña ha sido actualizada.')
            else:
                messages.error(request, 'Por favor, corrige el error en la contraseña.')

        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'password_form': password_form
    })