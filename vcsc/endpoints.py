from wagtail.api.v2.views import BaseAPIViewSet
from people.models import PeoplePerson
from research.models import ResearchItem, ResearchLab

class PeoplePersonAPIEndpoint(BaseAPIViewSet):

    model = PeoplePerson

    body_fields = BaseAPIViewSet.body_fields + [
        'name',
        'last_name',
        'title',
        'bio',
        'internal_page',
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields = [
        'name',
        'last_name',
        'title',
        'bio',
        'internal_page',
    ]

class ResearchItemAPIEndpoint(BaseAPIViewSet):

    model = ResearchItem 

    body_fields = BaseAPIViewSet.body_fields + [
        'url',
        'title',
        'date',
        'source',
        'research_labs',
        #'authors',
        'research_type',
    ]  

    listing_default_fields = BaseAPIViewSet.listing_default_fields = [
        'url',
        'title',
        'date',
        'source',
        'research_labs',
        #'authors',
        'research_type',
    ]  

class ResearchLabAPIEndpoint(BaseAPIViewSet):

    model = ResearchLab

    body_fields = BaseAPIViewSet.body_fields + [
        'lab_name',
        'external_website',
        'internal_page',
        'lab_logo',
        'group_leads',
    ]  

    listing_default_fields = BaseAPIViewSet.listing_default_fields = [
        'lab_name',
        'external_website',
        'internal_page',
        'lab_logo',
        'group_leads',
    ]  