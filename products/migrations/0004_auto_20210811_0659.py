# Generated by Django 3.2.6 on 2021-08-11 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productmodel_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productbrandmodel',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='productbrandmodel',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='productbrandmodel',
            name='title_uz',
        ),
    ]
