# Generated by Django 4.0 on 2022-10-16 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary', '0003_primaryproperty_main_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='Описание'),
        ),
    ]
