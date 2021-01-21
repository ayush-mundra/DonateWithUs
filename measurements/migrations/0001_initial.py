# Generated by Django 2.2.17 on 2021-01-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
