from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):
    """We can make Wishlists for Rooms or Experiences"""

    name = models.CharField(max_length=250)
    room = models.ManyToManyField(
        "rooms.Room",
        blank=True,
        related_name="wishlists",
    )
    experience = models.ManyToManyField(
        "experiences.Experience",
        blank=True,
        related_name="wishlists",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )

    def __str__(self):
        return self.name
