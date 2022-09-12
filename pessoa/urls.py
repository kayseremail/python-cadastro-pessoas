from django.urls import path
from .views import ListPessoaView, CreatePessoaView, UpdatePessoaView, DeletePessoaView

urlpatterns = [
    path('',ListPessoaView.as_view(),name='pessoa.index'),
    path('create/',CreatePessoaView.as_view(),name='pessoa.create'),
    path('update/<int:pk>',UpdatePessoaView.as_view(),name='pessoa.update'),
    path('delete/<int:pk>',DeletePessoaView.as_view(),name='pessoa.delete')
]