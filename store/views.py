"""
Define views and constraints for each view.
"""

from django.shortcuts import render

from book.models import Book
from footer.models import MyInformation
from store.models import Category


def booksforsale(request):
    """Define the Book For Sale display function."""

    return render(request, "booksforsale.html")


def booksforsale_subcategory(request, slug):
    """Define the Book For Sale To Subcategory display function."""

    specific_category = Category.objects.filter(slug=slug).first()
    subcategory = specific_category.subcategory.all()
    book = Book.objects.filter(category=specific_category.id)

    subcategory_list = []
    for _ in subcategory:
        for single_book in book:
            if single_book.subcategory is None:
                continue
            if single_book.subcategory.name not in subcategory_list:
                subcategory_list.append(single_book.subcategory.name)

    subcategory_list = set(subcategory_list)
    subcategory_list = list(subcategory_list)

    subcategory = specific_category.subcategory.filter(
        name__in=subcategory_list
    )

    context = {
        "specific_category": specific_category,
        "subcategory": subcategory,
        "book": book,
    }
    return render(request, "onecategorybookswithcategories.html", context)
