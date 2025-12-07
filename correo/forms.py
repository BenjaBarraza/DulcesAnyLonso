from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Tu nombre', 'class': 'form-input'}))
    email = forms.EmailField(label="Correo", widget=forms.EmailInput(attrs={'placeholder': 'Tu correo', 'class': 'form-input'}))
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'placeholder': 'Cuéntanos qué se te antoja...', 'rows': 4, 'class': 'form-input'}))