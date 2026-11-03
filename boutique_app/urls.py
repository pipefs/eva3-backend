from django.urls import path
from . import views

urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("gestion/", views.gestion, name="gestion"),
    path("detalle/<int:id>/", views.detalle, name="detalle"),
    path("crear/", views.crear, name="crear"),
    path("editar/<int:id>/", views.editar, name="editar"),
    path("eliminar/<int:id>/", views.eliminar, name="eliminar"),
]