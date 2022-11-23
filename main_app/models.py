from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Challenge(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=250)
    # Add ManyToManyField here (later)
    
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse('detail', kwargs={'challenge_id': self.id})

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=400)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    challenge = models.ForeignKey(
        Challenge,
        on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-date']
    
    