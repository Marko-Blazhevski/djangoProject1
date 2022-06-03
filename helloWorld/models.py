from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()
    country = models.CharField(max_length=50, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Publication(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50, null=True, blank=True)
    house_number = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=17)
    short_context = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Author 1 : M Book
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)  # Publication 1 : M Book
    cover_page = models.ImageField(upload_to="book_covers/", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class PublicationAuthor(models.Model):  # Author M : M Publication
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
