from django.contrib import admin

from blog.models import Category, Article, CustomUser, Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(CustomUser)
admin.site.register(Comment)
