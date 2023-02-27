# Generated by Django 4.1.4 on 2023-01-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created'], 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(null=True, upload_to='product/mains'),
        ),
    ]
