from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from redactor.fields import RedactorField

# Create your models here.

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Черновик'),
        ('p', 'Опубликовано'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField('Название', max_length=100)
    description = models.CharField('Описание статьи',max_length=300)
    body = RedactorField(
                    verbose_name=u'Text',
                    redactor_options={'lang': 'ru','focus': True, 'plugins': ['video','fullscreen','fontcolor','alignment','source']},
                    upload_to='tmp/',
                    allow_file_upload=True,
                    allow_image_upload=True
                    )       
    image = models.ImageField(verbose_name='Превью', upload_to='media',
                null=True, 
                blank = True, 
                width_field="width_field", 
                height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    created_time = models.DateTimeField('Время создания', auto_now_add=True)
    #last_modified_time = models.DateTimeField('Последняя модификация', auto_now=True)
    status = models.CharField('Статус', max_length=1, choices=STATUS_CHOICES)
    views = models.PositiveIntegerField('Просмотр', default=0)
    likes = models.PositiveIntegerField('Likes', default=0)
    topped = models.BooleanField('Топ', default=False)
    category = models.ForeignKey('Category', verbose_name='Категории',
                                 null=True,
                                 on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='Тэг', blank=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def get_absolute_url(self):
        return reverse('app:detail', kwargs={'article_id': self.pk})

class Category(models.Model):
    name = models.CharField('Категория', max_length=30)
    created_time = models.DateTimeField('Время создания', auto_now_add=True)
    last_modified_time = models.DateTimeField('Последняя модификация', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    name = models.CharField('Имя тэга', max_length=20)
    created_time = models.DateTimeField('Дата создания', auto_now_add=True)
    last_modified_time = models.DateTimeField('Дата последней модификации', auto_now=True)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name


class Contact(models.Model):
    contact_name = models.CharField('Имя контакта', max_length=20)
    contact_email = models.EmailField('Ваш email')
    content = models.TextField('Текст сообщения')

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратные связи"


    def __str__(self):
        return self.contact_email