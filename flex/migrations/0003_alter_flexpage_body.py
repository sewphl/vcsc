# Generated by Django 4.1.4 on 2022-12-26 13:42

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_alter_flexpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Text to display', max_length=None, required=True))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
