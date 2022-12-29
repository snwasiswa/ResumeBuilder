from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify


# Create your models here.

class Education:
    """Model for the education section"""
    school = models.CharField(blank=False, null=False, max_length=255)
    degree = models.CharField(blank=False, null=False, max_length=255)
    major = models.CharField(blank=False, null=False, max_length=255)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=4.00,
                              validators=[MinValueValidator(Decimal(0.00))])

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __init__(self):
        self.slug = None

    def save(self, *args, **kwargs):
        self.slug = slugify(self.school)
        super(Education, self).save(*args, **kwargs)

    def __str__(self):
        return self.school


