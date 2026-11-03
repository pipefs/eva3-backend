from django.db import migrations


COLOR_SLUGS = {
    "#000000": "negro", "#FFFFFF": "blanco", "#FF0000": "rojo",
    "#800080": "morado", "#FFC0CB": "rosado", "#008000": "verde",
    "#0000FF": "azul", "#00FFFF": "celeste", "#FFFF00": "amarillo",
}


def populate_image_paths(apps, schema_editor):
    Prenda = apps.get_model("boutique_app", "Prenda")
    for prenda in Prenda.objects.all():
        color = COLOR_SLUGS.get(str(prenda.color).upper(), "blanco")
        prenda.imagen = f"boutique_app/images/products/{prenda.categoria}-{color}.jpg"
        prenda.save(update_fields=["imagen"])


class Migration(migrations.Migration):
    dependencies = [("boutique_app", "0002_prenda_imagen")]
    operations = [migrations.RunPython(populate_image_paths, migrations.RunPython.noop)]
