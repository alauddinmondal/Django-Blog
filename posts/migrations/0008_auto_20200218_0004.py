# Generated by Django 3.0 on 2020-02-17 20:04

from django.db import migrations, models
import posts.models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=1),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=tinymce.models.HTMLField(validators=[posts.models.min_length_check]),
        ),
    ]