# Generated by Django 4.0.6 on 2022-10-25 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_photo_height_photo_width_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='height',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='photo',
            name='width',
            field=models.IntegerField(editable=False),
        ),
    ]
