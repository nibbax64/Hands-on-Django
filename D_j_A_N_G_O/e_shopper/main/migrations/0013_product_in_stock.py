# Generated by Django 3.1 on 2020-08-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200830_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.DecimalField(decimal_places=0, default='1', max_digits=10),
        ),
    ]