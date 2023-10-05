from django.db.models import QuerySet

from tree_menu.models import MenuItem


def get_menu_items(menu_name, select_related_obj=('parent', 'menu')) -> QuerySet[MenuItem]:
    return MenuItem.objects.select_related(*select_related_obj).filter(menu__name=menu_name)


def generate_tree_in_menu_items(menu_items: list[MenuItem], menu_name: str):
    tree = {
        'name': menu_name,
        'child': []
    }

    cache = {
        # содержит ключи parent со списком, куда необходимо добавлять элементы child
    }
    for menu_item in menu_items:
        if not menu_item.parent:
            """ Если у объекта нет отца, то это значит, что он является корневым """
            if not f"{menu_item.id}__to" in cache.keys():
                cache[f"{menu_item.id}__to"] = []
            tree['child'].append({
                'name': menu_item.name,
                'child': cache[f"{menu_item.id}__to"]
            })
        else:
            if f"{menu_item.parent.id}__to" in cache.keys():
                """ если ключ parent уже есть в списке """
                cache[f"{menu_item.id}__to"] = []
                cache[f"{menu_item.parent.id}__to"].append({
                    'name': menu_item.name,
                    'child': cache[f"{menu_item.id}__to"]
                }

                )
            else:
                """ если ключа parent нету в списке """
                if not f"{menu_item.id}__to" in cache.keys():
                    cache[f"{menu_item.id}__to"] = []
                cache[f"{menu_item.parent.id}__to"] = []
                cache[f"{menu_item.parent.id}__to"].append({
                    'name': menu_item.name,
                    'child': cache[f"{menu_item.id}__to"]
                })
    return tree
