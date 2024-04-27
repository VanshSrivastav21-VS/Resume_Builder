from django.shortcuts import render
from contactenquiry .models import contactEnquiry
from django.contrib.auth.decorators import login_required

@login_required
def contact(request):
    return render(request, 'contactenquiry/contact.html')

def saveEnquiry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        en = contactEnquiry(name=name, email=email, message=message)
        # Assuming 'contactEnquiry' is your model for storing contact inquiries
        en.save()  # Save the object to the database
    return render(request, 'contactenquiry/contact.html')


