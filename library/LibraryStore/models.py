from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    copies = models.IntegerField(default=1)
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return self.title
    
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    borrowed_books = models.ManyToManyField(Book,blank=True, related_name="borrowers")

    def __str__(self):
        return self.name
    

