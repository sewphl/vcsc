from django import forms
##from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from wagtail.blocks import (
    RichTextBlock, 
    CharBlock, 
    StructBlock, 
    StructValue, 
    URLBlock, 
    PageChooserBlock, 
    TextBlock, 
    ListBlock, 
    ChoiceBlock,
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.blocks.struct_block import StructBlockValidationError
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from vcsc.settings.base import ALL_RICHTEXT_FEATURES

class TitleBlock(StructBlock):
    text = CharBlock(
        required=True,
        max_length=None,
        help_text="Text to display",
    )

    ##we don't need panels here---it's assumed that we want this to show.

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display on the page"

class LinkValue(StructValue):
    """Additional logic for our links."""

    def url(self) -> str:
        internal_page = self.get("internal_page")
        external_link = self.get("external_link")
        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link
        return ""


class Link(StructBlock):
    link_text = CharBlock(
        max_length=50,
        default='More Details',
    )
    internal_page = PageChooserBlock(
        required=False
    )
    external_link = URLBlock(
        required=False
    )

    class Meta:
        value_class = LinkValue

    def clean(self, value):
        internal_page = value.get("internal_page")
        external_link = value.get("external_link")
        errors = {}
        if internal_page and external_link:
            errors["internal_page"] = ErrorList(["Both of these fields cannot be filled; please select only one option."])
            errors["external_link"] = ErrorList(["Both of these fields cannot be filled; please select only one option."])
        elif not internal_page and not external_link:
            errors["internal_page"] = ErrorList(["Please select an internal page or external URL for one of these options."])
            errors["external_link"] = ErrorList(["Please select an internal page or external URL for one of these options."])

        if errors:
            raise StructBlockValidationError(errors)
            ##raise ValidationError("Validation error in link", params=errors)

        return super().clean(value)

class Card(StructBlock):
    title = CharBlock(
        max_length=100,
        help_text="Bold title text for this card. Max length of 100 characters.",
    )
    text = TextBlock(
        max_length=255,
        help_text="Optional text for this card. Max length is 255 characters.",
        required=False
    )
    image = ImageChooserBlock(
        help_text="Image will be automagically cropped 570px by 370px"
    )
    link = Link(help_text="Enter a link or select a page")

class CardsBlock(StructBlock):

    cards = ListBlock(
        Card()
    )

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"

class CardText(StructBlock):
    title = CharBlock(
        max_length=100,
        help_text="Optional bold title text for this card. Max length of 100 characters.",
        required=False
    )

    #text = TextBlock(
    #    max_length=800,
    #    help_text="Paragraph text for this card. Max length of 800 characters.",
    #    required=True
    #)

    text = RichTextBlock(
        required=True,
        features=ALL_RICHTEXT_FEATURES,
        )
    

class CardsTextBlock(StructBlock):

    cards_text = ListBlock(
        CardText()
    )

    class Meta:
        template = "streams/cards_text_block.html"
        icon = "edit"
        label = "Card with Text Only"

class RadioSelectBlock(ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget = forms.RadioSelect(
            choices=self.field.widget.choices
        )

class ImageAndTextBlock(StructBlock):
    image = ImageChooserBlock(help_text="Image will be automagically cropped to 786px x 552px")
    ##note: originally = ChoiceBlock (dropdown) instead of RadioSelectBlock;
    ##this is still a ChoiceBlock, but field widget is different (radio button)
    image_alignment = RadioSelectBlock(  
        choices=(
            ("left", "Image to the left"),
            ("right", "Image to the right"),
        ),
        default="left",
        help_text="Image on the left with text on the right. Or image on right with text on left." 
    )
    title  = CharBlock(max_length=60, help_text="Max length of 60 characters")
    text = CharBlock(max_length=140, required=False)
    link = Link()

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"

class ImageBesideTextBlock(StructBlock):
    image = ImageChooserBlock(help_text="Image will be automagically cropped to 786px x 552px")
    title  = CharBlock(
        max_length=60, 
        help_text="Max length of 60 characters", 
        required=False
    )
    subtitle  = CharBlock(
        max_length=200, 
        help_text="Max length of 200 characters", 
        required=False
    )
    #text = CharBlock(
    #    max_length=140, 
    #    required=True
    #)
    text = RichTextBlock(
        required=True,
        features=ALL_RICHTEXT_FEATURES,
    )
    link = Link()

    class Meta:
        template = "streams/image_beside_text_block.html"
        icon = "image"
        label = "Horizontal Card w/ Image"


class ImageBesideTextBlockNoLink(StructBlock):
    image = ImageChooserBlock(help_text="Image will be automagically cropped to 786px x 552px")
    title  = CharBlock(
        max_length=60, 
        help_text="Max length of 60 characters", 
        required=False
    )
    subtitle  = CharBlock(
        max_length=200, 
        help_text="Max length of 200 characters", 
        required=False
    )
    #text = CharBlock(
    #    max_length=140, 
    #    required=True
    #)
    text = RichTextBlock(
        required=True,
        features=ALL_RICHTEXT_FEATURES,
    )

    class Meta:
        template = "streams/image_beside_text_block.html"
        icon = "image"
        label = "Image Beside Text"

class CallToActionBlock(StructBlock):
    title = CharBlock(max_length=200, help_text="Max length of 200 characters.")
    link = Link()

    class Meta:
        template = "streams/call_to_action_block.html"
        icon = "plus"
        label = "Call to Action"

class PricingTableBlock(TableBlock):
    """Pricing table block."""

    class Meta:
        #template = "streams/pricing_table_block.html"
        label = "Pricing Table"
        icon = "table"
        help_text = "Your pricing tables should always have 4 columns."

class AlignedParagraphBlock(StructBlock):
    alignment = ChoiceBlock([('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right')])
    paragraph = RichTextBlock(
        required=True,
        features=ALL_RICHTEXT_FEATURES,
    )

    class Meta:
        template = 'streams/aligned_paragraph.html'
        icon = "edit"
        label = "Align Text/Image"
        help_text = "Align (left, right, center) rich text/image content"

