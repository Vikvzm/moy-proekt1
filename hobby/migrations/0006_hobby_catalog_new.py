# Generated by Django 4.2.2 on 2023-09-05 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0005_alter_catalog_options_catalog_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobby',
            name='catalog_new',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hobby', to='hobby.catalog'),
        ),
    ]
