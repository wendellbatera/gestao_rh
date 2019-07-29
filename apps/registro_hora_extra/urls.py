from django.urls import path, include
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete, HoraExtraNovo

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo/', HoraExtraNovo.as_view(), name='create_registro_hora_extra'),
    path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='edit_hora_extra'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),

]
