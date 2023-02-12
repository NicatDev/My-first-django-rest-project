# Generated by Django 4.1.2 on 2023-02-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='blogimage/')),
            ],
            options={
                'verbose_name': 'Blog ',
                'verbose_name_plural': 'Blogs',
                'ordering': ('-created_at',),
            },
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]