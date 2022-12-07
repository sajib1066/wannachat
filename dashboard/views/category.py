from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from chatroom.models import Category


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/category/list.html'
    model = Category
    login_url = "/auth/admin-login/"

    def get_queryset(self, **kwargs):
        return self.model.objects.all()
