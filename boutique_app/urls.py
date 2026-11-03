from django.urls import path
from . import views

urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("login/", views.login, name="login"),
    path("gestion/", views.gestion, name="gestion"),
    path("detalle/<int:id>/", views.detalle, name="detalle"),
    path("crear/", views.crear, name="crear"),
    path("editar/<int:id>/", views.editar, name="editar"),
    path("eliminar/<int:id>/", views.eliminar, name="eliminar"),

    # API Autenticacion
    path("api/login/", views.LoginAPI.as_view(), name='api_login'),

    # API get
    path("api/catalogo/", views.CatalogoAPI.as_view(), name='api_catalogo'),
    path("api/prendas/", views.PrendasAPI.as_view(), name='api_prendas'),
]