# Generated by Django 2.0.8 on 2018-09-13 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_auto_20180913_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.TextField(max_length=50, verbose_name=0),
        ),
    ]
