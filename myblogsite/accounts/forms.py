#"myblogsite\accounts\forms.py"
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.forms import ImageField
from django.conf import settings


class CustomUserCreationForm(UserCreationForm):
    profile_image = ImageField(required=False, label="Foto de Perfil")
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'profile_image')

class CustomUserChangeForm(UserChangeForm):
    profile_image = ImageField(required=False, label="Foto de Perfil")
    username = forms.CharField(
        label=_("Nombre de usuario"),
        max_length=20,
        help_text=_("Requerido. 20 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente."),
    )
    description = forms.CharField(
        label=_("Escribe información que quieres que el resto vea!"),
        widget=forms.Textarea,
        required=False
    )
    website = forms.URLField(required=False)
    def clean_profile_image(self):
        profile_image = self.cleaned_data.get('profile_image')

        # Si no se ha subido una nueva imagen, simplemente regresa el valor actual
        if not profile_image:
            return self.instance.profile_image

        # Asegúrate de que el archivo sea una imagen
        if not profile_image.name.endswith(('.png', '.jpg', '.jpeg')):
            raise ValidationError('Solo se admiten archivos en formato .png, .jpg y .jpeg.')

        if profile_image and profile_image.size > settings.MAX_UPLOAD_SIZE:
            raise ValidationError(_('El archivo es demasiado grande. Tamaño máximo permitido: %(max_size)s. Tamaño actual: %(current_size)s.') % {
                'max_size': filesizeformat(settings.MAX_UPLOAD_SIZE),
                'current_size': filesizeformat(profile_image.size),
            })

        return profile_image

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'description', 'website', 'profile_image']


class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        if old_password and new_password1:
            if old_password == new_password1:
                raise ValidationError("La nueva contraseña no puede ser la misma que la actual.")
        return new_password1
    
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2:
            if new_password1 != new_password2:
                self.add_error('new_password2', "La confirmación de la contraseña no coincide.")
