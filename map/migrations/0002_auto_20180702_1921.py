# Generated by Django 2.0.6 on 2018-07-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseaseinstance',
            name='value',
            field=models.IntegerField(null=True),
        ),
    ]
