from django.contrib import admin
from prompts.models import (
    Prompt,
    Tag,
    Feature,
)


class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 0

class PromptAdmin(admin.ModelAdmin):
    filter_horizontal = [
        'tags',
    ]
    inlines = [
        FeatureInline,
    ]

# Register your models here.
admin.site.register(Prompt, PromptAdmin)
admin.site.register(Tag)
admin.site.register(Feature)
