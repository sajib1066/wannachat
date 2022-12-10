from customauth.models import User
from chatroom.models import Category, SubCategory


def stats(request):
    context = {
        'total_user': User.objects.count(),
        'total_category': Category.objects.count(),
        'total_subcategory': SubCategory.objects.count(),
    }
    return context
