from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, room):
    for room in room.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "pk",
        "name",
        "price",
        "kind",
        "owner",
        "total_amenities",
        "created_at",
        "rating",
    )
    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
    )
    search_fields = ("name", "=price", "owner__username")

    def total_amenities(self, room):
        return room.amenities.count()


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "description", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
