from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5, null=True, blank=True)
    biography = models.fields.CharField(max_length=1000, null=True, blank=True)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)],
        null=True, blank=True
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'
    



class Listing(models.Model):
    
    title = models.fields.CharField(max_length=100)

    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)