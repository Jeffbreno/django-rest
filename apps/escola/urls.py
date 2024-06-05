from django.urls import path, include
from apps.escola.views import (
    AlunosViewSet,
    CursosViewSet,
    MatriculaViewSet,
    ListaMatriculasAluno,
    ListaAlunosMatriculados,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")
router.register("matricula", MatriculaViewSet, basename="Matriculas")

urlpatterns = [
    path("", include(router.urls)),
    path("alunos/<int:pk>/matriculas/", ListaMatriculasAluno.as_view()),
    path("cursos/<int:pk>/matriculas/", ListaAlunosMatriculados.as_view()),
]
