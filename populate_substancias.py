# coding: utf-8
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magna_aquae.settings')

import django

django.setup()

import rbcapp.models.substancia


def populate():

    add_substancia(nome="Oxigenio Dissolvido")
    add_substancia(nome="Coliformes Termotolerantes")
    add_substancia(nome="Potencial Hidrogenico - pH")
    add_substancia(nome="DBO 5.20")
    add_substancia(nome="Temperatura da Agua")
    add_substancia(nome="Nitrogenio Total")
    add_substancia(nome="Fosforo Total")
    add_substancia(nome="Residuo Total")
    add_substancia(nome="Turbidez")
    add_substancia(nome="Cadmio")
    add_substancia(nome="Cromo Total")
    add_substancia(nome="Cobre Dissolvido")
    add_substancia(nome="Ferro Dissolvido")
    add_substancia(nome="Chumbo")
    add_substancia(nome="Mercurio")
    add_substancia(nome="Niquel")
    add_substancia(nome="Fenois Totais")
    add_substancia(nome="Surfactantes")
    add_substancia(nome="Zinco")
    add_substancia(nome="PFHTM")
    add_substancia(nome="Numero de Celulas Cianobacterias")
    add_substancia(nome="Manganes")
    add_substancia(nome="Aluminio Dissolvido")
    add_substancia(nome="Clorofila")


def add_substancia(nome):
    m = rbcapp.models.Substancia.objects.get_or_create(nome=nome)[0]
    m.nome = nome

    m.save()
    return m

# Start execution here!
if __name__ == '__main__':
    print("Starting substancias population script...")
    populate()