from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "published_date")
    list_filter = ("published_date",)
    search_fields = ("question_text",)

    inlines = [
        ChoiceInline,
    ]
