from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    password1 = forms.CharField(label='Ingrese Contraseña', widget=forms.TextInput(attrs={'id':'password1','autocomplete':"off",'type':'password', 'class':'form-control','placeholder':'Ingrese la contraseña'}))
    password2 = forms.CharField(label='Confirme Contraseña', widget=forms.TextInput(attrs={'id':'password2','autocomplete':"off",'type':'password', 'class':'form-control','placeholder':'Vuelva a Ingresar la Contraseña'}))
    username = forms.CharField(label='Ingrese el Nombre de Usuario', widget=forms.TextInput(attrs={'id':'username','type':'text', 'class':'form-control','placeholder':'Ingrese el Nombre de Usuario'}))
    class Meta:
        model = User
        fields = ('username','password1', 'password2', )