from django.apps import AppConfig


class BookBrowserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_browser'
    def ready(self):
        import book_browser.signals