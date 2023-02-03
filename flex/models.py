##from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock

from home.models import NEW_TABLE_OPTIONS
from streams import blocks as stream_blocks

from vcsc.settings.base import ALL_RICHTEXT_FEATURES



class FlexPage(Page):
    parent_page_types = ["home.HomePage", "flex.FlexPage","subbanners.SubbannerPage"]
    body = StreamField([
        ("title", stream_blocks.TitleBlock()),
        ("cards", stream_blocks.CardsBlock()),
        ("cards_text", stream_blocks.CardsTextBlock()),
        ("image_and_text", stream_blocks.ImageAndTextBlock()),
        ("horizontal_card", stream_blocks.ImageBesideTextBlock()),
        ("image_beside_text",stream_blocks.ImageBesideTextBlockNoLink()),
        ("cta", stream_blocks.CallToActionBlock()),
        #("pricing_table", stream_blocks.PricingTableBlock(
        #    table_options=NEW_TABLE_OPTIONS,
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
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Flex (misc) page"
        verbose_name_plural = "Flex (misc) pages"