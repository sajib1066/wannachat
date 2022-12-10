from django.urls import path

from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
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
]
