from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    html="""
    <html>
    <head>
        <title>
            contact us
        </title>
    </head>

    <body>
        <ul>
            <li ><a href="home">home</a></li>
            <li><a href=about>about</a></li>
            <li><a href="contact">contact</a></li>
          </ul>
          <h1>welcome</h1>
          """
    return HttpResponse(html)

def contact(request):
 return render(request,'pages/contact.html')
 
def about(request):
 return render(request,'pages/about.html')