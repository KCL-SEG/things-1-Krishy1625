from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, max_length=120)
    quantity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def clean(self):
        super().clean()
        if Thing.objects.exclude(pk=self.pk).filter(name=self.name).exists():
            raise ValidationError({'name': 'Name must be unique'})