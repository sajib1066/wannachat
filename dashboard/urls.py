from django.urls import path

from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),

    # country urls
    path(
        'country-list/', views.CountryListView.as_view(),
        name='country_list'
    ),
    path(
        'country-create/', views.CountryCreateView.as_view(),
        name='country_create'
    ),
    path(
        'country/<int:pk>/edit/', views.CountryEditView.as_view(),
        name='country_edit'
    ),
    path(
        'country/<int:pk>/status-change/',
        views.CountryStatusUpdateView.as_view(),
        name='country_status_change'
    ),
    path(
        'country/<int:pk>/delete/', views.CountryDeleteView.as_view(),
        name='country_delete'
    ),

    # category urls
    path(
        'category-list/', views.CategoryListView.as_view(),
        name='category_list'
    ),
    path(
        'category-create/', views.CategoryCreateView.as_view(),
        name='category_create'
    ),
    path(
        'category/<int:pk>/edit/', views.CategoryEditView.as_view(),
        name='category_edit'
    ),
    path(
        'category/<int:pk>/status-change/',
        views.CategoryStatusUpdateView.as_view(),
        name='category_status_change'
    ),
    path(
        'category/<int:pk>/delete/', views.CategoryDeleteView.as_view(),
        name='category_delete'
    ),

    # sub category urls
    path(
        'subcategory-list/', views.SubCategoryListView.as_view(),
        name='subcategory_list'
    ),
    path(
        'subcategory-create/', views.SubCategoryCreateView.as_view(),
        name='subcategory_create'
    ),
    path(
        'subcategory/<int:pk>/edit/', views.SubCategoryEditView.as_view(),
        name='subcategory_edit'
    ),
    path(
        'subcategory/<int:pk>/status-change/',
        views.SubCategoryStatusUpdateView.as_view(),
        name='subcategory_status_change'
    ),
    path(
        'subcategory/<int:pk>/delete/', views.SubCategoryDeleteView.as_view(),
        name='subcategory_delete'
    ),
]
