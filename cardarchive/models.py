from django.db import models

# Create your models here.
from django.db import models

class PokemonCardSet(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)

class PokemonCard(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    set = models.ForeignKey(PokemonCardSet, on_delete=models.RESTRICT)

    def __str__(self):
        return "{} (id: {})".format(self.name, self.id)