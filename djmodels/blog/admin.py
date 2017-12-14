from django.contrib import admin

# Register your models here.

from .models import PostModel


class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'publish_date',
        'updated',
        'timestamp',
        'get_age',
        'publish'
    ]
    readonly_fields = [
        'updated',
        'timestamp',
        'get_age'
    ]

    @staticmethod
    def get_age(obj):
        return obj.age

    class Meta:
        model = PostModel


admin.site.register(PostModel, PostModelAdmin)
