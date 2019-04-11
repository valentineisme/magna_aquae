# coding: utf-8

from rbcapp.models import Rio
from django import forms


class FormPonto(forms.Form):
    latitude = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'pattern': '(\\d+\\.?)+', 'title': 'Apenas números e ponto'}
        )
    )

    longitude = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'pattern': '(\\d+\\.?)+', 'title': 'Apenas números e ponto'}
        )
    )

    rio = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'required': 'True'}
        ),
        queryset=Rio.objects.all(),
        empty_label='Selecione um Rio'
    )
