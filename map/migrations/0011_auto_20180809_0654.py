# Generated by Django 2.0.6 on 2018-08-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_remove_disease_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='region',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
