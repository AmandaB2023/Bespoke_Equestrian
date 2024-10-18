from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    discount = models.IntegerField(validators=[MaxValueValidator(0),MaxValueValidator(100)],)
    active = models.BooleanField()

    def __str__(self):
        return self.code

def is_valid(self):
        """
        Check if the coupon is valid based on
        its active status, validity period, and usage.
        """
        now = timezone.now()
        return (
            self.active
            and not self.is_used
            and self.valid_from <= now <= self.valid_to
        )