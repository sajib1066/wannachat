from django import forms

from chatroom.models import Category, SubCategory


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
