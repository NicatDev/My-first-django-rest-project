# Generated by Django 4.1.2 on 2022-12-07 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipmentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-id',), 'verbose_name': 'Comment', 'verbose_name_plural': 'Commentler'},
        ),
    ]
