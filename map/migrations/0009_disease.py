# Generated by Django 2.0.6 on 2018-08-09 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_delete_disease'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gho', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('region', models.CharField(max_length=5, null=True)),
                ('country', models.CharField(max_length=5, null=True)),
                ('display', models.CharField(max_length=50, null=True)),
                ('numeric', models.IntegerField(null=True)),
                ('low', models.IntegerField(null=True)),
                ('high', models.IntegerField(null=True)),
            ],
        ),
    ]