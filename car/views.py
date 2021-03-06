from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import carName, Manufacturer
from .forms import carNameForm, ManufacturerForm
from django.shortcuts import render,render_to_response

def index(request):

    brand = Manufacturer.objects.all()
    context = {
                'brand': brand,
            }
    return render(request,"index.html",context)



def cardetails(request, num=None):
    instance = carName.objects.get(id = num)
    context = {
     "car" : instance,}
    return render(request,"carview.html",context)


def about(request, num=None):
    return render(request,"about.html")

def guide(request, num=None):
    return render(request,"guide.html")

def emi(request, num=None):
    return render(request,"emi.html")

def carcost(request, num=None):
    return render(request,"carcost.html")

def cargrid(request):
    instance = carName.objects.all()
    context = {
     "cars" : instance,}
    return render(request,"grid.html",context)


def compare1(request):
    instance = carName.objects.all()
    context = {
     "cars" : instance,}
    return render(request,"compare1.html",context)

def compare2(request, num1 = None):
    instance = carName.objects.all()
    instance1 = carName.objects.get(id = num1)
    context = {
     "select" : instance1,
     "cars" : instance,}
    return render(request,"compare2.html",context)


def compareresult(request, num1=None, num2=None):
    instance1 = carName.objects.get(id = num1)
    instance2 = carName.objects.get(id = num2)
    context = {
     "car1" : instance1,
     "car2" : instance2,	}
    return render(request,"compare.html",context)


class carNameListView(ListView):
    model = carName


class carNameCreateView(CreateView):
    model = carName
    form_class = carNameForm


class carNameDetailView(DetailView):
    model = carName


class carNameUpdateView(UpdateView):
    model = carName
    form_class = carNameForm


class ManufacturerListView(ListView):
    model = Manufacturer


class ManufacturerCreateView(CreateView):
    model = Manufacturer
    form_class = ManufacturerForm


class ManufacturerDetailView(DetailView):
    model = Manufacturer


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm

