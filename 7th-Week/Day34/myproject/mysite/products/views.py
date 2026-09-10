from django.shortcuts import render
from django.http import Http404


products = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "category": "Electronics",
        "price": 250,
        "rating": 4.5,
        "description": "Comfortable wireless headphones with clear sound.",
    },
    {
        "id": 2,
        "name": "Mechanical Keyboard",
        "category": "Electronics",
        "price": 320,
        "rating": 4.8,
        "description": "Mechanical keyboard suitable for gaming and work.",
    },
    {
        "id": 3,
        "name": "Coffee Mug",
        "category": "Home",
        "price": 45,
        "rating": 4.2,
        "description": "Simple ceramic mug for hot drinks.",
    },
    {
        "id": 4,
        "name": "Desk Lamp",
        "category": "Home",
        "price": 120,
        "rating": 4.6,
        "description": "Adjustable desk lamp with warm lighting.",
    },
]


def product_list(request):

    category = request.GET.get("category")
    min_price = request.GET.get("min_price")
    q = request.GET.get("q")
    sort = request.GET.get("sort", "name")

    filtered_products = products

    # Category filter
    if category:
        filtered_products = [
            product
            for product in filtered_products
            if product["category"] == category
        ]

    # Minimum price filter
    if min_price:
        try:
            min_price = float(min_price)

            filtered_products = [
                product
                for product in filtered_products
                if product["price"] >= min_price
            ]

        except ValueError:
            pass

    # Search
    if q:
        filtered_products = [
            product
            for product in filtered_products
            if q.lower() in product["name"].lower()
        ]

    # Sorting
    allowed_sorts = ["price", "rating", "name"]

    if sort not in allowed_sorts:
        sort = "name"

    filtered_products = sorted(
        filtered_products,
        key=lambda product: product[sort]
    )

    # Pagination
    page = request.GET.get("page", 1)

    try:
        page = int(page)

        if page < 1:
            page = 1

    except ValueError:
        page = 1

    per_page = 2

    start = (page - 1) * per_page
    end = start + per_page

    page_products = filtered_products[start:end]

    return render(
        request,
        "products/product_list.html",
        {
            "products": page_products,
            "page": page,
        }
    )


def product_detail(request, id):

    product = None

    for item in products:
        if item["id"] == id:
            product = item
            break

    if product is None:
        raise Http404("Product not found")

    tab = request.GET.get("tab", "details")

    allowed_tabs = ["details", "reviews", "shipping"]

    if tab not in allowed_tabs:
        tab = "details"

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "tab": tab,
        }
    )