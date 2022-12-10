from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from chatroom.models import Category
from chatroom.forms import CategoryForm


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/category/list.html'
    model = Category
    login_url = "/auth/admin-login/"
    paginate_by = 15

    def get_queryset(self, **kwargs):
        return self.model.objects.all()


class CategoryCreateView(LoginRequiredMixin, View):
    template_name = 'dashboard/category/create.html'
    model = Category
    form_class = CategoryForm
    login_url = "/auth/admin-login/"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:category_list')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class CategoryEditView(LoginRequiredMixin, View):
    template_name = 'dashboard/category/edit.html'
    model = Category
    form_class = CategoryForm
    login_url = "/auth/admin-login/"

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(self.model, pk=self.kwargs['pk'])
        form = self.form_class(instance=category)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        category = get_object_or_404(self.model, pk=self.kwargs['pk'])
        form = self.form_class(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboard:category_list')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class CategoryStatusUpdateView(LoginRequiredMixin, View):
    model = Category
    login_url = "/auth/admin-login/"

    def post(self, request, *args, **kwargs):
        category = get_object_or_404(self.model, pk=self.kwargs['pk'])
        if category.is_active:
            category.is_active = False
        else:
            category.is_active = True
        category.save()
        return redirect('dashboard:category_list')


class CategoryDeleteView(LoginRequiredMixin, View):
    model = Category
    login_url = "/auth/admin-login/"

    def post(self, request, *args, **kwargs):
        category = get_object_or_404(self.model, pk=self.kwargs['pk'])
        category.delete()
        return redirect('dashboard:category_list')
