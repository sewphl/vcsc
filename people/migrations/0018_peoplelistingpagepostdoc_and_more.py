# Generated by Django 4.1.4 on 2022-12-29 19:42

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('people', '0017_alter_peoplelistingpagestudent_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleListingPagePostdoc',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('lead_text', wagtail.fields.RichTextField(blank=True, help_text='Short lead text, if needed')),
            ],
            options={
                'verbose_name': 'People listing page: Postdocs',
                'verbose_name_plural': 'People listing pages: Postdocs',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='peoplelistingpagecore',
            options={'verbose_name': 'People listing page: Core Team', 'verbose_name_plural': 'People listing pages: Core Team'},
        ),
        migrations.AlterModelOptions(
            name='peoplelistingpagestudent',
            options={'verbose_name': 'People listing page: Students', 'verbose_name_plural': 'People listing pages: Students'},
        ),
        migrations.AlterModelOptions(
            name='peoplepersonpage',
            options={'verbose_name': 'Person page: Core Team', 'verbose_name_plural': 'Person pages: Core Team'},
        ),
        migrations.AlterModelOptions(
            name='peoplepersonpagestudents',
            options={'verbose_name': 'Person page: Students', 'verbose_name_plural': 'Person pages: Students'},
        ),
    ]
