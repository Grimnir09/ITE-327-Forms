from django.shortcuts import render, redirect
from django.http import response
from .forms import ReqFormAdd
from .models import Requisition

#index view
def index(request):
    return render(request,'webapp/index.html')

# /requisition url
def req_table(request):
    #show our database table
    requistions = Requisition.objects.order_by('clientName')
    #return our html with table context
    return render(request,'webapp/req_table.html', {
        'req_table' : requistions
    })

# /requsition/add url
def req_Add(request):
    # if our request to this url is a POST we save the form into our database
    if request.method == 'POST':
        # load our form data into form
        form = ReqFormAdd(request.POST)
        # check to see if we have any missing fields
        if form.is_valid():
            #instance our Requistion Model with our form data
            req = Requisition(
                clientName          = form.cleaned_data['clientName'],
                clientAddress       = form.cleaned_data['clientAddress'],
                clientTelephone     = form.cleaned_data['clientTelephone'],
                clientContact       = form.cleaned_data['clientContact'],
                clientJobTitle      = form.cleaned_data['clientJobTitle'],
                skillRequired       = form.cleaned_data['skillRequired'],
                educationLevel      = form.cleaned_data['educationLevel'],
                startDate           = form.cleaned_data['startDate'],
                endDate             = form.cleaned_data['endDate'],
                daysNeeded          = form.cleaned_data['daysNeeded'],
                dailyHours          = form.cleaned_data['dailyHours'],
                dailyRate           = form.cleaned_data['dailyRate'],
            )
            #commit our data to the model
            req.save()
            # redirect the user to our success page
            return redirect('success')
    else:
        #pass errors to our add page
        form = ReqFormAdd()
    # render the requsition add page
    return render(request, 'webapp/req_add.html', {'form':form})

# send our users to the success page
def success(request):
    return render(request, 'webapp/success.html')