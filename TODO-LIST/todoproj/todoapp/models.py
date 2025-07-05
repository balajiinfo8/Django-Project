from django.db import models

# Create your models here.
class TODOAPP(models.Model):
    id = models.IntegerField(primary_key=True)
    work_name = models.CharField(max_length=200)

    def __str__(self):
        return self.work_name