from django.contrib import admin
from trafficking.models import *

class VictimAdmin(admin.ModelAdmin):
    list_display = ("name", "victim_type")

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, ]


admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Victim, VictimAdmin)
admin.site.register(UserExtra)

