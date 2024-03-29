# Generated by Django 4.1.4 on 2022-12-27 18:51

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('research', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleListingPageCore',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'People listing page: Core Team',
                'verbose_name_plural': 'People listing pages: Core Team',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='peopleperson',
            name='research_type',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='research.researchtype'),
        ),
    ]
