from django.shortcuts import render, redirect
from .models import Prenda

def catalogo(request):
    prendas = Prenda.objects.all()
    return render(request, 'boutique_app/catalogo.html', {'prendas': prendas})

def gestion(request):
    prendas = Prenda.objects.all()
    return render(request, 'boutique_app/gestion.html', {'prendas': prendas})

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
