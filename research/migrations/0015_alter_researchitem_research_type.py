# Generated by Django 4.1.4 on 2023-02-15 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0014_alter_researchitem_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchitem',
            name='research_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='research.researchtype'),
        ),
    ]
