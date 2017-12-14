from django.contrib import admin

# Register your models here.

from .models import PostModel


class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'publish_date',
        'updated',
        'timestamp',
        'new_content'
    ]
    readonly_fields = [
        'updated',
        'timestamp',
        'new_content'
    ]

    @staticmethod
    def new_content(obj,  *args, **kwargs):
        return str(obj.title) + str(obj.publish_date)

    class Meta:
        model = PostModel


admin.site.register(PostModel, PostModelAdmin)
