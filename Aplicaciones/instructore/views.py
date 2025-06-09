from django import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Curso, Instructor

# Formulario personalizado para Curso con selector de fecha
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
        }

# CRUD Cursos
class CursoListView(ListView):
    model = Curso
    template_name = 'curso_list.html'
    context_object_name = 'cursos'

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso_form.html'
    success_url = reverse_lazy('curso_list')

    def form_valid(self, form):
        messages.success(self.request, 'Curso creado correctamente')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Curso'
        return context

class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso_form.html'
    success_url = reverse_lazy('curso_list')

    def form_valid(self, form):
        messages.success(self.request, 'Curso actualizado correctamente')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Curso'
        return context

class CursoDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy('curso_list')

    def get(self, request, *args, **kwargs):
        messages.success(self.request, 'Curso eliminado correctamente')
        return self.delete(request, *args, **kwargs)

# CRUD Instructores
class InstructorListView(ListView):
    model = Instructor
    template_name = 'instructor_list.html'
    context_object_name = 'instructores'

class InstructorCreateView(CreateView):
    model = Instructor
    fields = '__all__'
    template_name = 'instructor_form.html'
    success_url = reverse_lazy('instructor_list')

    def form_valid(self, form):
        messages.success(self.request, 'Instructor creado correctamente')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Instructor'
        return context

class InstructorUpdateView(UpdateView):
    model = Instructor
    fields = '__all__'
    template_name = 'instructor_form.html'
    success_url = reverse_lazy('instructor_list')

    def form_valid(self, form):
        messages.success(self.request, 'Instructor actualizado correctamente')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Instructor'
        return context

class InstructorDeleteView(DeleteView):
    model = Instructor
    success_url = reverse_lazy('instructor_list')

    def get(self, request, *args, **kwargs):
        messages.success(self.request, 'Instructor eliminado correctamente')
        return self.delete(request, *args, **kwargs)
