from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from Ensaladas.models import Salads
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ListadoEnsaladas(ListView):
    model = Salads
    context_object_name = 'listado_de_ensaladas'
    template_name = 'Ensaladas/poke.html'
    
    def get_queryset(self):
        Tipo = self.request.GET.get('tipo', '')
        if Tipo:
            listado_de_ensaladas = self.model.objects.filter(Tipo__icontains=Tipo)
        else:
            listado_de_ensaladas = self.model.objects.all()
        return listado_de_ensaladas

    
class CrearEnsaladas(LoginRequiredMixin, CreateView):
    model = Salads
    template_name = "Ensaladas/new_poke.html"
    fields = ['Tipo', 'Sabor', 'Adic_ingre', 'Cantidad']
    success_url = reverse_lazy('ensaladas')


class ActualizarEnsaladas(LoginRequiredMixin, UpdateView):
    model = Salads
    template_name = "Ensaladas/act_poke.html"
    fields = ['Tipo', 'Sabor', 'Adic_ingre', 'Cantidad']
    success_url = reverse_lazy('ensaladas')


class DetalleEnsaladas(DetailView):
    model = Salads
    template_name = "Ensaladas/detalle_poke.html"


class EliminarEnsaladas(LoginRequiredMixin, DeleteView):
    model = Salads
    template_name = "Ensaladas/delete.html"
    success_url = reverse_lazy('ensaladas')
