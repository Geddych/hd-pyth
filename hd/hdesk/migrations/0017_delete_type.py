# Generated by Django 3.1.2 on 2020-10-12 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hdesk', '0016_remove_technics_tec_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Type',
        ),
    ]
