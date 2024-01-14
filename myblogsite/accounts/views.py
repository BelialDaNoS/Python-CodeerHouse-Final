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
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        print("request.POST:", request.POST)
        print("request.FILES:", request.FILES)
        
        if 'update_username' in request.POST:
            new_username = request.POST.get('username')
            if User.objects.filter(username=new_username).exists():
                messages.error(request, "El nombre de usuario ya está en uso.")
            else:
                request.user.username = new_username
                request.user.save()
                messages.success(request, "Nombre de usuario actualizado.")

        if 'update_email' in request.POST:
            new_email = request.POST.get('email')
            if User.objects.filter(email=new_email).exists():
                messages.error(request, "El email ya está en uso.")
            else:
                request.user.email = new_email
                request.user.save()
                messages.success(request, "Email actualizado.")
                
        # Verifica si se está actualizando la imagen o si se está guardando todo
        if 'update_image' in request.POST or 'update_all' in request.POST:
            if 'profile_image' in request.FILES:
                if user_form.is_valid():
                    user = user_form.save(commit=False)
                    user.profile_image = request.FILES['profile_image']
                    user.save()
                    messages.success(request, "Imagen de perfil actualizada.")
                    print("Imagen guardada en:", user.profile_image.path)
                else:
                    messages.error(request, "Error al actualizar la imagen de perfil.")
                    print("Errores del formulario de usuario:", user_form.errors)


        if 'update_description' in request.POST:
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "Descripción actualizada.")

        if 'update_password' in request.POST:
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, request.user)  # Importante para no desloguear al usuario
                messages.success(request, "Contraseña actualizada.")

        if 'update_all' in request.POST:
            if user_form.is_valid() and password_form.is_valid():
                user = user_form.save(commit=False)
                if 'profile_image' in request.FILES:
                    user.profile_image = request.FILES['profile_image']
                user.save()
                password_form.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, "Todos los cambios guardados.")

        return redirect('profile')

    else:
        user_form = CustomUserChangeForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)
        return render(request, 'accounts/edit_profile.html', {'user_form': user_form, 'password_form': password_form})
