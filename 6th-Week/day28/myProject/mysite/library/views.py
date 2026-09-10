from django.shortcuts import render


# Create your views here.

books = [{"id":1 , "title":"welcome to Django" , "author":"Abdullah"},
         {"id":2 ,"title":"fastAPI demystified" , "author":"Taif"}]

def book_list(request):
    return render(request, "library/book_list.html" , {"books":books})

def book_detail(request):
    return render(request, "library/book_detail.html" , {"books":books})


