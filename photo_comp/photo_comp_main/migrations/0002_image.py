# Generated by Django 4.2.7 on 2024-06-23 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_comp_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'db_table': 'photo_comp_main_image',
                'managed': False,
            },
        ),
    ]
