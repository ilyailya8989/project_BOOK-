from django.urls import path

from b_app import views

urlpatterns = [
    path('title/', views.displayBook, name='displayBook'),
    path('title/<int:book_id>', views.infoBook, name='infoBook'),
    path('title/belete/<int:book_id>', views.deleteBook, name='deleteBook'),
    path('title/createBook', views.createBook, name='createBook'),
    path('title/update/book', views.updataBook, name='updataBook'),

    path('title/<int:category_id>', views.displayCategory, name='displayCategory'),
    path('title/delete/<int:category_id>', views.deleteCategory, name='deleteCategory'),
    path('title/update/category/', views.updateCategory, name='updateCategory'),
    path('title/create/category/', views.creteCategory, name='creteCategory'),

    path('author/<int:author_id>', views.infoAutor, name='infoAuthor'),
    path('title/<int:author_id>', views.displayAutor, name='displayAutor'),

]
