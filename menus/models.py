from django.db import models 
from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable
from wagtail.admin.panels import FieldPanel, PageChooserPanel, InlinePanel

# Create your models here.

class MenuItem(Orderable):
    link_title = models.CharField(blank=True, max_length=50)
    link_url = models.CharField(blank=True, max_length=500)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE, ##destroyed by cascading
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    page = ParentalKey("Menu", related_name="menu_items")

    @property
    def link(self) -> str:
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return "#"

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return "Missing Title"

class Menu(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from="title",
        editable=True,
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        InlinePanel("menu_items", label="Menu Item"),
    ]

    def __str__(self):
        return self.title

    



