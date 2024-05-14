from django.apps import AppConfig


class BooksConfig(AppConfig):
    """
    the book config class is automatically created as we create the books app
    command :  python manage.py startapp books
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "books"
