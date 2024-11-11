# Projeto Django CRUD

Este projeto é um sistema CRUD simples desenvolvido em Django para gerenciar informações de autores, livros e categorias. 
O sistema permite adicionar, editar, visualizar e excluir entradas de livros, e apenas visualizar entradas de autores e categorias.
O projeto possui configurações que isolam o banco de dados e implementa conceitos de herança de views genéricas.

## Estrutura do Projeto

- categoria: {nome}
- autor: {nome, data_nascimento}
- livro: {titulo, autor, categoria, numeropaginas}

## Requisitos

- Python 3.12
- Pycharm
- Django

## Configuração

1. Acesse o site oficial do [Python](https://www.python.org/) e faça o download. Durante a instalação, marque a opção "Add Python to PATH".
2. Instale o [PyCharm](https://www.jetbrains.com/pycharm/download/).
3. Abra o PyCharm e clique em "New Project".
4. Selecione "Django" no painel à esquerda.
5. Marque a opção para criar um novo ambiente virtual (Virtualenv), marque a caixa de seleção para instalar o Django e depois clique em "Create".
6. No arquivo settings.py do projeto você pode configurar o banco de dados, como também idioma e fuso horário. 

## Referências
- [Crie um projeto completo com Django - Youtube](https://www.youtube.com/watch?v=MsUL3Pgofl4)
