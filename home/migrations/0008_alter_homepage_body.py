# Generated by Django 4.1.4 on 2023-01-31 13:30

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Text to display', max_length=None, required=True))])), ('cards', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Bold title text for this card. Max length of 100 characters.', max_length=100)), ('text', wagtail.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automagically cropped 570px by 370px')), ('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('internal_page', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False))], help_text='Enter a link or select a page'))])))])), ('cards_text', wagtail.blocks.StructBlock([('cards_text', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Optional bold title text for this card. Max length of 100 characters.', max_length=100, required=False)), ('text', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'bold', 'italic', 'image', 'embed', 'link', 'document-link', 'hr', 'code', 'superscript', 'subscript', 'strikethrough', 'blockquote'], required=True))])))])), ('image_and_text', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automagically cropped to 786px x 552px')), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Image to the left'), ('right', 'Image to the right')], help_text='Image on the left with text on the right. Or image on right with text on left.')), ('title', wagtail.blocks.CharBlock(help_text='Max length of 60 characters', max_length=60)), ('text', wagtail.blocks.CharBlock(max_length=140, required=False)), ('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('internal_page', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False))]))])), ('horizontal_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automagically cropped to 786px x 552px')), ('title', wagtail.blocks.CharBlock(help_text='Max length of 60 characters', max_length=60, required=False)), ('subtitle', wagtail.blocks.CharBlock(help_text='Max length of 200 characters', max_length=200, required=False)), ('text', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'bold', 'italic', 'image', 'embed', 'link', 'document-link', 'hr', 'code', 'superscript', 'subscript', 'strikethrough', 'blockquote'], required=True)), ('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('internal_page', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False))]))])), ('image_beside_text', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automagically cropped to 786px x 552px')), ('title', wagtail.blocks.CharBlock(help_text='Max length of 60 characters', max_length=60, required=False)), ('subtitle', wagtail.blocks.CharBlock(help_text='Max length of 200 characters', max_length=200, required=False)), ('text', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'bold', 'italic', 'image', 'embed', 'link', 'document-link', 'hr', 'code', 'superscript', 'subscript', 'strikethrough', 'blockquote'], required=True))])), ('cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Max length of 200 characters.', max_length=200)), ('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('internal_page', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False))]))])), ('richtext', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'bold', 'italic', 'image', 'embed', 'link', 'document-link', 'hr', 'code', 'superscript', 'subscript', 'strikethrough', 'blockquote'], template='streams/simple_richtext_block.html')), ('large_image', wagtail.images.blocks.ImageChooserBlock(help_text='This image will be cropped to 1200px by 775px', template='streams/large_image_block.html')), ('align_content', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right')])), ('paragraph', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'bold', 'italic', 'image', 'embed', 'link', 'document-link', 'hr', 'code', 'superscript', 'subscript', 'strikethrough', 'blockquote'], required=True))], help_text='Align (left/right/center) text and images', template='streams/aligned_paragraph.html'))], blank=True, null=True, use_json_field=None),
        ),
    ]
