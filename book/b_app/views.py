from django.shortcuts import render , get_object_or_404,redirect

from b_app.models import Book, Category, Author


def displayBook(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'b_app/displayInfoBook.html',{'books':books, 'categories':categories, 'authors':authors})
def infoBook(request, book_id):
    books = get_object_or_404(Book, id=book_id)
    return render(request, 'b_app/infoAboutBook.html', {'books':books})
def deleteBook(request, book_id):
    books = Book.objects.get(id=book_id)
    books.delete()
    return redirect('displayBook', )
def createBook(request):
    books = Book.objects.all()
    if request.method == 'POST':
        title_name = request.POST.get('title_name')
        author_name = request.POST.get('author_name')
        category_name = request.POST.get('category_name')
        description_name = request.POST.get('description_name')



        if title_name  and author_name and category_name and description_name:
            Book.objects.create(
                title_name=title_name,
                author_name=author_name,
                category_name=category_name,
                description_name=description_name
            )
            return redirect('createBook')
    return render(request, 'b_app/createBook.html', {'books':books})
def updataBook(request):
    books = Book.objects.all()
    if request.method == 'POST':
        books.title_name =request.POST.get('title_name')
        books.author_name =request.POST.get('author_name')
        books.category_name = request.POST.get('category_name')
        books.description_name = request.POST.get('description_name')
        books.save()
        return redirect('updataBook',)
    return render(request, 'b_app/updataBook.html', {'books':books})


def displayCategory(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    books = Book.objects.filter(cat=cat)
    context = {
        'cat': cat,
        'books': books
    }
    return render(request, 'b_app/infoCategory', context=context)

def deleteCategory(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    cat.delete()
    return redirect('displayBook', )

def updateCategory(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        name.save()
        return redirect('updateCategory',)
    return render(request,'b_app/updateCategory.html', {'categories': cat})

def creteCategory(request):
    cat = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name,)
            return redirect('creteCategory')
    return render(request, 'b_app/createCategory.html', {'cat':cat})



def displayAutor(request, author_id):
    authors = get_object_or_404(Author, id=author_id)
    return render(request, 'b_app/displayInfoCategory.html', {'authors':authors})

def infoAutor(request, author_id):
    authors = get_object_or_404(Author, id=author_id)
    return render(request, 'b_app/infoAuthor.html', {'authors':authors})