# Generated by Django 3.1.2 on 2020-10-14 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hdesk', '0029_auto_20201014_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='technics',
            name='busy',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
