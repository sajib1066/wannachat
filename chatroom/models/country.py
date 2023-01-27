from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=220, unique=True)
    ordering = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=220, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('ordering', )

    def __str__(self):
        return self.name
