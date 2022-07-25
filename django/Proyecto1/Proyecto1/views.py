from django.http import HttpResponse
import datetime

def hello(request):
     return HttpResponse("Hello, world. This is my first page with python.")

def bay(request):
     return HttpResponse("Good Bay, world.")

def seeyouagain(request):
     return HttpResponse("See you again, world.")

def getDate(request):
     dateNow = datetime.datetime.now()
     return HttpResponse("Today is " + str(datetime.date.today()) + " and the time is " + str(dateNow))

def calculateAge(request, age ,year):
    #  actualAge = 26
     period = year - 2022
     futureAge = age + period

     return HttpResponse("You will be " + str(futureAge) + " years old in " + str(year))