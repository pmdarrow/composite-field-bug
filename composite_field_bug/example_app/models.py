from django.db import models
from composite_field import CompositeField


class Details(CompositeField):
    code = models.TextField()
    linenos = models.BooleanField(default=False)


class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    details = Details()
