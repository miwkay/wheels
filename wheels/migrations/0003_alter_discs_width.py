# Generated by Django 4.0.3 on 2022-04-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheels', '0002_alter_discs_id_alter_rubber_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discs',
            name='width',
            field=models.FloatField(max_length=4),
        ),
    ]
