# Generated by Django 3.0 on 2020-02-02 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200201_2205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-created_at'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='posts',
            name='thumbnail',
            field=models.FileField(null=True, upload_to='posts/'),
        ),
    ]
