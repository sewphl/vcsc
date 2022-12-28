# Generated by Django 4.1.4 on 2022-12-28 20:00

from django.db import migrations
import wagtail.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_alter_peoplepersonpagestudents_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplepersonpagestudents',
            name='body',
            field=wagtail.fields.StreamField([('add_person', wagtail.snippets.blocks.SnippetChooserBlock(target_model='people.PeoplePerson', template='streams/person_block_student.html'))], blank=True, null=True, use_json_field=None),
        ),
    ]
