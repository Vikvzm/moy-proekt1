# Generated by Django 4.2.2 on 2023-08-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0002_alter_hobby_name_likes_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hobby',
            options={'verbose_name': 'Композицию', 'verbose_name_plural': 'Композиции'},
        ),
        migrations.AddField(
            model_name='hobby',
            name='catalog',
            field=models.CharField(default=1, max_length=60, verbose_name='Каталог'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hobby',
            name='description',
            field=models.TextField(default='разные', verbose_name='Описание'),
        ),
    ]
