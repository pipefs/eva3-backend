from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from .models import Prenda

def login(request):
    return render(request, 'boutique_app/login.html')

def catalogo(request):
    return render(request, 'boutique_app/catalogo.html')

def gestion(request):
    return render(request, 'boutique_app/gestion.html')

def detalle(request, id):
    prenda = Prenda.objects.get(id=id)
    return render(request, 'boutique_app/detalle.html', {'prenda': prenda})

def crear(request):
    if request.method == 'POST':
        Prenda.objects.create(
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            categoria=request.POST.get('categoria'),
            talla=request.POST.get('talla'),
            color=request.POST.get('color'),
            precio=request.POST.get('precio'),
            stock=request.POST.get('stock')
        )
        return redirect('gestion')
    return render(request, 'boutique_app/crear.html')

def editar(request, id):
    prenda = Prenda.objects.get(id=id)
    if request.method == 'POST':
        prenda.nombre = request.POST.get('nombre')
        prenda.descripcion = request.POST.get('descripcion')
        prenda.categoria = request.POST.get('categoria')
        prenda.talla = request.POST.get('talla')
        prenda.color = request.POST.get('color')
        prenda.precio = request.POST.get('precio')
        prenda.stock = request.POST.get('stock')
        prenda.save()
        return redirect('gestion')
    return render(request, 'boutique_app/editar.html', {'prenda': prenda})

def eliminar(request, id):
    prenda = Prenda.objects.get(id=id)
    if request.method == 'POST':
        prenda.delete()
        return redirect('gestion')
    return render(request, 'boutique_app/eliminar.html', {'prenda': prenda})

class LoginAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            token, creado = Token.objects.get_or_create(user=usuario)

            return Response({
                'mensaje': 'Autenticación correcta!',
                'usuario': usuario.username,
                'token': token.key
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Usuario o contraseña incorrectos.'}, status=status.HTTP_401_UNAUTHORIZED)

class PrendasAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        prendas = Prenda.objects.all()
        datos = []

        for prenda in prendas:
            datos.append({
                'id': prenda.id,
                'nombre': prenda.nombre,
                'descripcion':prenda.descripcion,
                'categoria':prenda.categoria,
                'color':prenda.color,
                'talla':prenda.talla,
                'precio':prenda.precio,
                'stock':prenda.stock,
                'creado':prenda.creado,
                'actualizado':prenda.actualizado
            })

        return Response(datos, status=status.HTTP_200_OK)