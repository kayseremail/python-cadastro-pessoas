from django.shortcuts import render
from django.views.generic import TemplateView #conteúdo customizado

# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/index.html' #caminho do html sem precisar passar o folder templates
