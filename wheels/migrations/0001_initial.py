# Generated by Django 4.0.3 on 2022-04-14 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discs',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=50)),
                ('width', models.PositiveIntegerField(max_length=3)),
                ('diametr', models.PositiveIntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Rubber',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=250)),
                ('season', models.CharField(max_length=20)),
                ('width', models.PositiveIntegerField(max_length=3)),
                ('profile', models.PositiveIntegerField(max_length=2)),
                ('diametr', models.PositiveIntegerField(max_length=2)),
                ('load_index', models.PositiveIntegerField(max_length=3)),
                ('speed_index', models.CharField(max_length=1)),
            ],
        ),
    ]
