# Generated by Django 3.2.5 on 2021-07-28 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load_images', '0006_alter_imagedetail_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagedetail',
            old_name='image',
            new_name='image_url',
        ),
    ]
