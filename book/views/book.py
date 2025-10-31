from django.shortcuts import get_object_or_404, redirect, render
from book.models import Category, Books,Comments,Favorite
from django.views import View
from django.db.models import Q

class HomeView(View):
    def get(self, request):
        books = Books.objects.all()[:6]
        return render(request, "book/index.html", context={"books": books})

class BooksAsView(View):
    def get(self, request):
        cid = request.GET.get('category')
        if cid:
            books = Books.objects.filter(category_id=cid)
        else:
            books = Books.objects.all()

        query = request.GET.get('q')
        if query:
            books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))

        return render(request, "book/books.html", context={"books":books})
    
class Category_as_View(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "book/category.html", context={"categories": categories})


class DetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        comments = Comments.objects.filter(book=book)
        is_favorite = False
        if request.user.is_authenticated:
            is_favorite = Favorite.objects.filter(user=request.user, book=book).exists()
        data ={
            'book':book,
            'comments':comments,
            'is_favorite': is_favorite
        }
        return render(request, "book/detail.html", context=data)
    
    def post(self, request, book_id):
        if not request.user.is_authenticated:
            return redirect('login')
        book = get_object_or_404(Books, id=book_id)
        text = request.POST.get('comment_text')
        if text:
            Comments.objects.create(user=request.user, book=book, text=text)
            
        return redirect('detail', book_id=book.id)