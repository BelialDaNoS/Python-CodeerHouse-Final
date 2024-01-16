# "myblogsite\accounts\views.py"
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
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
    user_form = CustomUserChangeForm(request.POST or None, request.FILES or None, instance=request.user)
    password_form = CustomPasswordChangeForm(user=request.user, data=request.POST or None)

    if request.method == 'POST':
        # Bandera para verificar si algún formulario es válido
        is_form_valid = False

        # Verificar si estamos actualizando la imagen del perfil
        if 'update_image' in request.POST:
            if 'profile_image' in request.FILES:
                user = user_form.save(commit=False)
                user.profile_image = request.FILES['profile_image']
                is_form_valid = True

        # Verificar si estamos actualizando la contraseña
        if 'update_password' in request.POST:
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, request.user)
                is_form_valid = True

        # Si actualizamos todo, o si una de las secciones anteriores es válida, guardar el usuario
        if 'update_all' in request.POST or is_form_valid:
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "Perfil actualizado con éxito.")
            else:
                messages.error(request, "Por favor, corrija los errores en el formulario.")

        return redirect('profile')

    context = {
        'user_form': user_form,
        'password_form': password_form,
    }
    return render(request, 'accounts/edit_profile.html', context)
