# coding: utf-8
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magna_aquae.settings')

import django

django.setup()

import rbcapp.models.entorno


def populate():

    add_entorno(variavel_entorno="Vegetação", cor="#033403")
    add_entorno(variavel_entorno="Área Urbana", cor="#ba3acb")
    add_entorno(variavel_entorno="Solo Exposto", cor="#d49c00")
    add_entorno(variavel_entorno="Uso do Solo", cor="#74a048")
    add_entorno(variavel_entorno="Vegetação Secundária", cor="#74fb48")
    add_entorno(variavel_entorno="Água Doce", cor="#0055ff")
    add_entorno(variavel_entorno="Água Salobra", cor="#00ffff")
    add_entorno(variavel_entorno="Mar", cor="#afcaff")
    add_entorno(variavel_entorno="Montanha de Pedra", cor="#AA5500")

def add_entorno(variavel_entorno, cor):
    m = rbcapp.models.Entorno.objects.get_or_create(variavel_entorno=variavel_entorno, cor=cor)[0]
    m.variavel_entorno = variavel_entorno
    m.cor = cor

    m.save()
    return m

# Start execution here!
if __name__ == '__main__':
    print("Starting entornos population script...")
    populate()