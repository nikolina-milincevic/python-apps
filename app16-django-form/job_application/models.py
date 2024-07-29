from django.db import models
# All this is model for the database table


class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)
    
    # Magic method for print output of an instance of class
    def __str__(self):
        return f"{self.first_name} {self.last_name}"