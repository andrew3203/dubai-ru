# Generated by Django 4.0 on 2022-10-19 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resaleproperty',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Название лота'),
        ),
    ]
