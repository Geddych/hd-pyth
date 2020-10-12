# Generated by Django 3.1.2 on 2020-10-12 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hdesk', '0014_remove_sendrecord_technics'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendrecord',
            name='depart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Отделение', to='hdesk.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sendrecord',
            name='technics',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Техника', to='hdesk.technics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technics',
            name='tec_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Тип', to='hdesk.type'),
            preserve_default=False,
        ),
    ]