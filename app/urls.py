from django.conf.urls import url
#from django.views.decorators.cache import cache_page
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r"^category/(?P<cate_id>\d+)$", views.CategoryView.as_view(), name='category'),
    url(r'^search/$', views.blog_search, name='search'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^tags/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
]