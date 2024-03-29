# Generated by Django 4.1.4 on 2022-12-26 13:44

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0004_alter_flexpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Text to display', max_length=None, required=True))])), ('cards', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Bold title text for this card. Max length of 100 characters.', max_length=100)), ('text', wagtail.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automagically cropped 570px by 370px')), ('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('internal_page', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False))], help_text='Enter a link or select a page'))])))])), ('image_and_text', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automagically cropped to 786px x 552px')), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Image to the left'), ('right', 'Image to the right')], help_text='Image on the left with text on the right. Or image on right with text on left.')), ('title', wagtail.blocks.CharBlock(help_text='Max length of 60 characters', max_length=60)), ('text', wagtail.blocks.CharBlock(max_length=140, required=False)), ('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('internal_page', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False))]))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
