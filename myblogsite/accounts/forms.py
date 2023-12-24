from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):
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
    AVATAR_CHOICES = [
        ('avatars/avatar1.png', _('Avatar') + ' 1'),
        ('avatars/avatar2.png', _('Avatar') + ' 2'),
        ('avatars/avatar3.png', _('Avatar') + ' 3'),
        ('avatars/avatar4.png', _('Avatar') + ' 4'),
    ]
    profile_avatar = forms.ChoiceField(choices=AVATAR_CHOICES, label=_("Avatar"), widget=forms.RadioSelect)

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'description', 'website', 'profile_avatar']

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Contraseña actual"), widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=_("Nueva contraseña"), widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=_("Confirme nueva contraseña"), widget=forms.PasswordInput)
