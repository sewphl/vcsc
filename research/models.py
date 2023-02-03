"""Research Item Snippet."""
from django.shortcuts import render
from django.urls import include, path, re_path

from django.db import models
from django import forms            # the default Django widgets live here

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.admin import widgets   # to use Wagtail's special datetime widget
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    PageChooserPanel,
)
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from wagtail.fields import StreamField
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel 
from wagtail.snippets.blocks import SnippetChooserBlock

from people import models as people_models

class ResearchPressListingPage(RoutablePageMixin, Page):
    """Research press listing page"""
    parent_page_types = ["subbanners.SubbannerPage"]
    subpage_types = []
    template = "research/research_listing_page.html"
    max_count = 1

    
    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["research_labs"] = ResearchLab.objects.all()
        context["researchitems"] = ResearchItem.objects.all()
        context["research_type"] = ResearchType.objects.all()
        context["authors"] = people_models.PeoplePerson.objects.all()
        context["press"] = ResearchItem.objects.filter(research_type__in=ResearchType.objects.filter(slug='press'))
        context["cards"] = context["press"]

        #context['a_special_link'] = self.reverse_subpage('latest_posts')

        return context 
    
    class Meta:
        verbose_name = "Research press listing page"
        verbose_name_plural = "Research press listing pages"
    
    #@route(r"^year/(\d+)/$", name="press_by_year")  #/(\d+)
    #def press_by_year(self, request, year=None):  #, month=None
    #    context = self.get_context(request)
    #    # Note: The below template (latest_posts.html) will need to be adjusted

    #    print(year)
    #    print(year)
    #    print(year)
    #    return render(request, "research/latest_posts.html", context)

    @route(r"^lab/(?P<lab_slug>[-\w]*)/$", name="lab_view")
    def lab_view(self, request, lab_slug):
        """Find blog posts based on a category."""
        context = self.get_context(request)

        try:
            category = ResearchLab.objects.get(slug=lab_slug)
        except Exception:
            category = None
        if category is None:
            pass

        #print(category.lab_name)
        context["cards"] = ResearchItem.objects.filter(research_type__in=ResearchType.objects.filter(slug='press'), research_labs__in=[category])
        return render(request, "research/research_listing_page.html", context)
    
    #@route(r'^latest-posts/$', name="latest_posts")
    #def the_subscribe_page(self, request, *args, **kwargs):
    #    context = self.get_context(request, *args, **kwargs)
    #    context['a_special_test'] = "Hello, World."
    #    return render(request, "research/latest_posts.html", context)

class ResearchPublicationsListingPage(RoutablePageMixin, Page):
    """Research publications listing page"""
    parent_page_types = ["subbanners.SubbannerPage"]
    subpage_types = []
    template = "research/research_listing_page.html"
    max_count = 1
    
    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["research_labs"] = ResearchLab.objects.all()
        context["researchitems"] = ResearchItem.objects.all()
        context["research_type"] = ResearchType.objects.all()
        context["authors"] = people_models.PeoplePerson.objects.all()
        context["publications"] = ResearchItem.objects.filter(research_type__in=ResearchType.objects.filter(slug='publications'))
        context["cards"] = context["publications"]
        #context["media"] = ResearchItem.objects.filter(research_type__in=ResearchType.objects.filter(slug='media'))

        #context['a_special_link'] = self.reverse_subpage('latest_posts')

        return context 
    
    class Meta:
        verbose_name = "Research publications listing page"
        verbose_name_plural = "Research publications listing pages"

    #@route(r"^year/(\d+)/$", name="blogs_by_year")  #/(\d+)
    #def publications_by_year(self, request, year=None):  #, month=None
    #    context = self.get_context(request)
    #    # Note: The below template (latest_posts.html) will need to be adjusted

    #    print(year)
    #    print(year)
    #    print(year)
    #    return render(request, "research/latest_posts.html", context)

    @route(r"^lab/(?P<lab_slug>[-\w]*)/$", name="lab_view")
    def lab_view(self, request, lab_slug):
        """Find blog posts based on a category."""
        context = self.get_context(request)

        try:
            category = ResearchLab.objects.get(slug=lab_slug)
        except Exception:
            category = None
        if category is None:
            pass

        #print(category.lab_name)
        context["cards"] = ResearchItem.objects.filter(research_type__in=ResearchType.objects.filter(slug='publications'), research_labs__in=[category])
        return render(request, "research/research_listing_page.html", context)


    #@route(r'^latest-posts/$', name="latest_posts")
    #def the_subscribe_page(self, request, *args, **kwargs):
    #    context = self.get_context(request, *args, **kwargs)
    #    context['a_special_test'] = "Hello, World."
    #    context['publications'] = context['publications']
    #    return render(request, "research/latest_posts.html", context)


