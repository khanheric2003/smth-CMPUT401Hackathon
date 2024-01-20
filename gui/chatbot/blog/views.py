from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    theList = [1,2,3,4,5]
    return HttpResponse(theList)
def article(request, article_id):
    theID = article_id + 1
    return render(request, 'blog/index.html', {"article_id": theID})
def getResponse(request):
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)