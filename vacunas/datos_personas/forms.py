
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import authenticate
from datos_personas.models import Usuario

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(label='nombre')
    Contraseña = forms.IntegerField(label='Contraseña', widget=forms.PasswordInput)
    Contraseña2 = forms.IntegerField(label='Confirmar contraseña', widget=forms.PasswordInput)
    pro =Usuario(nombre='nombre',Contraseña='Contraseña',Contraseña2='Contraseña2')
    pro.save()

    class Meta:
        model = Usuario
        fields = ('nombre','Contraseña','Contraseña2')
        labels = {'nombre': 'Nombre completo', 'Contraseña': 'Contraseña','Contraseña': 'Contraseña'}
        

class AutenticarForm(forms.ModelForm):

    Contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('nombre','Contraseña')

        def clean(self):
            nombre = self.cleaned_data['nombre']
            Contraseña = self.cleaned_data['Contraseña']

            if not authenticate(nombre=nombre, Contraseña=Contraseña):
                raise forms.ValidationError("Datos no correctos")