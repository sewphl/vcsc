# Generated by Django 4.1.4 on 2023-01-01 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0004_researchlab_lab_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchlab',
            name='lab_url',
        ),
    ]
