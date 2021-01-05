from django import template
# нужна для неповторения кода использования категории в функциях
from news.models import Category


register=template.Library()
# обрабатывает категории
@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


# обрабатывает и выводит категории
@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories=Category.objects.all()
    return {'categories':categories}