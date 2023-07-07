from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models

from wagtail.api import APIField
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.blocks import RichTextBlock
from wagtail.admin.panels import FieldPanel, PageChooserPanel  
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from streams import blocks as stream_blocks
from wagtail.rich_text import RichText

##import dropbox 
from vcsc.settings.base import ALL_RICHTEXT_FEATURES
##DROPBOX_OAUTH2_TOKEN, DROPBOX_APP_KEY, DROPBOX_APP_SECRET, DROPBOX_OAUTH2_REFRESH_TOKEN



NEW_TABLE_OPTIONS = {
    'minSpareRows': 0,
    'startRows': 4,
    'startCols': 4,
    'colHeaders': False,
    'rowHeaders': True,
    'contextMenu': [
        'row_above',
        'row_below',
        '---------',
        'col_left',
        'col_right',
        '---------',
        'remove_row',
        'remove_col',
        '---------',
        'undo',
        'redo'
    ],
    'editor': 'text',
    'stretchH': 'all',
    'renderer': 'text',
    'autoColumnSize': False,
}

class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]
    ##limit to only 1 home page in the entire website:
    max_count = 1
    lead_text = models.CharField(
        max_length = 140, 
        blank = True, 
        help_text = 'Subheading text under banner title',
    )

    ##link to an internal page (CTA button)
    button = models.ForeignKey(
        'wagtailcore.Page',
        blank = True,
        null = True,
        related_name = '+',
        help_text = 'Select an optional page to link to',
        on_delete = models.SET_NULL,
    )

    ##add short text to button
    button_text = models.CharField(
        max_length = 50,
        default = 'Read More',
        blank = False, ##always has to be filled out
        help_text = 'Button text',
    )

    banner_background_image = models.ForeignKey(
        'wagtailimages.Image', ##default image model
        blank = False, ##has to be filled out
        null = True, ##allowed to be empty in db
        related_name = '+',
        help_text = 'Banner background image',
        on_delete = models.SET_NULL,
    )

    body = StreamField([
        ("title", stream_blocks.TitleBlock()),
        ("cards", stream_blocks.CardsBlock()),
        ("cards_text", stream_blocks.CardsTextBlock()),
        ("image_and_text", stream_blocks.ImageAndTextBlock()),
        ("horizontal_card", stream_blocks.ImageBesideTextBlock()),
        ("image_beside_text",stream_blocks.ImageBesideTextBlockNoLink()),
        ("cta", stream_blocks.CallToActionBlock()),
        #("pricing_table", stream_blocks.PricingTableBlock(
        #    table_options=NEW_TABLE_OPTIONS
        #)),
        ("richtext", RichTextBlock(
            template="streams/simple_richtext_block.html",
            features=ALL_RICHTEXT_FEATURES,
        )),
        ("large_image", ImageChooserBlock(
            help_text='This image will be cropped to 1200px by 775px',
            template="streams/large_image_block.html"
        )),
        ("align_content", stream_blocks.AlignedParagraphBlock(
            help_text='Align (left/right/center) text and images',
            template="streams/aligned_paragraph.html"
        )),
    ], null=True, blank=True, use_json_field=True)

    api_fields = [
        APIField("button_text"),
        APIField("banner_background_image"),
        
    ]

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"), ##regular text field
        PageChooserPanel("button"), 
        FieldPanel("button_text"),
        FieldPanel("banner_background_image"),
        FieldPanel("body"),
    ]

    def save(self, *args, **kwargs):

        key = make_template_fragment_key(
            "home_page_streams",
            [self.id],
        )
        cache.delete(key)

        return super().save(*args, **kwargs)