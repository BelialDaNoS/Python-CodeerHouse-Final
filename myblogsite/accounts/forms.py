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

        if profile_image and not profile_image.content_type.startswith('image'):
            raise ValidationError(_('Solo se permiten archivos de imagen.'))

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
                raise ValidationError(_("La nueva contraseña no puede ser la misma que la anterior."))
        return new_password1
