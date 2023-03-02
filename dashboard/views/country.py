from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from chatroom.models import Country
from chatroom.forms import CountryForm, CountryFilterForm


class CountryListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/country/list.html'
    model = Country
    login_url = "/auth/admin-login/"
    paginate_by = 15
    filterset_form = CountryFilterForm

    def get_queryset(self, **kwargs):
        objects = self.model.objects.all()
        self.filterset = self.filterset_form(
            data=self.request.GET, queryset=objects,
            request=self.request
        )
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = self.filterset.qs.count()
        context['filterset_form'] = self.filterset.form
        return context


class CountryCreateView(LoginRequiredMixin, View):
    template_name = 'dashboard/country/create.html'
    model = Country
    form_class = CountryForm
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
            return redirect('dashboard:country_list')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class CountryEditView(LoginRequiredMixin, View):
    template_name = 'dashboard/country/edit.html'
    model = Country
    form_class = CountryForm
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
            return redirect('dashboard:country_list')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class CountryStatusUpdateView(LoginRequiredMixin, View):
    model = Country
    login_url = "/auth/admin-login/"

    def post(self, request, *args, **kwargs):
        category = get_object_or_404(self.model, pk=self.kwargs['pk'])
        if category.is_active:
            category.is_active = False
        else:
            category.is_active = True
        category.save()
        return redirect('dashboard:country_list')


class CountryDeleteView(LoginRequiredMixin, View):
    model = Country
    login_url = "/auth/admin-login/"

    def post(self, request, *args, **kwargs):
        category = get_object_or_404(self.model, pk=self.kwargs['pk'])
        category.delete()
        return redirect('dashboard:country_list')
