from django.db import models

from customauth.models import User


class Category(models.Model):
    TYPE_CHOICES = (
        ('post', 'Post'),
        ('chatroom', 'Chat Room'),
    )
    FEE_STATUS_CHOICES = (
        ('free', 'Free'),
        ('paid', 'Paid'),
    )
    country = models.ForeignKey(
        "chatroom.Country", on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=255, unique=True)
    category_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    fee_status = models.CharField(max_length=20, choices=FEE_STATUS_CHOICES)
    ordering = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def total_sub_category(self):
        return self.sub_categories.all().count()

    def category_type_display(self):
        return dict(self.TYPE_CHOICES)[self.category_type]

    def fee_status_display(self):
        return dict(self.FEE_STATUS_CHOICES)[self.fee_status]


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

    @property
    def current_users(self):
        return self.chatroom.count()


class ChatRoomUser(models.Model):
    room = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name='chatroom'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='chatroom_users'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
