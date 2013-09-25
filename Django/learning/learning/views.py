from django.http import HttpResponse
import datetime
from django import template
from learning.mytemp import *
###hello
def hello(request):
	return HttpResponse("Hello Guy")

###my_date
def my_date(request):
	now=datetime.datetime.now()
	html='<html><body><p>It is %s now<body></html>' % now
	return HttpResponse(html)


###thanks
def thanks(request):
	c=template.Context({'person_name':'Jhon','company':'Tulpar_company','ship_date':datetime.datetime.now(),'item_list':['dsf',344,455,'fg','ht'],'ordered_warranty':False})
	html=t.render(c)
	return HttpResponse(html) 
