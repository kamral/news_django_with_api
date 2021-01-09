from django.shortcuts import render, get_object_or_404, redirect
from .models import News,Category
# Create your views here.
from .forms import NewsForm
from django.shortcuts import render, get_object_or_404  # render page, return data or 404 page
from .models import News
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse_lazy



# def index(request):
#     news=News.objects.filter(is_published='True')
#     # мы используем файл из templatetags для
#     # того чтобы убрать повторения заимствования категории
#     # categories=Category.objects.all()
#     context={
#         'news':news,
#         # 'categories':categories
#     }
#     return render(request,'news/index.html',context=context)


class HomeNewsView(ListView):
    model=News
    template_name = 'news/for_class/news_list.html'

    # отображаем только те, которые опубликованны
    def get_queryset(self):
        return News.objects.filter(is_published='True')


#
#
# def get_category(request,category_id):
#     news=News.objects.filter(category_id=category_id)
#     # мы используем файл из templatetags для
#     # того чтобы убрать повторения заимствования категории
#     # categories=Category.objects.all()
#     category=Category.objects.get(pk=category_id)
#     return render(request,'news/news_category.html',{
#         'news':news,
#         # 'categories':categories,
#         'category':category})



class NewsByCategory(ListView):
    model=News
    template_name ='news/for_class/news_category.html'
    # чтобы показывал 404 когда нет статьи
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['pk'])





# def view_news(request,news_id):
#     # news_item=News.objects.get(pk=news_id)
#     news_item=get_object_or_404(News,pk=news_id)
#     return render(request,'news/view_news.html',{
#         'news_item':news_item
#     })
#

class ViewDetail(DetailView):
    model = News
    template_name = 'news/for_class/news_detail.html'



# # для создания  формы
# def add_news(request):
#     if request.method == 'POST':
#         # отправляем форму с заполнеными полями
#         form=NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             # если форма прошла валидацию, то создаем словарь
#             # cleaned_data. в cleaneda_data попадают очишенные данные
#             # которые прошли после валиадации. Из нее можно сохранить данные
#             # news=News.objects.create(**form.cleaned_data)
#             news=form.save()
#             return redirect(news)
#
#     else:
#         form=NewsForm()
#     return render(request,'news/add_news.html',{'form':form})


class CreateViews(CreateView):
    form_class=NewsForm
    template_name = 'news/for_class/add_news.html'
    success_url = reverse_lazy('home')

