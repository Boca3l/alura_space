# Generated by Django 5.0.6 on 2024-07-07 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_fotografia_ursuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='ursuario',
            new_name='usuario',
        ),
    ]
