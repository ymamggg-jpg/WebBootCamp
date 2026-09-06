from django.shortcuts import render

# Create your views here.
def course_list(request):
 return render (request, "courses/courses.html")

def course_detail(request , slug):
 return render(request , "courses/course_detail.html" , {"slug":slug})

def category(request):
 return render(request , "courses/category.html")
