# Generated by Django 4.0.4 on 2022-05-11 09:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reservation_code', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('deleted_at', models.DateTimeField(null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'reservations',
            },
        ),
    ]
