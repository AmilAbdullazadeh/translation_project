from modeltranslation.translator import translator, TranslationOptions
from pages.models import *


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


translator.register(News, NewsTranslationOptions)
