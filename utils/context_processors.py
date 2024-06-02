from footer.models import MyInformation
from book.models import Book
from store.models import Category


def footer_and_category(request):
    """define a function to get footer and categories."""

    footer = MyInformation.objects.first_row()

    category = Book.objects.select_related("category").values_list(
        "category__name", flat=True
    )
    category = Category.objects.filter(name__in=category)

    context = {
        "footer": footer,
        "category": category,
    }

    return context