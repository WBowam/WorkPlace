import datetime 
from django.shortcuts import render_to_response
def threesuper(request):
	return render_to_response('threetemp.html',{'person_name':'Jhon','company':'Tulpar_company','adword':'Come on popet','ship_date':datetime.datetime.now(),'item_list':['dsf',344,455,'fg','ht'],'ordered_warranty':False})