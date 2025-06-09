# Aplicaciones/instructore/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs para Cursos
    path('cursos/', views.CursoListView.as_view(), name='curso_list'),
    path('curso/nuevo/', views.CursoCreateView.as_view(), name='curso_create'),
    path('curso/editar/<int:pk>/', views.CursoUpdateView.as_view(), name='curso_update'),
    path('curso/eliminar/<int:pk>/', views.CursoDeleteView.as_view(), name='curso_delete'),
    
    # URLs para Instructores
    path('instructores/', views.InstructorListView.as_view(), name='instructor_list'),
    path('instructor/nuevo/', views.InstructorCreateView.as_view(), name='instructor_create'),
    path('instructor/editar/<int:pk>/', views.InstructorUpdateView.as_view(), name='instructor_update'),
    path('instructor/eliminar/<int:pk>/', views.InstructorDeleteView.as_view(), name='instructor_delete'),
]
