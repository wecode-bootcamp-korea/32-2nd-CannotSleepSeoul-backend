# Generated by Django 4.0.4 on 2022-05-11 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=1000)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('hotels_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
                ('users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='ReviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200, null=True)),
                ('reviews_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.review')),
            ],
            options={
                'db_table': 'review_images',
            },
        ),
    ]
