from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def feed(request):
    posts = Post.objects.all()

    if request.method == "POST":
        username = request.POST.get("username")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        if image:
            allowed_types = [".jpg", ".jpeg", ".png"]

            if not any(image.name.lower().endswith(ext) for ext in allowed_types):
                return render(request, "feed.html", {
                    "posts": posts,
                    "error": "Only JPG, JPEG, and PNG files are allowed."
                })

        Post.objects.create(
            username=username,
            description=description,
            image=image
        )

        return redirect("feed")

    return render(request, "feed.html", {"posts": posts})

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.likes += 1
        post.save()

    return redirect("feed")