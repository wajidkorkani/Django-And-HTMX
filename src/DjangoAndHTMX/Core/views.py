from django.shortcuts import render

# Create your views here.

def Home(request):
    template = 'index.html'
    context = {
        'text':'Hello world!'
    }
    return render (request, template, context)
