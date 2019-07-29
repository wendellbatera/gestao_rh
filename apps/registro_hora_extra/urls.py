from django.urls import path, include
from .views import HoraExtraList

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    # path('editar/<int:pk>/', EmpresaEdit.as_view(), name='edit_empresa'),
]
