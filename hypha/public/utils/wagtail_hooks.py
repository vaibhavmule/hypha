from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import escape

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from wagtail.core import hooks
from wagtail.core.rich_text import LinkHandler
from wagtailcache.cache import clear_cache

from hypha.public.news.models import NewsType
from hypha.public.people.models import PersonType


class NewsTypeModelAdmin(ModelAdmin):
    model = NewsType
    menu_icon = 'tag'


class PersonTypeModelAdmin(ModelAdmin):
    model = PersonType
    menu_icon = 'tag'


class TaxonomiesModelAdminGroup(ModelAdminGroup):
    menu_label = "Taxonomies"
    items = (NewsTypeModelAdmin, PersonTypeModelAdmin)
    menu_icon = 'tag'


modeladmin_register(TaxonomiesModelAdminGroup)


@hooks.register('insert_editor_css')
def editor_css():
    link = '<link rel="stylesheet" href="{}">\n'
    path = static('css/apply/wagtail_editor.css')
    return link.format(path)


@hooks.register('after_create_page')
@hooks.register('after_edit_page')
def clear_wagtailcache(request, page):
    if page.live:
        clear_cache()


class NewWindowExternalLinkHandler(LinkHandler):
    # This specifies to do this override for external links only.
    # Other identifiers are available for other types of links.
    identifier = 'external'

    @classmethod
    def expand_db_attributes(cls, attrs):
        href = attrs["href"]
        # Let's add the target attr, and also rel="noopener" + noreferrer fallback.
        # See https://github.com/whatwg/html/issues/4078.
        return '<a href="%s" target="_blank" rel="noopener noreferrer">' % escape(href)


@hooks.register('register_rich_text_features')
def register_external_link(features):
    features.register_link_type(NewWindowExternalLinkHandler)
