from django.contrib import admin
from placticeapp.models import Person, Organization


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "age",
        "nickname",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id",)


admin.site.register(Person, PersonAdmin)
admin.site.register(Organization)
