from django.urls import path
from .views import TarefaAPIView, TarefaDetalheAPIView

urlpatterns = [
    path('api-view', TarefaAPIView.as_view() , name="API-view"),
    path('tarefas/<int:pk>/', TarefaDetalheAPIView.as_view() , name="Detalhe-api")
]
