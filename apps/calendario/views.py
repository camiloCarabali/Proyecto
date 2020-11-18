from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .forms import *


class Inicio(TemplateView):
    template_name = 'index.html'

class Calendario(ListView):
    model = Actividad
    template_name = 'calendario/actividad/calendario.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(estado = True)
        return queryset


class CrearActividad(CreateView):
    model = Actividad
    template_name = 'calendario/actividad/crear.html'
    form_class = ActividadForm
    success_url = reverse_lazy('calendario:listar')


class ListadoActividad(ListView):
    model = Actividad
    template_name = 'calendario/actividad/listar.html'
    context_object_name = 'actividades'
    queryset = Actividad.objects.filter(estado=True)

    def get(self, request, *args, **kwargs):
        queryset = request.GET.get("buscar")
        actividades = Actividad.objects.filter(estado=True)
        if queryset:
            actividades = Actividad.objects.filter(
                Q(titulo__icontains=queryset),
                estado=True
            ).distinct()
        paginator = Paginator(actividades, 5)
        page = request.GET.get('page')
        actividades = paginator.get_page(page)
        return render(request, self.template_name, {'actividades': actividades})


class ActualizarActividad(UpdateView):
    model = Actividad
    template_name = 'calendario/actividad/crear.html'
    form_class = ActividadForm
    success_url = reverse_lazy('calendario:listar')


class EliminarActividad(DeleteView):
    model = Actividad

    def post(self, request, pk, *args, **kwargs):
        object = Actividad.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('calendario:listar')
