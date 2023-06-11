from django.db import models


class World(models.Model):
    name = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    ethnicity = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' | ' + self.continent + ' | ' + self.language + ' | ' + str(self.ethnicity)
