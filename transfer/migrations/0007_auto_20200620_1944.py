# Generated by Django 3.0.4 on 2020-06-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0006_auto_20200620_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfercar',
            name='arrive',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='transfercar',
            name='take_off',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
