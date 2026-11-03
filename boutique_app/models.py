from django.db import models

class Prenda(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=12, default="polera", choices={
        "polera":"Polera",
        "chaleco":"Chaleco",
        "camisa":"Camisa",
        "chaqueta":"Chaqueta",
    })
    color = models.CharField(max_length=12, default="#0000FF", choices={
        "#000000":"Negro",
        "#FFFFFF":"Blanco",
        "#FF0000":"Rojo",
        "#800080":"Morado",
        "#FFC0CB":"Rosado",
        "#008000":"Verde",
        "#0000FF":"Azul",
        "#00FFFF":"Celeste",
        "#FFFF00":"Amarillo"
    })
    talla = models.CharField(max_length=4, default="m", choices={
        "xs":"XS",
        "s":"S",
        "m":"M",
        "l":"L",
        "xl":"XL",
        "xxl":"XXL",
    })
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
