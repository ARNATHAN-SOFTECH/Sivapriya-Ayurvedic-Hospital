from django.db import models
from django.utils.text import slugify

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    experience = models.PositiveIntegerField()
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='doctors/')
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# main/models.py

class Gallery(models.Model):
    CATEGORY_CHOICES = (
        ('hospital', 'Hospital'),
        ('doctors', 'Doctors'),
        ('treatment', 'Treatment'),
        ('events', 'Events'),
    )

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title