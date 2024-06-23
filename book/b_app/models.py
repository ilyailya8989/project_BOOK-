from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors/%d-%m-%y')
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ManyToManyField(Category, related_name='books')
    description = models.TextField()

    def __str__(self):
        return f"Книга - {self.title} || Автор {self.author}"