# Generated by Django 3.0 on 2020-02-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200202_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='thumbnail',
            field=models.FileField(null=True, upload_to='posts/'),
        ),
    ]
