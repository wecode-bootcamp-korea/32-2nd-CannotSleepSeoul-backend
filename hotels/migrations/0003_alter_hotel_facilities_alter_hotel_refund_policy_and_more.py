# Generated by Django 4.0.4 on 2022-05-16 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_room_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='facilities',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='refund_policy',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='service',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='using_time',
            field=models.CharField(max_length=100),
        ),
    ]
