#"myblogsite\blog\forms.py"
from django import forms
from .models import Blog
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(), label='Contenido')  # Cambia 'body' por 'Contenido' y usa CKEditorWidget

    class Meta:
        model = Blog
        fields = ['title', 'category', 'body', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'category': 'Categoría',
            'image': 'Imágenes',
        }
