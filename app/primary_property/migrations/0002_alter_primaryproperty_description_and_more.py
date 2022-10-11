# Generated by Django 4.0 on 2022-09-04 12:30

from django.db import migrations, models
import property.models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
        ('primary_property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryproperty',
            name='description',
            field=models.TextField(help_text='Можно использовать html, до 1500 символов', max_length=1500, verbose_name='Полное описание лота'),
        ),
        migrations.AlterField(
            model_name='primaryproperty',
            name='images',
            field=models.ManyToManyField(to='property.Image', verbose_name='Фотографии лота'),
        ),
        migrations.AlterField(
            model_name='primaryproperty',
            name='logo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=property.models.complex_dir_path, verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='primaryproperty',
            name='max_square',
            field=models.IntegerField(default=500, verbose_name='Максимальная площядь'),
        ),
        migrations.AlterField(
            model_name='primaryproperty',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Название лота'),
        ),
        migrations.AlterField(
            model_name='primaryproperty',
            name='presentation',
            field=models.FileField(upload_to=property.models.complex_dir_path, verbose_name='Презентация лота'),
        ),
        migrations.AlterField(
            model_name='primaryproperty',
            name='second_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=property.models.complex_dir_path, verbose_name='Доп. фото'),
        ),
        migrations.AlterField(
            model_name='primaryproperty',
            name='short_phrase',
            field=models.TextField(help_text='Яркая и короткая фраза, отображается на странице лота', max_length=250, verbose_name='Короткая фраза'),
        ),
        migrations.AlterField(
            model_name='primaryproperty',
            name='title_image',
            field=models.ImageField(upload_to=property.models.complex_dir_path, verbose_name='Обложка'),
        ),
    ]
