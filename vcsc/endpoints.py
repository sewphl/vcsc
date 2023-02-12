from wagtail.api.v2.views import BaseAPIViewSet
from people.models import PeoplePerson

class PeoplePersonAPIEndpoint(BaseAPIViewSet):

    model = PeoplePerson

    body_fields = BaseAPIViewSet.body_fields + [
        'name',
        'last_name',
        'title',
        'bio',
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields = [
        'name',
        'last_name',
        'title',
        'bio',
    ]
