# Register your models here.
from django.contrib import admin

from .models import Corporation
from .models import Location


class LocationInline(admin.TabularInline):
    model = Location
    extra = 1


@admin.register(Corporation)
class CorporationAdmin(admin.ModelAdmin):
    inlines = [LocationInline]


admin.site.register(Location)
