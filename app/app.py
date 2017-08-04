from django.apps import AppConfig

class ArticleAppConfig(AppConfig):
    name = "App" # Здесь указываем исходное имя приложения
    verbose_name = "Мой блог" # А здесь, имя которое необходимо отобразить в админке