# Generated by Django 4.2 on 2023-04-19 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipmentapp', '0006_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='productcat', verbose_name='catimage'),
        ),
    ]