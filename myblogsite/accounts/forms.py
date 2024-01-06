#"myblogsite\accounts\forms.py"
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')  # Add any other fields you need

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
        ('avatars/avatar1.png', 'Avatar 1'),
        ('avatars/avatar2.png', 'Avatar 2'),
        ('avatars/avatar3.png', 'Avatar 3'),
        ('avatars/avatar4.png', 'Avatar 4'),
        ('avatars/default-avatar.png', 'Default Avatar'),
    ]
    profile_avatar = forms.ChoiceField(choices=AVATAR_CHOICES, label="Avatar", widget=forms.RadioSelect)

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'description', 'website', 'profile_avatar']


class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        if old_password and new_password1:
            if old_password == new_password1:
                raise ValidationError(_("La nueva contraseña no puede ser la misma que la anterior."))
        return new_password1
