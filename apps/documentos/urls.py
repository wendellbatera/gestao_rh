from django.urls import path, include
from .views import DocumentoCreate

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
    # path('editar/<int:pk>/', EmpresaEdit.as_view(), name='edit_empresa'),
]
