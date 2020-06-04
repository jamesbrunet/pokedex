from django.db import models

# Create your models here.
from django.db import models


class PokemonCard(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return "{} (id: {})".format(self.name, self.id)