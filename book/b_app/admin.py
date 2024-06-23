from django.contrib import admin

from b_app.models import Book, Author, Category

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)

