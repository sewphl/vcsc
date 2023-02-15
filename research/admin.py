from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)

from .models import ResearchItem

@modeladmin_register
class ResearchAdmin(ModelAdmin):
    """Research admin."""

    model = ResearchItem
    menu_label = "Research" ##how it will show up in admin 
    menu_icon = "placeholder"
    menu_order = 289
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title","research_type","date","source")
    search_fields = ("title","research_type","date","source")