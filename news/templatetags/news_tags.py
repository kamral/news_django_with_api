from django import template
# нужна для неповторения кода использования категории в функциях
from news.models import Category
from django.db.models import Count

register=template.Library()
# обрабатывает категории
@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


# обрабатывает и выводит категории
@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # считает количество новостей в каждой группе, в случае если там нет,
    # то он не выведет групу
    categories=Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {'categories':categories}