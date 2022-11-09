from django.db import models
from common.models import CommonModel


class Experience(CommonModel):
    """Experience Model Definition"""

    name = models.CharField(max_length=250, default="")
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="experiences",
    )
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250, default="")
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perk = models.ManyToManyField(
        "experiences.Perk",
        related_name="experiences",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="experiences",
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):
    """What is included on an Experience"""

    name = models.CharField(max_length=100, default="", blank=True)
    detail = models.CharField(max_length=250, default="", blank=True)
    explanation = models.TextField()

    def __str__(self):
        return self.name
