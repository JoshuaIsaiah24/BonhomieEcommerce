from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from .forms import contactForm


# Create your views here.
def contact(request):
    if request.method == 'POST':
        contact_form = contactForm()
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            
            EmailMessage(
                
            'Contact Form Submission from {}'.format(name), 
            message, 
            'Bonhomiebasics.com', 
            ['maryjoybranzuela@gmail.com'], 
            reply_to=[email]).send()
            
            messages.success(request, 'Message successfully sent!')
            return redirect('contact')
        
    else:
        contact_form = contactForm()
        
    return render(request, 'contact/contact.html', {'contact_form':contact_form})