#"myblogsite\blog\forms.py"
from django import forms
from .models import Blog
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(), label='Contenido') 

    class Meta:
        model = Blog
        fields = ['title', 'category', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'category': 'Categoría',
        }
