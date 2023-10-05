from django import template
from django.template.context import RequestContext

from tree_menu.services.node_menu import get_menu_items, generate_tree_in_menu_items

register = template.Library()


@register.inclusion_tag('tree_menu/tags/menu.html', takes_context=True)
def draw_menu(context: RequestContext, menu_name):
    path = list(filter(None, context.request.path.split('/')))
    menu_items = list(get_menu_items(menu_name))
    if not len(menu_items):
        return {
            'error': f"Menu {menu_name}, Does Not Exist"
        }
    tree = generate_tree_in_menu_items(menu_items, menu_name)

    return {
        'tree': tree,
        'url': path,
        'error': False
    }


@register.simple_tag(takes_context=True)
def name_is_url(context: dict, name: str, count: int):
    """
    Проверяет, входит ли элемент в url
    """
    try:
        if context['url'][count] == name:
            return True
        else:
            return False
    except IndexError:
        return False
