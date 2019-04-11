# coding: utf-8

from rbcapp.models import Ponto_Monitoramento, Substancia
from django import forms


class FormColeta(forms.Form):
    data_coleta = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        )
    )

    ponto = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
        queryset=Ponto_Monitoramento.objects.all(),
        empty_label="Selecione o ponto"
    )

    valor_coletado = forms.FloatField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

class FormColetaPesquisar(forms.Form):
    data_coleta = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        )
    )

    ponto = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
        queryset=Ponto_Monitoramento.objects.all(),
        empty_label="Selecione o ponto"
    )
