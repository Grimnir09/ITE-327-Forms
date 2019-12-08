from django import forms

class ReqFormAdd(forms.Form):
    clientName = forms.CharField(max_length=100)
    clientAddress = forms.CharField(max_length=100)
    clientTelephone = forms.CharField(max_length=100)
    clientContact = forms.CharField(max_length=100)
    clientJobTitle = forms.CharField(max_length=100)
    skillRequired = forms.CharField(max_length=1000)
    educationLevel = forms.CharField(max_length=100)
    startDate = forms.DateField()
    endDate = forms.DateField()
    daysNeeded = forms.IntegerField()
    dailyHours = forms.IntegerField()
    dailyRate = forms.FloatField()