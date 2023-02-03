from django.core.exceptions import ValidationError
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
from wagtail.fields import StreamField
from wagtail.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel 
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from streams import blocks
from research import models as research_models


class PeopleListingPageCore(Page):
    """People listing page: Core Team"""
    parent_page_types = ["subbanners.SubbannerPage"]
    subpage_types = ["people.PeoplePersonPage"]
    template = "people/people_listing_page.html"
    max_count = 1 

    lead_text = RichTextField(
        blank=True,
        help_text = 'Short lead text, if needed',
    )

    def child_pages(self):
        return PeoplePersonPage.objects.live().child_of(self)

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["person_role"] = PeopleRole.objects.all()
        context["people_all"] = PeoplePerson.objects.all()
        #context['person_page'] = PeoplePersonPage.objects.all() 
        context["person"] = PeoplePerson.objects.filter(person_role__in=PeopleRole.objects.filter(slug='core-team'))
        return context 
    
    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
    ]

    class Meta:
        verbose_name = "People listing page: Core Team"
        verbose_name_plural = "People listing pages: Core Team"

class PeopleListingPageExternalFaculty(Page):
    """People listing page: External Faculty"""
    parent_page_types = ["subbanners.SubbannerPage"]
    subpage_types = ["people.PeoplePersonPage"]
    template = "people/people_listing_page.html"
    max_count = 1 

    lead_text = RichTextField(
        blank=True,
        help_text = 'Short lead text, if needed',
    )

    def child_pages(self):
        return PeoplePersonPage.objects.live().child_of(self)

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["person_role"] = PeopleRole.objects.all()
        context["people_all"] = PeoplePerson.objects.all()
        #context['person_page'] = PeoplePersonPage.objects.all() 
        context["person"] = PeoplePerson.objects.filter(person_role__in=PeopleRole.objects.filter(slug='external-faculty'))
        return context 
    
    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
    ]

    class Meta:
        verbose_name = "People listing page: External Faculty"
        verbose_name_plural = "People listing pages: External Faculty"

class PeopleListingPagePostdoc(Page):
    """People listing page: Postdocs"""
    parent_page_types = ["subbanners.SubbannerPage"]
    subpage_types = ["people.PeoplePersonPage"]
    template = "people/people_listing_page.html"
    max_count = 1

    lead_text = RichTextField(
        blank=True,
        help_text = 'Short lead text, if needed',
    )

    def child_pages(self):
        return PeoplePersonPage.objects.live().child_of(self)

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["person_role"] = PeopleRole.objects.all()
        context["people_all"] = PeoplePerson.objects.all()
        #context['person_page'] = PeoplePersonPage.objects.all() 
        context["person"] = PeoplePerson.objects.filter(person_role__in=PeopleRole.objects.filter(slug='postdocs'))
        return context 
    
    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
    ]

    class Meta:
        verbose_name = "People listing page: Postdocs"
        verbose_name_plural = "People listing pages: Postdocs"
    
class PeopleListingPageAlumni(Page):
    """People listing page: Alumni"""
    parent_page_types = ["subbanners.SubbannerPage"]
    subpage_types = ["people.PeoplePersonPageAlumni"]
    template = "people/people_listing_page.html"
    max_count = 1 

    lead_text = RichTextField(
        blank=True,
        help_text = 'Short lead text, if needed',
    )

    def child_pages(self):
        return PeoplePersonPage.objects.live().child_of(self)

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["person_role"] = PeopleRole.objects.all()
        context["people_all"] = PeoplePerson.objects.all()
        #context['person_page'] = PeoplePersonPage.objects.all() 
        context["person"] = PeoplePerson.objects.filter(person_role__in=PeopleRole.objects.filter(slug='alumni'))
        return context 
    
    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
    ]

    class Meta:
        verbose_name = "People listing page: Alumni"
        verbose_name_plural = "People listing pages: Alumni"

