from django.contrib import admin

from .models import PointOfInterest


# Creating a custom admin interface for the PointOfInterest model
class PointOfInterestAdmin(admin.ModelAdmin):
    # Specifying which fields to display in the admin pannel view
    list_display = ("internal_id", "external_id", "name", "category", "avg_ratings")

    # Adding search functionality to specific fields
    search_fields = ["internal_id", "external_id"]

    # Adding filters to the admin list view
    list_filter = ["category"]


# Registering the PointOfInterest model with its custom admin interface
admin.site.register(PointOfInterest, PointOfInterestAdmin)
