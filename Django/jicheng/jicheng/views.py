from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import datetime
from books.models import Book
def foursuper(request):
	return render_to_response('foursuper.html',{'person_name':'Jhon','company':'Tulpar_company','adword':'Come on popet','ship_date':datetime.datetime.now(),'item_list':['dsf',344,455,'fg','ht'],'ordered_warranty':False})



def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

###Version 2 of desplay_meta() with templates
def display_meta2(request):
    return render_to_response('info.html',{'html':request.META.items()}) 

def view(request):
    return HttpResponse('welcome to %s'%request.path)



def agent(request):
    ua=request.META.get('HTTP_USER_AGENT','No info')
    return HttpResponse('Yours :%s'%ua)



##search_form 
def search_form(request):
    return render_to_response('search_form.html')

##search
def search(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error.append('please enter a search item')
        elif len(q)>20:
            error.append('Please enter a char in 20')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_result.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'error': error})
'''
	
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html',
        {'errors': errors})
'''
