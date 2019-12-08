from django.db import models

class Requisition(models.Model):
    #define our objects manager
    objects = models.Manager()
    
    #our fields for our table
    clientName = models.CharField(max_length=100)
    clientAddress = models.CharField(max_length=100)
    clientTelephone = models.CharField(max_length=100)
    clientContact = models.CharField(max_length=100)
    clientJobTitle = models.CharField(max_length=100)
    skillRequired = models.CharField(max_length=1000)
    educationLevel = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    daysNeeded = models.IntegerField()
    dailyHours = models.IntegerField()
    dailyRate = models.FloatField()

    #display our client name for django admin
    def __str__(self): 
        return self.clientName

