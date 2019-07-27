from django.db import models

class Domain(models.Model):
    name = models.CharField(max_length=253)

    def __str__(self):
        return self.name

class Subdomain(models.Model):
    name = models.CharField(max_length=253)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
