# Generated by Django 3.1.4 on 2020-12-07 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20201207_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.modelo'),
        ),
    ]
