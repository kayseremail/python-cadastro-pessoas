from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pessoa
from .forms import PessoaForm

# Create your views here.

class ListPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')
    
    def get_queryset(self):
        queryset=super().get_queryset()
        filtro_nome=self.request.GET.get('nome') or None
        
        if filtro_nome:
            queryset=queryset.filter(nome_completo__contains=filtro_nome)
        
        return queryset
    
class CreatePessoaView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoa/'
    
class UpdatePessoaView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoa/'
    
class DeletePessoaView(DeleteView):
    model = Pessoa
    success_url = '/pessoa/'
