# Generated by Django 3.1.6 on 2021-02-10 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_sector'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sector',
            old_name='id_department',
            new_name='department',
        ),
    ]
