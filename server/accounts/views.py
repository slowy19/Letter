from django.shortcuts import render

# Create your views here.
def login(response):
    return render(response, '../client/public/index.html')