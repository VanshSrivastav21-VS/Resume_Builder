from django.shortcuts import render, redirect
from .models import ContactForm, ResumeTemplate
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'resumebuilder/home.html')

@login_required
def resume(request): 
	if request.method == 'POST': 
		name = request.POST.get('name', '') 
		about = request.POST.get('about', '') 
		age = request.POST.get('age', '') 
		email = request.POST.get('email', '') 
		phone = request.POST.get('phone', '') 
		skill1 = request.POST.get('skill1', '') 
		skill2 = request.POST.get('skill2', '') 
		skill3 = request.POST.get('skill3', '') 
		skill4 =request.POST.get('skill4', '') 
		skill5 =request.POST.get('skill5', '') 
		degree1 = request.POST.get('degree1', '') 
		college1 = request.POST.get('college1', '') 
		year1 = request.POST.get('year1', '') 
		degree2 = request.POST.get('degree2', '') 
		college2 = request.POST.get('college2', '') 
		year2 = request.POST.get('year2', '') 
		college3 = request.POST.get('college3', '') 
		year3 = request.POST.get('year3', '') 
		degree3 = request.POST.get('degree3', '') 
		lang1 = request.POST.get('lang1', '') 
		lang2 = request.POST.get('lang2', '') 
		lang3 = request.POST.get('lang3', '')	 
		project1= request.POST.get('project1', '') 
		durat1 = request.POST.get('duration1', '') 
		desc1 = request.POST.get('desc1', '') 
		project2 = request.POST.get('project2', '') 
		durat2 = request.POST.get('duration2', '') 
		desc2 = request.POST.get('desc2', '') 
		company1 = request.POST.get('company1', '') 
		post1 = request.POST.get('post1', '') 
		duration1 = request.POST.get('duration1', '') 
		lin11 = request.POST.get('lin11', '') 
		company2 = request.POST.get('company2', '') 
		post2 = request.POST.get('post2', '') 
		duration2 = request.POST.get('duration2', '') 
		lin21 = request.POST.get('lin21', '') 
		ach1 = request.POST.get('ach1', '') 
		ach2 = request.POST.get('ach2', '') 
		ach3 = request.POST.get('ach3', '') 
		return render(request, 'resumebuilder/resume.html', {'name':name, 
											'about':about, 'skill5':skill5, 
											'age':age, 'email':email, 
											'phone':phone, 'skill1':skill1, 
											'skill2':skill2, 'skill3':skill3, 
											'skill4':skill4, 'degree1':degree1, 
											'college1':college1, 'year1':year1, 
											'college3':college3, 'year3':year3, 
											'degree3':degree3, 'lang1':lang1, 
											'lang2':lang2, 'lang3':lang3, 
											'degree2':degree2, 'college2':college2, 
											'year2':year2, 'project1':project1, 
											'durat1':durat1, 'desc1':desc1, 
											'project2':project2, 'durat2':durat2, 
											'desc2':desc2, 'company1':company1, 
											'post1':post1, 'duration1': duration1, 
											'company2':company2, 'post2':post2, 
											'duration2': duration2,'lin11':lin11, 
												'lin21':lin21, 'ach1':ach1, 
												'ach2':ach2,'ach3':ach3 }) 
	
	return render(request, 'resumebuilder/resumetemplate.html') 

@login_required
def resume_templates(request):
    templates = ResumeTemplate.objects.all()
    return render(request, 'resumebuilder/resume_templates.html', {'templates': templates})

@login_required
def resumetemplate(request):
    return render(request, 'resumebuilder/resumetemplates.html')

@login_required
def resumetemplatedownload(request):
    templates = ResumeTemplate.objects.all()
    return render(request, 'resumebuilder/resumetemplatedownload.html', {'templates': templates})

@login_required
def about(request):
    return render(request, 'resumebuilder/about.html')

@login_required
def contact(request):
    if request.method == 'POST':
        # Process form submission
        # You can access form data using request.POST
        # For example:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the database or perform any other necessary actions

        # Example of saving the form data to a ContactForm model
        ContactForm.objects.create(name=name, email=email, message=message)

        # Display a success message
        messages.success(request, 'Your message has been sent successfully!')
        
        # Redirect to the contact page again or to a thank you page
        return redirect('contact')

    # If the request method is GET, render the contact page template
    return render(request, 'contact.html')

@login_required
def submit_contact(request):
    if request.method == 'POST':
        # Process the form data
        # Example: Saving the form data to the database
        
        # Redirect to a success page
        return HttpResponseRedirect(reverse('home'))
    else:
        # Handle GET requests or other cases
        # Example: Render a form template
        return render(request, 'contact_form.html', contact)


