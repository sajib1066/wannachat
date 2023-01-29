from django import forms
from django_filters import (
    FilterSet, OrderingFilter, CharFilter, ModelChoiceFilter, ChoiceFilter
)
from django.db.models import Q

from chatroom.models import Category, SubCategory, Country


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'category_type', 'fee_status']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category_type': forms.Select(attrs={'class': 'form-control'}),
            'fee_status': forms.Select(attrs={'class': 'form-control'}),
        }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category', 'name', 'max_user', 'max_previous_message']

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'max_user': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_previous_message': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }


class CategoryFilterForm(FilterSet):
    q = CharFilter(
        label='Search',
        method='filter_by_q',
    )

    country = ModelChoiceFilter(
        queryset=Country.objects.all(),
        field_name='country',
        label='Country',
        empty_label='-Country-',
    )
    TYPE_CHOICES = (
        ('post', 'Post'),
        ('chatroom', 'Chat Room'),
    )
    FEE_STATUS_CHOICES = (
        ('free', 'Free'),
        ('paid', 'Paid'),
    )
    category_type = ChoiceFilter(
        field_name='category_type',
        choices=TYPE_CHOICES,
        label='Category Type',
        empty_label='-Category Type-',
    )
    fee_status = ChoiceFilter(
        field_name='fee_status',
        choices=FEE_STATUS_CHOICES,
        label='Fee Status',
        empty_label='-Fee Status-',
    )
    STATUS_CHOICES = (
        (True, 'Active'),
        (False, 'Inactive'),
    )
    is_active = ChoiceFilter(
        field_name='is_active',
        choices=STATUS_CHOICES,
        label='Status',
        empty_label='-Status-',
    )

    class Meta:
        model = Category
        fields = ()

    o = OrderingFilter(
        fields=(
            ('name', 'Name'),
            ('created_at', 'Created Date'),
            ('updated_at', 'Updated Date'),
        )
    )

    def filter_by_q(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) or Q(country__name__icontains=value)
        )


class SubCategoryFilterForm(FilterSet):
    q = CharFilter(
        label='Search',
        method='filter_by_q',
    )

    STATUS_CHOICES = (
        (True, 'Active'),
        (False, 'Inactive'),
    )
    is_active = ChoiceFilter(
        field_name='is_active',
        choices=STATUS_CHOICES,
        label='Status',
        empty_label='-Status-',
    )
    category = ModelChoiceFilter(
        queryset=Category.objects.all(),
        field_name='category',
        label='Category',
        empty_label='-Category-',
    )

    class Meta:
        model = SubCategory
        fields = ()

    o = OrderingFilter(
        fields=(
            ('name', 'Name'),
            ('created_at', 'Created Date'),
            ('updated_at', 'Updated Date'),
        )
    )

    def filter_by_q(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) or Q(category__name__icontains=value)
        )
