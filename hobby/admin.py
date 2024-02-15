from django.contrib import admin
from .models import Hobby, Comments, Catalog

admin.site.register(Catalog)

# Register your models here.
@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post_hobby')

