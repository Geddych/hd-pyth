# Generated by Django 3.1.2 on 2020-10-09 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hdesk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carthridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hdesk.department')),
            ],
            options={
                'verbose_name': 'Картридж',
                'verbose_name_plural': 'Картриджи',
            },
        ),
    ]