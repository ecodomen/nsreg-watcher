# Generated by Django 4.1.7 on 2023-07-24 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regcomp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=False, max_length=255, null=False, unique=True)),
                ('note1', models.TextField(blank=False, null=False)),
                ('note2', models.TextField(blank=False, null=False)),
                ('city', models.CharField(blank=False, max_length=255, null=False)),
                ('website', models.TextField(blank=False, null=False)),
                ('pricereg', models.FloatField(blank=True, null=True)),
                ('priceprolong', models.FloatField(blank=True, null=True)),
                ('pricechange', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'regcomp',
                'managed': True,
            },
        ),
    ]