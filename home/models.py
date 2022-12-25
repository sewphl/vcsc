from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models

from wagtail.models import Page
from wagtail.core import blocks as wagtail_blocks
from wagtail.core.fields import StreamField
from wagtail.core.blocks import RichTextBlock
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
#from streams import blocks
from wagtail.rich_text import RichText

from vcsc.settings.base import ALL_RICHTEXT_FEATURES


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

    #body = StreamField([
        #("title", blocks.TitleBlock()),
        #("cards", blocks.CardsBlock()),
        #("cards_text", blocks.CardsTextBlock()),
        #("image_and_text", blocks.ImageAndTextBlock()),
        #("image_beside_text", blocks.ImageBesideTextBlock()),
        #("cta", blocks.CallToActionBlock()),
        #("pricing_table", blocks.PricingTableBlock(
        #    table_options=NEW_TABLE_OPTIONS
        #)),
        #("richtext", wagtail_blocks.RichTextBlock(
        #    template="streams/simple_richtext_block.html",
        #    features=ALL_RICHTEXT_FEATURES,
        #)),
        #("large_image", ImageChooserBlock(
        #    help_text='This image will be cropped to 1200px by 775px',
        #    template="streams/large_image_block.html"
        #)),
        #("align_content", blocks.AlignedParagraphBlock(
        #    help_text='Align (left/right/center) text and images',
        #    template="streams/aligned_paragraph.html"
        #)),
    #], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"), ##regular text field
        PageChooserPanel("button"), 
        FieldPanel("button_text"),
        ImageChooserPanel("banner_background_image"),
        #StreamFieldPanel("body"),
    ]

    def save(self, *args, **kwargs):

        key = make_template_fragment_key(
            "home_page_streams",
            [self.id],
        )
        cache.delete(key)

        return super().save(*args, **kwargs)