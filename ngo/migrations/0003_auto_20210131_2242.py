# Generated by Django 2.2.17 on 2021-01-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0002_auto_20210120_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Username', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Ngo',
        ),
    ]
