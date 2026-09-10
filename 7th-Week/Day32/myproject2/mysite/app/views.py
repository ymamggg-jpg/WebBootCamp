from django.shortcuts import render

# Create your views here.

courses = [
    {
        "id": 1,
        "name": "Python Basics",
        "level": "Beginner",
        "student_count": 15,
        "description": "Learn the basics of Python programming and build your first programs.",
        "image": "python.jpg",
    },
    {
        "id": 2,
        "name": "Django Development",
        "level": "Intermediate",
        "student_count": 8,
        "description": "Build modern web applications using Django.",
        "image": "django.jpg",
    },
    {
        "id": 3,
        "name": "Advanced Database",
        "level": "Advanced",
        "student_count": 0,
        "description": "Learn advanced database concepts, queries, and optimization techniques.",
        "image": "database.jpg",
    },
]


def home(request):
    context = {
        "username": "Ymam",
        "courses": courses,
    }

    return render(request, "home.html", context)

def course_list(request):
    context ={
        "courses":courses,

    }
    return render(request, "courses.html", context)


def course_detail(request, id):

    selected_course = None

    for course in courses:
        if course["id"] == id:
            selected_course = course
            break

    context = {
        "course": selected_course
    }

    return render(request, "course_detail.html", context)