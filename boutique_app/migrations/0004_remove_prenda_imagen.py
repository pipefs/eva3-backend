from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("boutique_app", "0003_backfill_prenda_imagen")]
    operations = [migrations.RemoveField(model_name="prenda", name="imagen")]
