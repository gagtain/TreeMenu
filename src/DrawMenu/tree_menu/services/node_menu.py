from pprint import pprint

from django.db.models import QuerySet

from tree_menu.models import MenuItem


def get_menu_items(menu_name, select_related_obj=('parent', 'menu')) -> QuerySet[MenuItem]:
    return MenuItem.objects.select_related(*select_related_obj).filter(menu__name=menu_name)


def generate_child(menu_item, select_tree):
    ...


def generate_tree_in_menu_items(menu_items: QuerySet[MenuItem], menu_name: str, url: list[str]):
    tree = {
        'name': menu_name,
        'child': []
    }
    cache = {

    }
    for menu_item in menu_items:
        if not menu_item.parent:
            if not f"{menu_item.id}__to" in cache.keys():
                cache[f"{menu_item.id}__to"] = []
            cache[str(menu_item.id)] = {
                'name': menu_item.name,
                'child': cache[f"{menu_item.id}__to"]
            }
            tree['child'].append(cache[str(menu_item.id)])
        else:
            if f"{menu_item.parent.id}__to" in cache.keys():
                cache[f"{menu_item.id}__to"] = []
                cache[f"{menu_item.parent.id}__to"].append({
                    'name': menu_item.name,
                    'child': cache[f"{menu_item.id}__to"]
                }

                )
            else:
                if f"{menu_item.parent.id}__to" in tree.keys():
                    if not f"{menu_item.id}__to" in cache.keys():
                        cache[f"{menu_item.id}__to"] = []
                    cache[f"{menu_item.parent.id}__to"].append({
                        'name': menu_item.name,
                        'child': cache[f"{menu_item.id}__to"]
                    }
                    )
                else:
                    if not f"{menu_item.id}__to" in cache.keys():
                        cache[f"{menu_item.id}__to"] = []
                    cache[f"{menu_item.parent.id}__to"] = []
                    cache[f"{menu_item.parent.id}__to"].append({
                        'name': menu_item.name,
                        'child': cache[f"{menu_item.id}__to"]
                        })


    pprint(tree)

# if str(menu_item.parent.id) in cache.keys():
#     cache[f"{menu_item.id}__to"] = []
#     cache[str(menu_item.parent.id)]['child'].append(
#         {
#             'name': menu_item.parent.name,
#             'child': [{
#                 'name': menu_item.name,
#                 'child': cache[f"{menu_item.id}__to"]
#             }]
#         }
#     )
# else:
#     if f"{menu_item.parent.id}__to" in cache.keys():
#         cache[f"{menu_item.parent.id}__to"].append({
#             'name': menu_item.parent.name,
#             'child': [{
#                 'name': menu_item.name,
#                 'child': []
#             }]
#         })
#     else:
#         print(cache, menu_item.name)
