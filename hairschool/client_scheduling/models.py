from django.db import models

# Create your models here.
class CScheduling(models.Model):
    #services include Haircut $20 for an example
    services = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    stylist = models.CharField(max_length=30)
   #For right now I am making date and time char fields will need to be changed
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=10)

   #Not sure on how to write this. used this site as a guide https://docs.djangoproject.com/en/2.0/ref/models/fields/
   # Date = models.DateField.unique_for_date
   # Time = models.Date.time.time()
   # or all together as
   # Date_Time = models.DateTimeField(auto_now=False, auto_now_add=False, **options) [source]
  
  #not sure if I need these 2 lines of code
   # def __unicode__(self):
   #    return self.CScheduling()