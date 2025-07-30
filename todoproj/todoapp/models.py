from django.db import models

# Create your models here.
class todoapp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    class Meta:
        db_table = "todo_db"