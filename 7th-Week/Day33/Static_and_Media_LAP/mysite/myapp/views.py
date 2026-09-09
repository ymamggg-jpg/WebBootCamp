from django.shortcuts import render

# Create your views here.


from django.core.files.storage import FileSystemStorage


def upload_image(request):

    if request.method == "POST":
        image = request.FILES.get("image")

        if image:
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)

            image_url = fs.url(filename)

            return render(request, "upload.html", {
                "image_url": image_url
            })

    return render(request, "upload.html")
