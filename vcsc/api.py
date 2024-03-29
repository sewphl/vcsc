from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

from .endpoints import (
    PeoplePersonAPIEndpoint, 
    ResearchItemAPIEndpoint, 
    ResearchLabAPIEndpoint, 
)

api_router = WagtailAPIRouter('wagtailapi')  ##url namespace

##register endpoints:
##first parameter is url
##second parameter is what we are importing above. 
api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)
api_router.register_endpoint('people', PeoplePersonAPIEndpoint)
api_router.register_endpoint('research', ResearchItemAPIEndpoint)
api_router.register_endpoint('labs', ResearchLabAPIEndpoint)
