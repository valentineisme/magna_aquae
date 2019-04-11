# coding: utf-8

from rbcapp.models import Bacia_Hidrografica
from django import forms


class FormRio(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True'}
        )
    )

    dimensao = forms.FloatField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'pattern': '(\\d+\\.?)+', 'title': 'Apenas números e ponto'}
        )
    )

    bacia_hidrografica = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'required': 'True'}
        ),
        queryset=Bacia_Hidrografica.objects.all(),
        empty_label='Selecione uma Bacia Hidrográfica'
    )
