from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank = False)
    description = models.charField(max_length=120, blank = True)
    quantity = models.IntegerField(unique = False)
    
    def clean(self):
        super().clean()
        if self.quantity < 0:
            raise ValidationError("Quantity must not be negative")
        if self.quantity > 100:
            raise ValidationError("Quantity must not be greater than 100")

    def save(self, *args, **kwargs):
        self.full_clean()  # Run full_clean() before saving to ensure validation
        super().save(*args, **kwargs)
        #pass