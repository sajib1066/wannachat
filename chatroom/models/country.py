from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=220, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    @property
    def total_chatrooms(self):
        return self.chatroom.all().count()


class State(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='states'
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('country', 'name')
        ordering = ('name', )

    def __str__(self):
        return self.name
