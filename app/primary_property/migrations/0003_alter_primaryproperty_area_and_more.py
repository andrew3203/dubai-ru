# Generated by Django 4.0 on 2022-09-04 13:38

from django.db import migrations, models
import django.db.models.deletion
import property.models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
        ('primary_property', '0002_alter_primaryproperty_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryproperty',
            name='area',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.area', verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='primaryproperty',
            name='images',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='property.Image', verbose_name='Фотографии лота'),
        ),
        migrations.AlterField(
            model_name='primaryproperty',
            name='presentation',
            field=models.FileField(blank=True, default=None, null=True, upload_to=property.models.complex_dir_path, verbose_name='Презентация лота'),
        ),
        migrations.AlterField(
            model_name='primaryproperty',
            name='second_image',
            field=models.ImageField(blank=True, default=None, help_text='Первая фото в фотографиях комплекса', null=True, upload_to=property.models.complex_dir_path, verbose_name='Доп. фото'),
        ),
        migrations.AlterField(
            model_name='primaryproperty',
            name='title_image',
            field=models.ImageField(help_text='Фотография на странице лота', upload_to=property.models.complex_dir_path, verbose_name='Обложка'),
        ),
    ]
