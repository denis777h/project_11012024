from django.contrib import admin

from .models import Category, Article, Appointment, News, UserProfile

# Register your models here.


admin.site.register(Category)
admin.site.register(Article)
admin.site.register(UserProfile)
admin.site.register(News)
admin.site.register(Appointment)
