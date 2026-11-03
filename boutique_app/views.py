from django.shortcuts import render, redirect, get_object_or_404
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

class CatalogoAPI(APIView):
    permission_classes = [AllowAny]

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

    def post(self, request):
        datos = request.data

        campos_obligatorios = [
            'nombre',
            'categoria',
            'color',
            'talla',
            'precio',
            'stock'
        ]

        faltantes = [
            campo for campo in campos_obligatorios
            if datos.get(campo) in [None, '']
        ]

        if faltantes:
            return Response({
                'error': 'Faltan campos obligatorios.',
                'campos': faltantes
            }, status=status.HTTP_400_BAD_REQUEST)

        prenda = Prenda.objects.create(
            nombre=datos.get('nombre'),
            descripcion=datos.get('descripcion'),
            categoria=datos.get('categoria'),
            color=datos.get('color'),
            talla=datos.get('talla'),
            precio=datos.get('precio'),
            stock=datos.get('stock')
        )

        return Response({
            'mensaje': 'Prenda creada correctamente.',
            'prenda': {
                'id': prenda.id,
                'nombre': prenda.nombre,
                'descripcion': prenda.descripcion,
                'categoria': prenda.categoria,
                'color': prenda.color,
                'talla': prenda.talla,
                'precio': prenda.precio,
                'stock': prenda.stock
            }
        }, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        prenda = get_object_or_404(Prenda, id=id)
        datos = request.data

        campos_obligatorios = [
            'nombre',
            'categoria',
            'color',
            'talla',
            'precio',
            'stock'
        ]

        faltantes = [
            campo for campo in campos_obligatorios
            if datos.get(campo) in [None, '']
        ]

        if faltantes:
            return Response({
                'error': 'Faltan campos obligatorios.',
                'campos': faltantes
            }, status=status.HTTP_400_BAD_REQUEST)

        prenda.nombre = datos.get('nombre')
        prenda.descripcion = datos.get('descripcion')
        prenda.categoria = datos.get('categoria')
        prenda.color = datos.get('color')
        prenda.talla = datos.get('talla')
        prenda.precio = datos.get('precio')
        prenda.stock = datos.get('stock')

        prenda.save()

        return Response({
            'mensaje': 'Prenda actualizada correctamente.',
            'prenda': {
                'id': prenda.id,
                'nombre': prenda.nombre,
                'descripcion': prenda.descripcion,
                'categoria': prenda.categoria,
                'color': prenda.color,
                'talla': prenda.talla,
                'precio': prenda.precio,
                'stock': prenda.stock
            }
        }, status=status.HTTP_200_OK)

    def delete(self, request, id):
        prenda = get_object_or_404(Prenda, id=id)
        prenda.delete()

        return Response({
            'mensaje': 'Prenda eliminada correctamente.'
        }, status=status.HTTP_200_OK)