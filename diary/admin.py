from django.contrib import admin
from .models import DiaryEntry


# Register your models here.
@admin.register(DiaryEntry)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('horse_name', 'grade', 'distance', 'going', 'trainer')
    list_filter = ('horse_name', 'trainer', 'jockey')
    search_fields = ('horse_name', 'trainer', 'jockey', 'race_title')
    # actions = ['listoffunctionnames'] add later
