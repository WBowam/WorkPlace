from django.shortcuts import render_to_response
import datetime
def foursuper(request):
	return render_to_response('foursuper.html',{'person_name':'Jhon','company':'Tulpar_company','adword':'Come on popet','ship_date':datetime.datetime.now(),'item_list':['dsf',344,455,'fg','ht'],'ordered_warranty':False})