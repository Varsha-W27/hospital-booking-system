from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    doctor_name = models.CharField(max_length=100)

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username