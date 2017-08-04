from django.shortcuts import render
from django.contrib import messages
from .models import Article, Category, Tag, Contact
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ContactForm
from django.utils import dateformat
import re


# Create your views here.


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        return article_list

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all().order_by('name')
        context['tag_list'] = Tag.objects.all().order_by('name')
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = "article"

    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.views += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(ArticleDetailView, self).get_context_data(**kwargs)


class CategoryView(ListView):
    template_name = 'blog/index.html'
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['cate_id'], status='p')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        name = get_object_or_404(Category, pk=self.kwargs['cate_id'])
        kwargs['cate_name'] = name

        return super(CategoryView, self).get_context_data(**kwargs)



def blog_search(request,):
    query = request.GET.get("search_for")
    if query:
        article_list = Article.objects.filter(
                Q(title__icontains=query)|
                Q(body__icontains=query)
                ).distinct()
    return render(request, 'blog/search.html', {'article_list': article_list,
                                                    })

class TagView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(tags=self.kwargs['tag_id'], status='p')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['category_list'] = Category.objects.all().order_by('name')
        name = get_object_or_404(Tag, pk=self.kwargs['tag_id'])
        kwargs['tag_name'] = name
        return super(TagView, self).get_context_data(**kwargs)


def archives(request, year, month):
    article_list = Article.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    )
    return render(request, 'blog/index.html', context={'article_list': article_list})


class ArchivesView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        year = self.kwargs.get('year')        
        month = self.kwargs.get('month')
        
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month
                                                               )



def contact(request):
        #article_list = Article.objects.filter(tags=request.kwargs['tag_id'], status='p')
        article_list = Article.objects.filter(status='p')
        if request.method == "POST":
            form_class = ContactForm(request.POST)
            if form_class.is_valid():
                post = form_class.save(commit=False)
                post.save()
                messages.success(request, "<h2>Ваше сообщение отправленно!</h2>", extra_tags='html_safe')
                return redirect('app:index')
        else:
            form_class = ContactForm()

        return render(request, 'blog/contact.html', {
            'form': form_class,
            'article_list':article_list,
        })

def about(request,):
    return render(request, 'blog/about.html')