class ResearchGroupListingPage(Page):
    """Research Group Listing Page"""
    parent_page_types = ["subbanners.SubbannerPage"]
    #subpage_types = []
    template = "research/research_group_listing_page.html"
    max_count = 1 

    lead_text = RichTextField(
        blank=True,
        help_text = 'Short lead text, if needed',
    )

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["research_labs"] = ResearchLab.objects.all()
        context["researchitems"] = ResearchItem.objects.all()
        context["authors"] = people_models.PeoplePerson.objects.all()

        return context 
    
    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
    ]

    class Meta:
        verbose_name = "Research Group Listing Page"
        verbose_name_plural = "Research Group Listing Pages"
    
#@register_snippet  # uncomment to use a decorator instead of a function
class ResearchItem(Orderable, ClusterableModel):
    """Research item for snippets."""

    url = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    source = models.CharField(max_length=500, blank=True, null=True)
    img = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )

    # using the correct widget for your field type and desired effect
    date_widget = widgets.AdminDateInput(
        attrs = {
            'placeholder': 'yyyy-mm-dd'
        }
    )

    research_labs = ParentalManyToManyField("research.ResearchLab", blank=False)
    authors = ParentalManyToManyField("people.PeoplePerson", blank=True)
    research_type = ParentalManyToManyField("research.ResearchType", blank=True)
    
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("research_type", widget=forms.CheckboxSelectMultiple),
                FieldPanel("source"),
                FieldPanel("url"),
                FieldPanel("title"),
                FieldPanel("date", widget=date_widget),
                FieldPanel("img"),
            ],
            heading="Add research type, source, url, title, date, and image:",
        ),
        MultiFieldPanel(
            [
                #InlinePanel('research_labs', label='labs'),
                #InlinePanel("research_labs", label="Labs", min_num=1, max_num=5),
                #SnippetChooserPanel("research_labs"),
                FieldPanel("research_labs", widget=forms.CheckboxSelectMultiple),
                FieldPanel("authors", widget=forms.CheckboxSelectMultiple),
            ],
            heading="Add lab(s) and author(s):"
        ),
    ]

    def __str__(self):
        """String repr of this class."""
        return f" {self.title}"

    class Meta:  # noqa
        verbose_name = "Research Item"
        verbose_name_plural = "Research Items"


register_snippet(ResearchItem)

class ResearchLab(Orderable, ClusterableModel):
    """Research lab for a snippet"""
    lab_name = models.CharField(max_length=500)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=500,
        help_text="A slug to identify research items by this lab",
    )

    external_website = models.URLField(
        blank=True,
        help_text="Add lab website URL here (unless lab's website is part of this VCSC website, in which case, see the field below."
    )

    internal_page = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        related_name="+",
        help_text="If lab website is a page on the VCSC website, add the link here.",
        on_delete=models.SET_NULL,
    )

    lab_logo = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )

    lab_bio = RichTextField(
        blank=True,
        help_text="Brief lab bio (please limit number of hyperlinks included, as these need to be maintained and tend to go stale)",
       )

    
    group_leads = ParentalManyToManyField("people.PeoplePerson", blank=True)

    panels = [
        FieldPanel("lab_name"),
        FieldPanel("slug"),
        FieldPanel("external_website"),
        PageChooserPanel("internal_page"),
        FieldPanel("lab_bio"),
        FieldPanel("lab_logo"),
        FieldPanel(
            "group_leads", 
            #heading="Select multiple group leads using Command button on Mac", 
            widget=forms.CheckboxSelectMultiple,
            #help_text="Group leads",
        ),

    ]

    def clean(self):
        super().clean()

    class Meta:
        verbose_name = "Research Lab"
        verbose_name_plural = "Research Labs"
        ordering = ["lab_name"]

    def __str__(self):
        return self.lab_name

register_snippet(ResearchLab)

class ResearchType(models.Model):
    """Research type (publications, press, or media item) for a snippet"""
    research_type = models.CharField(max_length=500)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=500,
        help_text="A slug to identify research items by type (publications, press, or media)",
    )

    panels = [
        FieldPanel("research_type"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Research Type"
        verbose_name_plural = "Research Types"
        ordering = ["research_type"]

    def __str__(self):
        return self.research_type

register_snippet(ResearchType)


