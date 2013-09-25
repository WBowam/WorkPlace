# Create your views here.
from django.template import RequestContext 
from django.shortcuts import render_to_response
from form_contact.forms import ContactForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

#contact
def form_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['tulpar008@gmail.com'],
            )
            return HttpResponseRedirect('thank')
    else:
        form = ContactForm(initial={'subject':'I love you,my popet!','message':'Come on!popet!'})
    return render_to_response('form_contact.html', {'form':form},context_instance=RequestContext(request) )



#thank
def thank(request):
    return HttpResponse('<h1>Thank you,popet!</h1>')

