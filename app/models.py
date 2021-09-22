from django.db import models

class Appointments(models.Model):
    first_name = models.CharField(max_length=10000)
    last_name = models.CharField(max_length=10000)
    email = models.CharField(max_length=10000)
    phone = models.CharField(max_length=10000)
    request = models.TextField(blank=True)
    sent_date = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name_plural = 'appointments'
        ordering = ['-sent_date']

    