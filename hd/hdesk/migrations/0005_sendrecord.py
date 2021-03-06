# Generated by Django 3.1.2 on 2020-10-12 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hdesk', '0004_auto_20201012_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(max_length=128)),
                ('send_date', models.DateField()),
                ('ret_date', models.DateField()),
                ('repair_reason', models.CharField(max_length=500)),
                ('technics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Техника', to='hdesk.technics')),
            ],
        ),
    ]
