import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)
    is_archived = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ("-updated_at", "-created_at")
        get_latest_by = ("updated_at",)
        verbose_name_plural = "Base Models"

    def delete(self):
        self.is_archived = True
        self.save()

    def restore(self):
        self.is_archived = False
        self.save()
