# Generated by Django 2.1.5 on 2019-01-31 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190131_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image_path',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_name',
            field=models.TextField(max_length=50),
        ),
    ]
