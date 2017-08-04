from django import template
from django.db.models.aggregates import Count

from ..models import Article, Category, Tag

register = template.Library()

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)

@register.simple_tag
def archives():
    return Article.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_recent_posts(num=5):
    return Article.objects.all()[:num]

@register.simple_tag
def get_popular_posts(num=5):
	return Article.objects.all().order_by('-views')[:num]
    #return Article.objects.filter(views=1).order_by('-views')[:num]

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)