# Generated by Django 4.1.9 on 2023-07-07 18:42

from django.db import migrations
import wagtail.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0037_rename_mastadon_peopleperson_mastodon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="peoplepersonpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "add_person",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            target_model="people.PeoplePerson",
                            template="streams/person_block.html",
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="peoplepersonpagealumni",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "add_person",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            target_model="people.PeoplePerson",
                            template="streams/person_block_alumni.html",
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="peoplepersonpagestudents",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "add_person",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            target_model="people.PeoplePerson",
                            template="streams/person_block_student.html",
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
