# Generated by Django 3.1.2 on 2020-10-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hdesk', '0005_sendrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendrecord',
            name='repair_reason',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='sendrecord',
            name='ret_date',
            field=models.DateField(blank=True),
        ),
    ]
