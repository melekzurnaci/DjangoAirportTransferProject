# Generated by Django 3.0.4 on 2020-06-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0005_auto_20200619_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfercar',
            name='arrive',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='transfercar',
            name='take_off',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
