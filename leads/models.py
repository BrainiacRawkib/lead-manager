from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    message = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey('auth.User', related_name='leads', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
