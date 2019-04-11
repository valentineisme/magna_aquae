# coding:utf-8
from datetime import datetime
from django import forms
from cpf_validator import CPF
from rbcapp.models import Usuario


class UsuarioForm(forms.ModelForm):
    
    cpf = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'pattern': '(\\d+\\.?)+', 'title': 'Apenas números.', 'minlength': 11,'maxlength':11, 'placeholder': 'Apenas números'}
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True'}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'required': 'True'}
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True'}
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'required': 'True'}
        )
    )

    senha_conferir = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'required': 'True'}
        )
    )

    pergunta = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True'}
        )
    )

    resposta = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True'}
        )
    )

    class Meta:
        model = Usuario
        exclude = ('date_joined', 'is_staff', 'user_permissions', 'groups', 'last_login', 'is_superuser',
        'is_active')

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if CPF(cpf).isValid():
            return cpf
        else:
            raise forms.ValidationError("CPF inválido.")



    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
