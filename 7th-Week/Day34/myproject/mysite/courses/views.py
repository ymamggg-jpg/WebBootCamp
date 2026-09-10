from django.http import HttpResponse
from django.shortcuts import render


courses = [
    {
        "id": 1,
        "name": "Python Basics",
        "category": "Programming",
        "difficulty": "Beginner",
    },
    {
        "id": 2,
        "name": "Django Web Development",
        "category": "Programming",
        "difficulty": "Intermediate",
    },
    {
        "id": 3,
        "name": "Database Fundamentals",
        "category": "Database",
        "difficulty": "Beginner",
    },
    {
        "id": 4,
        "name": "Advanced SQL",
        "category": "Database",
        "difficulty": "Advanced",
    },
]


def course_list(request):
    category = request.GET.get("category")
    difficulty = request.GET.get("difficulty")
    search = request.GET.get("search")

    filtered_courses = courses

    if category:
        filtered_courses = [
            course for course in filtered_courses
            if course["category"] == category
        ]

    if difficulty:
        filtered_courses = [
            course for course in filtered_courses
            if course["difficulty"] == difficulty
        ]

    if search:
        filtered_courses = [
            course for course in filtered_courses
            if search.lower() in course["name"].lower()
        ]

    page = int(request.GET.get("page", 1))

    per_page = 2
    start = (page - 1) * per_page
    end = start + per_page

    page_courses = filtered_courses[start:end]

    return render(
        request,
        "courses/course_list.html",
        {
            "courses": page_courses,
            "page": page,
        }
    )


def course_detail(request, id):
    course = None

    for item in courses:
        if item["id"] == id:
            course = item
            break

    if not course:
        return HttpResponse("Course not found")

    tab = request.GET.get("tab", "details")

    return render(
        request,
        "courses/course_detail.html",
        {
            "course": course,
            "tab": tab
        }
    )