from django.shortcuts import render
from rest_framework import viewsets
from api1.models import Company
from api1.serializers import Companyserializer
from django.http import HttpResponse,JsonResponse
# Create your views here.

class Companyviewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Companyserializer

# def apifunc(request):
#     return HttpResponse("<h2>Hello World!!</h2> <p>testing views.py<p>")

# def home_page(request):
#     print("Home page requested successfully")
#     # friends = ["Andy","Mink","Cury","Tom"]
#     # grade = ("IX","XX","X","IV")
#     d1 = dict(Name="Bhawana",Age=30,Designation = "Engineer")
#     return JsonResponse(d1,safe=False)
