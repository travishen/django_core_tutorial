from django.contrib import admin

from .models import Car


class CarAdmin(admin.ModelAdmin):
    search_fields = ['name', 'id', 'owner_name', 'owner_id']
    raw_id_fields = ['drivers']

    class Meta:
        model = Car

    def save_model(self, request, obj, form, change):
        if change:
            obj.update_by = request.user
        obj.save()

# Register your models here.


admin.site.register(Car, CarAdmin)
