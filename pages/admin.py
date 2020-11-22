from django.contrib import admin
from pages.models import *
from modeltranslation.admin import TranslationAdmin


# Register your models here.
class NewsAdmin(TranslationAdmin):
    pass


admin.site.register(News, NewsAdmin)
