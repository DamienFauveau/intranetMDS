# Generated by Django 2.2.7 on 2019-11-26 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0004_call_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='note',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