class PeopleListingPageStudent(Page):
    """People listing page: Students"""
    parent_page_types = ["subbanners.SubbannerPage"]
    subpage_types = ["people.PeoplePersonPageStudents"]
    template = "people/people_listing_page_students.html"
    max_count = 1

    lead_text = RichTextField(
        blank=True,
        help_text = 'Short lead text, if needed',
    )

    def child_pages(self):
        return PeoplePersonPage.objects.live().child_of(self)

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["person_role"] = PeopleRole.objects.all()
        context["people_all"] = PeoplePerson.objects.all()
        #context['person_page'] = PeoplePersonPage.objects.all() 
        context["person_phd"] = PeoplePerson.objects.filter(person_role__in=PeopleRole.objects.filter(slug='students-phd'))
        context["person_masters"] = PeoplePerson.objects.filter(person_role__in=PeopleRole.objects.filter(slug='students-masters'))
        return context 
    
    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
    ]

    class Meta:
        verbose_name = "People listing page: Students"
        verbose_name_plural = "People listing pages: Students"



class PeoplePersonPage(Page):
    parent_page_types = ["people.PeopleListingPageCore","people.PeopleListingPageExternalFaculty","people.PeopleListingPagePostdoc"]
    ##do not allow child pages:
    subpage_types = []
    template = "people/person_page.html"

    body = StreamField([
            ("add_person", SnippetChooserBlock(
            target_model="people.PeoplePerson",
            template="streams/person_block.html",
        )),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["person_role"] = PeopleRole.objects.all()
        context["person"] = PeoplePerson.objects.all()
        context['person_page'] = PeoplePersonPage.objects.all() 
        ##From Research: 
        context["researchitems"] = research_models.ResearchItem.objects.all()
        context["research_type"] = research_models.ResearchType.objects.all()
        context["research_labs"] = research_models.ResearchLab.objects.all()
        context["press"] = research_models.ResearchItem.objects.filter(research_type__in=research_models.ResearchType.objects.filter(slug='press'), authors__in=PeoplePerson.objects.filter(name=self))
        context["publications"] = research_models.ResearchItem.objects.filter(research_type__in=research_models.ResearchType.objects.filter(slug='publications'), authors__in=PeoplePerson.objects.filter(name=self))
        context["media"] = research_models.ResearchItem.objects.filter(research_type__in=research_models.ResearchType.objects.filter(slug='media'), authors__in=PeoplePerson.objects.filter(name=self))
        
        return context 
    
    class Meta:
        verbose_name = "Person page: Core Team, Postdocs, External Faculty"
        verbose_name_plural = "Person pages: Core Team, Postdocs, External Faculty"

class PeoplePersonPageStudents(Page):
    parent_page_types = ["people.PeopleListingPageStudent"]
    ##do not allow child pages:
    subpage_types = []
    template = "people/person_page.html"
    
    body = StreamField([
            ("add_person", SnippetChooserBlock(
            target_model="people.PeoplePerson",
            template="streams/person_block_student.html",
        )),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["person_role"] = PeopleRole.objects.all()
        context["person"] = PeoplePerson.objects.all()
        context['person_page'] = PeoplePersonPage.objects.all() 
        ##From Research: 
        context["researchitems"] = research_models.ResearchItem.objects.all()
        context["research_type"] = research_models.ResearchType.objects.all()
        context["research_labs"] = research_models.ResearchLab.objects.all()
        context["press"] = research_models.ResearchItem.objects.filter(research_type__in=research_models.ResearchType.objects.filter(slug='press'), authors__in=PeoplePerson.objects.filter(name=self))
        context["publications"] = research_models.ResearchItem.objects.filter(research_type__in=research_models.ResearchType.objects.filter(slug='publications'), authors__in=PeoplePerson.objects.filter(name=self))
        context["media"] = research_models.ResearchItem.objects.filter(research_type__in=research_models.ResearchType.objects.filter(slug='media'), authors__in=PeoplePerson.objects.filter(name=self))
        context["person_phd"] = PeoplePerson.objects.filter(person_role__in=PeopleRole.objects.filter(slug='students-phd'))
        context["person_masters"] = PeoplePerson.objects.filter(person_role__in=PeopleRole.objects.filter(slug='students-masters'))
        
        return context 
    
    class Meta:
        verbose_name = "Person page: Students"
        verbose_name_plural = "Person pages: Students"

class PeoplePersonPageAlumni(Page):
    parent_page_types = ["people.PeopleListingPageAlumni"]
    ##do not allow child pages:
    subpage_types = []
    template = "people/person_page.html"
    
    body = StreamField([
            ("add_person", SnippetChooserBlock(
            target_model="people.PeoplePerson",
            template="streams/person_block_alumni.html",
        )),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["person_role"] = PeopleRole.objects.all()
        context["person"] = PeoplePerson.objects.all()
        context['person_page'] = PeoplePersonPage.objects.all() 
        ##From Research: 
        context["researchitems"] = research_models.ResearchItem.objects.all()
        context["research_type"] = research_models.ResearchType.objects.all()
        context["research_labs"] = research_models.ResearchLab.objects.all()
        context["press"] = research_models.ResearchItem.objects.filter(research_type__in=research_models.ResearchType.objects.filter(slug='press'), authors__in=PeoplePerson.objects.filter(name=self))
        context["publications"] = research_models.ResearchItem.objects.filter(research_type__in=research_models.ResearchType.objects.filter(slug='publications'), authors__in=PeoplePerson.objects.filter(name=self))
        context["media"] = research_models.ResearchItem.objects.filter(research_type__in=research_models.ResearchType.objects.filter(slug='media'), authors__in=PeoplePerson.objects.filter(name=self))
        
        return context 
    
    class Meta:
        verbose_name = "Person page: Alumni"
        verbose_name_plural = "Person pages: Alumni"


#@register_snippet  # uncomment to use a decorator instead of a function
class PeoplePerson(Orderable, ClusterableModel):
    """Person for snippets."""

    #website = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=500, blank=False, null=True, verbose_name="Full name")
    last_name = models.CharField(max_length=300, blank=False, null=True, verbose_name="Last name only")
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=200,
        help_text="Please enter person's name as first-last (all lowercase, using in place of spaces)",
    )
    title = models.CharField(max_length=500, blank=False, null=True)
    bio = RichTextField(
        blank=True,
        help_text="Brief bio (please limit number of hyperlinks included, as these need to be maintained and tend to go stale)",
       )
    thesis_topic = models.CharField(
        blank=True,
        max_length=500,
        help_text="For alumni only: thesis topic",
       )
    current_employer = models.CharField(
        blank=True,
        max_length=200,
        help_text="For alumni only: current employer",
       )
    current_role = models.CharField(
        blank=True,
        max_length=200,
        help_text="For alumni only: current role", 
    )
    person_img = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )
    internal_page = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        related_name="+",
        help_text="Create and then select internal page for this person.",
        on_delete=models.SET_NULL,
    )
    external_website = models.URLField(
        blank=True,
    )
    twitter = models.URLField(
        blank=True,
    )
    youtube = models.URLField(
        blank=True,
    )
    linkedin = models.URLField(
        blank=True,
    )
    instagram = models.URLField(
        blank=True,
    )
    github = models.URLField(
        blank=True,
    )
    gitlab = models.URLField(
        blank=True,
    )
    strava = models.URLField(
        blank=True,
    )
    google_scholar = models.URLField(
        blank=True,
    )
    arxiv = models.URLField(
        blank=True,
    )
    research_gate = models.URLField(
        blank=True,
    )
    orcid = models.URLField(
        blank=True,
    )
    academia = models.URLField(
        blank=True,
    )
    philpapers = models.URLField(
        blank=True,
    )

    person_role = ParentalManyToManyField("people.PeopleRole", blank=False)
    research_type = ParentalManyToManyField("research.ResearchType", blank=True)
    ##Note: Authors is also used for advisor dropdown (listing all people):
    authors = ParentalManyToManyField("people.PeoplePerson", blank=True)
    research_labs = ParentalManyToManyField("research.ResearchLab", blank=True)
    ##many to many (if want to allow for multiple degrees and years)
    #alumni_year = ParentalManyToManyField("people.PeopleGradYearAlumni", blank=True)
    #alumni_degree = ParentalManyToManyField("people.PeopleDegreeAlumni", blank=True)
    ##for now, set as many to one using foreign key:
    alumni_year = models.ForeignKey("people.PeopleGradYearAlumni", null=True, blank=True, on_delete=models.SET_NULL)
    alumni_degree = models.ForeignKey("people.PeopleDegreeAlumni", null=True, blank=True, on_delete=models.SET_NULL)
        
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("person_role", widget=forms.CheckboxSelectMultiple),
                FieldPanel(
                    "research_labs", 
                    heading="For students/alumni: Research Labs(s)",
                    widget=forms.CheckboxSelectMultiple,
                    ),
                FieldPanel(
                    "authors", 
                    heading="For students/alumni: Research advisor(s) (select multiple advisors using Command button on Mac)", 
                    widget=forms.SelectMultiple,
                    #help_text="For students/alumni: Research advisor(s)",
                    ),
            ],
            heading="Person role(s), lab(s), and advisor(s)",
        ),
        MultiFieldPanel(
            [
                FieldPanel(
                    "thesis_topic",
                    heading="For alumni only: Thesis topic",
                ),
                FieldPanel(
                    "current_employer",
                    heading="For alumni only: Current employer",
                ),
                FieldPanel(
                    "current_role",
                    heading="For alumni only: Current role at organization above",
                ),
                FieldPanel("alumni_degree", widget=forms.RadioSelect),
                FieldPanel("alumni_year", widget=forms.RadioSelect),
            ],
            heading="For alumni only: Thesis, employment, and degree info",
        ),
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("last_name"),
                FieldPanel("slug"),
                FieldPanel("title"),
                FieldPanel("bio"),
                FieldPanel("person_img"),
                PageChooserPanel("internal_page"), 
                FieldPanel("external_website"),
                FieldPanel("twitter"),
                FieldPanel("youtube"),
                FieldPanel("linkedin"),
                FieldPanel("instagram"),
                FieldPanel("github"),
                FieldPanel("gitlab"),
                FieldPanel("strava"),
                FieldPanel("google_scholar"),
                FieldPanel("arxiv"),
                FieldPanel("research_gate"),
                FieldPanel("orcid"),
                FieldPanel("academia"),
                FieldPanel("philpapers"),

            ],
            heading="Person",
        ),
    ]

    def clean(self):
        super().clean()

    def __str__(self):
        """String repr of this class."""
        ##return f"Person: {self.name}"
        return f"{self.name}"

    class Meta:  # noqa
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ["last_name"]


