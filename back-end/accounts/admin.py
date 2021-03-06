from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'nickname',
        'email',
    )

    list_display_links = (
        'nickname',
        'email',
    )