from django.contrib import admin

from chatroom import models


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ordering', 'slug']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'category_type', 'fee_status', 'is_active',
        'created_at', 'updated_at'
    ]
    list_filter = ['category_type', 'fee_status', 'is_active']
    search_fields = ['name']


@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'category', 'name', 'is_active', 'created_at', 'updated_at'
    ]
    list_filter = ['category', 'is_active']
    search_fields = ['name']


@admin.register(models.ChatRoomUser)
class ChatRoomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'user', 'created_at', 'updated_at']


@admin.register(models.DirectmessageUser)
class DirectmessageUserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'me', 'friends', 'friend_type', 'created_at', 'updated_at'
    ]


@admin.register(models.RoomMessage)
class RoomMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'user', 'created_at', 'updated_at']


@admin.register(models.DirectMessage)
class DirectMessageAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'sender_user', 'receiver_user', 'created_at', 'updated_at'
    ]
