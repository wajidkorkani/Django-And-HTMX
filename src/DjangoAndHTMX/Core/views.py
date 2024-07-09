from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):
    template = 'index.html'
    context = {
        'text':'Hello world!'
    }
    return render (request, template, context)

def Test(request):
    return  HttpResponse('Working!')