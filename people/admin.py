from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)

from .models import PeoplePerson

@modeladmin_register
class PeopleAdmin(ModelAdmin):
    """People admin."""

    model = PeoplePerson
    menu_label = "People" ##how it will show up in admin 
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "title")
    search_fields = ("name", "title")