# Generated by Django 4.1.4 on 2023-01-25 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0034_remove_peopleperson_alumni_degree_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='peoplepersonpage',
            options={'verbose_name': 'Person page: Core Team, Postdocs, External Faculty', 'verbose_name_plural': 'Person pages: Core Team, Postdocs, External Faculty'},
        ),
    ]
