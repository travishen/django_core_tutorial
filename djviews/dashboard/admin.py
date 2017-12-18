from django.contrib import admin

from .models import Book
from .forms import BookForm

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "slug"
    ]
    readonly_fields = [
        'updated',
        'timestamp',
        'added_by',
        'last_edited_by'
    ]

    form = BookForm


admin.site.register(Book, BookAdmin)