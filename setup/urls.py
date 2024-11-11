"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from toDos.views import ListarLivrosView, TelaInicial, CadastrarLivrosView, EditarLivrosView, DeletarLivrosView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TelaInicial, name="home"),
    path("livros/", ListarLivrosView.as_view(), name="ListarLivros"),
    path("livro/add/", CadastrarLivrosView.as_view(), name="CadastrarLivros"),
    path("livro/edit/<int:pk>", EditarLivrosView.as_view(), name="EditarLivros"),
    path("livro/delete/<int:pk>", DeletarLivrosView.as_view(), name="DeletarLivros")
]
