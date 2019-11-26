# Generated by Django 2.2.7 on 2019-11-26 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0002_call_call_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('url', models.CharField(max_length=4096, verbose_name='URL')),
                ('available', models.BooleanField(default=False, verbose_name='Disponible')),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
    ]
