# Generated by Django 3.2.23 on 2024-02-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_auto_20240203_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='title',
            field=models.CharField(default='Mudanças', editable=False, max_length=255, verbose_name='Título'),
        ),
    ]