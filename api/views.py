from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.

def Todo(request):
    return JsonResponse("API POINT", safe=False)
