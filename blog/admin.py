from django.contrib import admin
from .models import Blog , Category , Tags , Comments

# Register your models here.

# admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Comments)


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","create_at","author","category")
    list_filter = ("tags","category","author")
    search_fields = ("title",)

admin.site.register(Blog , BlogAdmin)