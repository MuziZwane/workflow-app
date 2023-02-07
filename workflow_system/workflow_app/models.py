from django.db import models


# Create your models here.
class Customer(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_of_birth = models.DateField()
  upload_file = models.FileField(upload_to='uploads/')

  # i plan to store the data in a database
  month = models.CharField(max_length=50)
  income = models.FloatingField()
  expenses = models.FloatingField()

  def __str__(self):
    return self.first_name + " " + self.last_name
