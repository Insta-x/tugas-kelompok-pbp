from email.policy import default
from pyexpat import model
from statistics import mode
from django.db import models
from django.utils import timezone
from authentication.models import User

class Project(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateField(default=timezone.now)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    donation_target = models.PositiveBigIntegerField()
    current_donation = models.PositiveBigIntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='projects_liked')