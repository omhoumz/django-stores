from django.db import models


class Entry(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ==> ' + self.email

    def is_valid(self):
        # validate the entry
        return True
