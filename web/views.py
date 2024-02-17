from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi shiv")

def about(request):
    return HttpResponse("Test About Page")
