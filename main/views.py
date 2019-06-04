from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Messages
from django.http import Http404
from .forms import MessagesForm
from datetime import datetime
from django.utils import formats
from django.urls import reverse
from django.contrib import messages
from django.db import models
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.mail import send_mail
import requests

# Create your views here.

def main(request):
    template = 'main/index.html'
    if request.method == 'GET':
        return render(request,template)
    form = MessagesForm(request.POST)
    if form.is_valid():
        #if request.POST.get("save"):
        name = form.cleaned_data['firstname']
        surname = form.cleaned_data['lastname']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        capped_name = name[0:1].capitalize()+name[1:len(name)].lower()
        capped_surname = surname[0:1].capitalize()+surname[1:len(surname)].lower()
        #form.save()
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
            }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''

        if result['success']:
            form.save()
            #send email
            heading = 'Automated reply - EyeC Consulting'
            subject = str('Dear ' + capped_name +' '+ capped_surname + ',\n '
            +'\nWe acknowledge receipt of your query for which we thank you and inform you that same is being attended to. \n'
            +'\nWe furthermore provide you with the assurance of it being our primary objective to provide the relevant feedback in due course.\n'
            +'\nThanking you in advance.')
            send_mail(heading,subject,settings.EMAIL_HOST_USER,[email],fail_silently=False)
            messages.success(request,'Thank you Mr/Ms '+ capped_name +' '+ capped_surname + ', we will respond momentarily.')
        #    messages.success(request, 'New comment added with success!')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        # ''' Till here'''
        return redirect('account:main')
    context = {'form':form}
    return render(request, template,context)
