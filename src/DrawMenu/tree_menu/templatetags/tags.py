from django import template
from django.template.context import RequestContext

from tree_menu.services.node_menu import get_menu_items, generate_tree_in_menu_items

register = template.Library()


@register.inclusion_tag('tree_menu/tags/menu.html', takes_context=True)
def draw_menu(context: RequestContext, menu_name):
    path = list(filter(None, context.request.path.split('/')))
    menu_items = get_menu_items(menu_name)
    new_context = {

    }
    generate_tree_in_menu_items(menu_items, menu_name, path)
    if not len(path) or len(path) == 1:
        return new_context

    return new_context
