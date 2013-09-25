from django.http import HttpResponse

##hello
def hello(request):
	return HttpResponse('hello popet')
