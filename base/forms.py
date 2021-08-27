from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    sobrenome = forms.CharField(label='Sobrenome')
    email = forms.EmailField(label='email')