from django.contrib import admin
from .models import SampleDB, Question, Choice, Document# models.py で指定したクラス

# Register your models here.
class SampleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['sample1']}),
        ('表示する検索結果', {'fields': ['sample2']}),
    ]
    list_display = ('sample1', 'sample2')
    search_fields = ['sample1']


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

"""
class DocumentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,   {'fields': ['description']}),
        ('file', {'fields': ['document']}),
        ('Date', {'field': ['uploaded_at']}),
    ]
"""
admin.site.register(SampleDB, SampleAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Document)

