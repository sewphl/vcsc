# Generated by Django 4.1.4 on 2023-01-05 20:39

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0034_remove_peopleperson_alumni_degree_and_more'),
        ('research', '0009_researchlab_lab_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchlab',
            name='group_leads',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='people.peopleperson'),
        ),
    ]
