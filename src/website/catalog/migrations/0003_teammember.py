# Generated by Django 4.1.7 on 2024-01-21 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_price_options_alter_registrator_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('title', models.CharField(max_length=255, verbose_name='Роль')),
                ('contact', models.CharField(blank=True, max_length=255, null=True, verbose_name='https://github.com/')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='src/website/website/static/pictures/', verbose_name='Фото')),
                ('sex', models.CharField(choices=[('M', 'М'), ('F', 'Ж')], max_length=1, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
    ]
