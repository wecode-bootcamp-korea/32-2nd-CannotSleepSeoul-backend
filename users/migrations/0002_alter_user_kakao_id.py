# Generated by Django 4.0.4 on 2022-05-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='kakao_id',
            field=models.BigIntegerField(),
        ),
    ]
