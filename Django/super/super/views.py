from django.http import HttpResponse
from django import template
import datetime
def my_super(request):
	try:
		with open('/home/tulpar/Workplace/WorkPlace/Django/super/super/super.html','r') as fp:
			t=template.Template(fp.read())
	except:
		print 'Error'
	c=template.Context({'person_name':'Jhon','company':'Tulpar_company','ship_date':datetime.datetime.now(),'item_list':['dsf',344,455,'fg','ht'],'ordered_warranty':False})
	return HttpResponse(t.render(c))