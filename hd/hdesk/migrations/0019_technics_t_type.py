# Generated by Django 3.1.2 on 2020-10-12 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hdesk', '0018_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='technics',
            name='t_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Тип', to='hdesk.type'),
            preserve_default=False,
        ),
    ]
