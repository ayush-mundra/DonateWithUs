# Generated by Django 2.2.17 on 2021-01-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donator', '0003_auto_20210117_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
        migrations.AlterField(
            model_name='product',
            name='Id',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
