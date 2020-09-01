# Generated by Django 3.1 on 2020-08-30 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_main_catch_phrases'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('catch_phrase', models.CharField(default='phrase', max_length=256)),
                ('images', models.ImageField(upload_to='front/images/home/slider')),
            ],
        ),
        migrations.RemoveField(
            model_name='main',
            name='catch_phrases',
        ),
    ]