# Generated by Django 5.0.1 on 2024-01-21 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=8)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('destrict', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('home', models.CharField(max_length=100)),
                ('liter', models.CharField(max_length=3)),
                ('flat', models.CharField(max_length=4)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(to='mybd.product')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mybd.user')),
            ],
        ),
    ]
