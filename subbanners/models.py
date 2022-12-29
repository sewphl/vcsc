from django.db import models

from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, PageChooserPanel
from wagtail.core import blocks as wagtail_blocks
from wagtail.core.blocks import RichTextBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.fields import RichTextField

from home.models import NEW_TABLE_OPTIONS
from streams import blocks

from vcsc.settings.base import ALL_RICHTEXT_FEATURES

class SubbannerPage(Page):
    template = "subbanners/subbanner_page.html"
    parent_page_types = ["home.HomePage"]

    banner_lead_text = models.CharField(
        max_length = 140, 
        blank = True, 
        help_text = 'Subheading text under banner title',
    )

    lead_text = RichTextField(
        blank=True,
        help_text = 'Short lead text, if needed',
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
        ("title", blocks.TitleBlock()),
        ("cards", blocks.CardsBlock()),
        ("image_and_text", blocks.ImageAndTextBlock()),
        ("image_beside_text", blocks.ImageBesideTextBlock()),
        ("cta", blocks.CallToActionBlock()),
        #("pricing_table", blocks.PricingTableBlock(
        #    table_options=NEW_TABLE_OPTIONS,
        #)),
        ("richtext", wagtail_blocks.RichTextBlock(
            template="streams/simple_richtext_block.html",
            features=ALL_RICHTEXT_FEATURES,
        )),
        ("large_image", ImageChooserBlock(
            help_text='This image will be cropped to 1200px by 775px',
            template="streams/large_image_block.html"
        )),
        ("align_content", blocks.AlignedParagraphBlock(
            help_text='Align (left/right/center) text and images',
            template="streams/aligned_paragraph.html"
        )),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_lead_text"), 
        FieldPanel("lead_text"),
        ImageChooserPanel("banner_background_image"),
        StreamFieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Interior banner page"
        verbose_name_plural = "Interior banner pages"