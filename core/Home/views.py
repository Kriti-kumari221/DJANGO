from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return render(request,"index.html")

def success_page(request):
    print(10*'*')
    return HttpResponse("<h1>Hey this is a success Page</h1>")
