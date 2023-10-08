from app.models import MenuItem
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag("app/menu.html")
def draw_menu(name=None, item=None):
    items = MenuItem.objects.filter(menu__name=name)

    def get_menu(item=None, submenu=None):
        menu = list(
            items.filter(parent=None)
            if item is None
            else items.filter(parent__name=item)
        )
        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        finally:
            try:
                return get_menu(items.get(name=item).parent.name, menu)
            except AttributeError:
                return get_menu(submenu=menu)
            except ObjectDoesNotExist:
                return menu

    if name == item:
        return {"menu": get_menu()}
    return {"menu": get_menu(item)}
