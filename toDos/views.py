from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Livro

def TelaInicial(request):
    return render(request, "toDos/home.html")

class ListarLivrosView(ListView):
    model = Livro

class CadastrarLivrosView(CreateView):
    model = Livro
    fields = ["titulo", "autor", "categoria", "numeropaginas"]
    success_url = reverse_lazy("ListarLivros")

class EditarLivrosView(UpdateView):
    model = Livro
    fields = ["titulo", "autor", "categoria", "numeropaginas"]
    success_url = reverse_lazy("ListarLivros")

class DeletarLivrosView(DeleteView):
    model = Livro
    success_url = reverse_lazy("ListarLivros")