from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Coupon(models.Model):

    code = models.CharField(max_length=50,
                            unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),
                            MaxValueValidator(100)],
                help_text='Percentage value (0 to 100)')

    active = models.BooleanField()
    is_used = models.BooleanField()
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