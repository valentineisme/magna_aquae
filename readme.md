# Magna Aqua

Magna Aqua é um ambiente computacional utilizando Raciocínio Baseado em Casos e Geoprocessamento para monitoramento da Bacia Hidrográfica do Rio Parati.

### Sobre

O projeto desenvolvido no Núcleo de Operacionalização e Desenvolvimento de Sistemas (NODES) do Intituto Federal Catarinense (IFC) Campus Araquari, fomentado pelo CNPq, entre os anos de 2015 e 2016. Envolveu alunos do Bacharelado de Sistemas de Informação (BSI), alunos do Técnico em Informática integrado ao Ensino Médio e do Técnico em Química integrado ao Ensino Médio.


### Tecnologias Utilizadas

* Python - Linguagem de programação
* Django - Framework Web para Python
* SemanticUI - Framework CSS
* PostgreSQL - Gerenciador de Banco de Dados


### Instalação

É necessário possuir Python 2.7 e PIP instalados.

Para instalar as dependências do projeto, é necessário executar o comando:

```sh
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
```

Para executar, basta executar o comando:

```sh
$ python manage.py runserver
```
