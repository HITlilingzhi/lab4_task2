from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
from models import Book,Author
    
    
def new_author(request):
    if request.POST:
        post = request.POST
        if Author.objects.filter(AuthorID = post["AuthorID"]):
            return render_to_response("author_has_exist.html")
        if post["AuthorID"].strip() == "" or post["Name"].strip() == "":
            return render_to_response("title_or_author_should_not_be_empty.html")
        else:
            new_author = Author(
                AuthorID = post["AuthorID"],
                Name = post["Name"],
                Age = post["Age"],
                Country = post["Country"],
                )           
            new_author.save()

    count = Author.objects.all().count()
    a = Context({'count':count})

    return render_to_response("creat_new_author.html", a)
    
def new_book(request):
    if request.POST:
        post = request.POST
        if not Author.objects.filter(AuthorID = post["AuthorID"]):         
            return render_to_response("you_should_creat_new_author_first.html")
        elif post["Title"].strip() == "" or post["AuthorID"].strip() == "":
            return render_to_response("title_or_author_should_not_be_empty.html")
        else:
            new_book = Book(
                Title = post["Title"],                
                ISBN = post["ISBN"],
                AuthorID = post["AuthorID"],
                Publisher = post["Publisher"],
                PublishDate = post["PublishDate"],
                Price = post["Price"],
                )           
            new_book.save()

    count = Book.objects.all().count()
    a = Context({'count':count})

    return render_to_response("new_book.html", a)


def book_list(request):
    book_list = Book.objects.all()
    
    count = Book.objects.all().count()
    b = Context({'count':count})
    
    c = Context({"book_list":book_list})   

    return render_to_response("show_book_list.html", b, c)
    
def author_list(request):
    author_list = Author.objects.all()
    
    count = Author.objects.all().count()
    b = Context({'count':count})
    
    c = Context({"author_list":author_list})   

    return render_to_response("show_author_list.html", b, c)


def search_author(request):
    if request.POST:
        post = request.POST
        search_author = post["search_author"]
        if Book.objects.filter(AuthorID = search_author):
            d = Context({"personal_book_list":Book.objects.filter(AuthorID = search_author)})
            return render_to_response("search_author_book_list.html", d)
        else:
            return render_to_response("dont_have_this_author.html")

def delete_book(request):
    id1 = request.GET["id"]
    Book.objects.filter(id = id1).delete()
    return render_to_response("delete_book_sucessfully.html")
    
def delete_author(request):
    id1 = request.GET["id"]
    tmp = Author.objects.get(id = id1)
    Book.objects.filter(AuthorID = tmp.AuthorID).delete()
    Author.objects.filter(id = id1).delete()
    return render_to_response("delete_author_sucessfully.html")
    
def update_book(request):
    id2 = request.GET["id"]
    book = Book.objects.get(id = id2)

    if request.POST:
        post = request.POST
        book.AuthorID = post["AuthorID"]
        book.Publisher = post["Publisher"]
        book.PublishDate = post["PublishDate"]
        book.Price = post["Price"]
              
        book.save()
        
    e = Context({'update_book':Book.objects.get(id = id2)})
    return render_to_response("update_book.html", e)

def show_book_information(request):
    id1 = request.GET["id"]
    book = Book.objects.get(id = id1)
    search_author = book.AuthorID
    author = Author.objects.get(AuthorID = search_author)
    a = Context({'book_information':book})
    b = Context({'author_information':author})
    return render_to_response("show_book_information.html", a , b)
