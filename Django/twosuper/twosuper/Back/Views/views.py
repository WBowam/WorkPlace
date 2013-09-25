from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

import datetime
def my_super(request):
	t=get_template('onetemp.py')
	c=Context({'person_name':'Jhon','company':'Tulpar_company','ship_date':datetime.datetime.now(),'item_list':['dsf',344,455,'fg','ht'],'ordered_warranty':False})
	html=t.render(c)
	return HttpResponse(html)