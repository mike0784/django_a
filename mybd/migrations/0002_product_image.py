# Generated by Django 5.0.1 on 2024-02-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
    ]