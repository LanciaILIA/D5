from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.views import generic
from .filters import PostFilter


def index(request): # Получение данных из БД
    num_post = Post.objects.all().count() # objects.all() - Получить все объекты Book из БД
    num_comment = Comment.objects.all().count()
    num_category = Category.objects.all().count()
    num_authors = Author.objects.count() # count() => SELECT COUNT(*)

    return render(request,'index.html',  # render - Формирует и возвращает ответ (НТМL-страницу index.html)
                    context={'num_post' : num_post,
                            'num_comment' : num_comment,
                             'num_category' : num_category,
                             'num_authors' : num_authors,
                            }
                   )
    # 'num_visits' : num_visits,
    # return HttpResponse("Глaвнaя страница сайта Мир книг!")

class NewsListView(generic.ListView): # D6
    model = Post
    ordering = 'name'
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

    def get_queryset_(self): # сортировка по дате
        queryset = Post.objects.all().order_by('-data')
        return queryset


class NewsDetailView(generic.DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'news_detail.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'news_detail'

