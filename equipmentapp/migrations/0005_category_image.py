# Generated by Django 4.2 on 2023-04-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipmentapp', '0004_remove_subcategory_category_remove_product_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]