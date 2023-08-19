from django.db import models

# Create your models here.
# se crea la tabla task que se ereda desde models esto es para crear la tabla 
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)

