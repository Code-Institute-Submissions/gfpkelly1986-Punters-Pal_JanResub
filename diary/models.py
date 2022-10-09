from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DiaryEntry(models.Model):
    race_title = models.CharField(
        max_length=100, unique=True, null=False, blank=False)
    race_type = models.CharField(
        max_length=100, null=False, blank=False, default='race')
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="new_entry"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    horse_name = models.CharField(
        max_length=100, unique=True, null=False, blank=False)
    grade = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)
    going = models.CharField(max_length=50)
    trainer = models.CharField(max_length=100)
    jockey = models.CharField(max_length=100)
    num_of_runners = models.IntegerField()
    result_of_entry = models.IntegerField()
    result_1 = models.CharField(max_length=100)
    result_2 = models.CharField(max_length=100)
    result_3 = models.CharField(max_length=100)
    note_detail = models.TextField()

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.race_title
