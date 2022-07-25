from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):

     def __init__(self, name, lastname):

          self.name = name

          self.lastname = lastname


def hello(request):

     p1=Persona("Profesor Juan", "Diaz")

     #name="Juan"

     #lastname="Perez"

     topics_list=["Template", "Models", "Forms", "Views", "Deploys"]

     now= datetime.datetime.now()
     
     #doc_externo = open("L:/luichix/code/python/practica/django/Proyecto1/Proyecto1/templates/myTemplate.html")
     
     #plt = Template(doc_externo.read())

     #doc_externo.close()

     #2 doc_externo = get_template("myTemplate.html")

     #ctx = Context({"name_person":p1.name, "lastname_person":p1.lastname, "now":now, "topics": topics_list})

     #2 documento = doc_externo.render({"name_person":p1.name, "lastname_person":p1.lastname, "now":now, "topics": topics_list})  #plt.render(ctx)

     return render(request, "myTemplate.html", {"name_person":p1.name, "lastname_person":p1.lastname, "now":now, "topics": topics_list} )  #HttpResponse(documento)

def courseC(request):

     now= datetime.datetime.now()
     
     return render(request, "courseC.html", {"get_date":now})

def courseCss(request):

     now= datetime.datetime.now()
     
     return render(request, "courseCss.html", {"get_date":now})


def bay(request):
     return HttpResponse("Good Bay, world.")

def see_you_again(request):
     return HttpResponse("See you again, world.")

def get_date(request):
     dateNow = datetime.datetime.now()
     return HttpResponse("Today is " + str(datetime.date.today()) + " and the time is " + str(dateNow))

def calculate_age(request, age ,year):
    #  actualAge = 26
     period = year - 2022
     futureAge = age + period

     return HttpResponse("You will be " + str(futureAge) + " years old in " + str(year))