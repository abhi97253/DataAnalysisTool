# Generated by Django 3.2 on 2022-07-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='monthly_Inc',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='data',
            name='monthly_exp',
            field=models.FloatField(default=0),
        ),
    ]
