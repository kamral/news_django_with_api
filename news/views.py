from django.shortcuts import render,get_object_or_404
from .models import News,Category
# Create your views here.


def index(request):
    news=News.objects.all()
    # мы используем файл из templatetags для
    # того чтобы убрать повторения заимствования категории
    # categories=Category.objects.all()
    context={
        'news':news,
        # 'categories':categories
    }
    return render(request,'news/index.html',context=context)

def get_category(request,category_id):
    news=News.objects.filter(category_id=category_id)
    # мы используем файл из templatetags для
    # того чтобы убрать повторения заимствования категории
    # categories=Category.objects.all()
    category=Category.objects.get(pk=category_id)
    return render(request,'news/news_category.html',{
        'news':news,
        # 'categories':categories,
        'category':category})



def view_news(request,news_id):
    # news_item=News.objects.get(pk=news_id)
    news_item=get_object_or_404(News,pk=news_id)
    return render(request,'news/view_news.html',{
        'news_item':news_item
    })
