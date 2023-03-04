from customauth.models import User
from chatroom.models import Country, Category, SubCategory


def stats(request):
    context = {
        'total_user': User.objects.count(),
        'total_country': Country.objects.filter(is_active=True).count(),
        'total_category': Category.objects.count(),
        'total_subcategory': SubCategory.objects.count(),
    }
    return context
