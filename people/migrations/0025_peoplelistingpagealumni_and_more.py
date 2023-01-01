# Generated by Django 4.1.4 on 2022-12-30 16:49

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('people', '0024_alter_peoplelistingpagecore_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleListingPageAlumni',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('lead_text', wagtail.fields.RichTextField(blank=True, help_text='Short lead text, if needed')),
            ],
            options={
                'verbose_name': 'People listing page: Alumni',
                'verbose_name_plural': 'People listing pages: Alumni',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='peoplelistingpagecore',
            options={'verbose_name': 'People listing page: Core Team', 'verbose_name_plural': 'People listing pages: Core Team'},
        ),
    ]