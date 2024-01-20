from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#Obtain user response

#Feed it to the model 

 
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

    #Feed the user message to the gpt model 
    #Have the chatbot send a response
    responseMessage = ["This is a default response", "I am ready to send stuff to the bot", "Waiting for inputt"]

    responseMessage = "<br>".join(responseMessage) 
    #Parse all the responses with new line characters
    return HttpResponse(responseMessage)