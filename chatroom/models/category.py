from django.db import models


class Category(models.Model):
    TYPE_CHOICES = (
        ('post', 'Post'),
        ('chatroom', 'Chat Room'),
    )
    FEE_STATUS_CHOICES = (
        ('free', 'Free'),
        ('paid', 'Paid'),
    )
    name = models.CharField(max_length=255, unique=True)
    category_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    fee_status = models.CharField(max_length=20, choices=FEE_STATUS_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def total_sub_category(self):
        return self.sub_categories.all().count()


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='sub_categories'
    )
    name = models.CharField(max_length=255)
    max_user = models.PositiveIntegerField(default=35)
    max_previous_message = models.PositiveIntegerField(default=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['category', 'name']

    def __str__(self):
        return f"{self.category.name} ({self.name})"
