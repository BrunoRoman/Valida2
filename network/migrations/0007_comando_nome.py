# Generated by Django 3.1.4 on 2020-12-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20201208_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='comando',
            name='nome',
            field=models.CharField(default='comando', max_length=100),
        ),
    ]
