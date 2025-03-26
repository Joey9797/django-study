from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(60)
        ],
        max_length=60
    )
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
