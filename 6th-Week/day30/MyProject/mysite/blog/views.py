from django.shortcuts import render

# Create your views here.

# def list(request):
#     return render(request , "blog/list.html")

# def detail(request):
#     return render(request , "blog/detail.html")

# def category(request):
#     return render(request , "blog/category.html")




posts = [
    {
        "id": 1,
        "title": "Learning Django",
        "category": "python"
    },
    {
        "id": 2,
        "title": "CSS Tips",
        "category": "web"
    },
    {
        "id": 3,
        "title": "Python Basics",
        "category": "python"
    }
]


def list(request):
    return render(request, "blog/list.html", {"posts": posts})


def detail(request, id):
    post = next((post for post in posts 
                 if post["id"] == id), None)
    return render(request, "blog/post.html", {"post": post})


def category(request, category):
    filtered_posts = [
        post for post in posts
        if post["category"] == category
    ]

    return render(request, "blog/category.html",{"posts": filtered_posts, "category": category})