register_snippet(PeoplePerson)

class PeopleRole(models.Model):
    """People role for a snippet"""
    role = models.CharField(max_length=500)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=500,
        help_text="A slug to identify people by role",
    )

    panels = [
        FieldPanel("role"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ["role"]

    def __str__(self):
        return self.role

register_snippet(PeopleRole)

class PeopleDegreeAlumni(models.Model):
    """Alumni degree type (Postdoc, PhD, MS, or BS) for a snippet"""
    alumni_degree_type = models.CharField(max_length=100)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=100,
        help_text="A slug to identify alumni degrees (Postdoc, PhD, MS, or BS)",
    )

    panels = [
        FieldPanel("alumni_degree_type"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Alumni Degree Type"
        verbose_name_plural = "Alumni Degree Types"
        ordering = ["alumni_degree_type"]

    def __str__(self):
        return self.alumni_degree_type

register_snippet(PeopleDegreeAlumni)

class PeopleGradYearAlumni(models.Model):
    """Alumni graduation year for a snippet"""
    alumni_graduation_year = models.CharField(max_length=50)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=50,
        help_text="A slug to identify alumni graduation years",
    )

    panels = [
        FieldPanel("alumni_graduation_year"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Alumni Graduation Year"
        verbose_name_plural = "Alumni Graduation Years"
        ordering = ["alumni_graduation_year"]

    def __str__(self):
        return self.alumni_graduation_year

register_snippet(PeopleGradYearAlumni)
