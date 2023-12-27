#"myblogsite\blog\forms.py"
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'body', 'image']  # Asegúrate de que 'category' esté en tu modelo
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),  # Agrega un widget para 'category'
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            # Agrega widgets para otros campos si es necesario
        }
