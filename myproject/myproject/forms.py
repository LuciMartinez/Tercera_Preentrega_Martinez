from django import forms
from .models import Libro, Autor, Editorial

class LibroForm(forms.ModelForm):
    autor = forms.ModelChoiceField(queryset=Autor.objects.all())
    editorial = forms.ModelChoiceField(queryset=Editorial.objects.all())

    class Meta:
        model = Libro
        fields = ('titulo', 'autor', 'editorial')