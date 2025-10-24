from django.db.models import (
    CharField,
)

from apps.lib.models import UUIDModel

class Resource(UUIDModel):
    link = CharField(max_length=500)
    description = CharField(max_length=300)

    def __str__(self):
        return self.description
