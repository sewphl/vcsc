# Generated by Django 4.1.4 on 2023-01-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_remove_researchlab_lab_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchlab',
            name='lab_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
