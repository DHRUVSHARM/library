from django.db import models

# Create your models here.
# books/models.py
from django.db import models

"""
# Example data for Book instances

book1 = Book(
    title="Journey to the Center of the Earth",
    subtitle="An extraordinary voyage into the planet",
    author="Jules Verne",
    isbn="9780451532152"
)

book2 = Book(
    title="The Great Gatsby",
    subtitle="A story of the fabulously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan",
    author="F. Scott Fitzgerald",
    isbn="9780743273565"
)

book3 = Book(
    title="1984",
    subtitle="A dystopian social science fiction novel and cautionary tale",
    author="George Orwell",
    isbn="9780451524935"
)

"""


class Book(models.Model):

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
