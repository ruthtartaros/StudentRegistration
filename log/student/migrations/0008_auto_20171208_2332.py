# Generated by Django 2.0 on 2017-12-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20171208_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='Dep_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
