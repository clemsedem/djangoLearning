from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Suburb
from .forms import  SuburbForm

from locality.models import Locality


def index(request):
    region_ref = request.GET['region']
    city_ref = request.GET['city']
    locality_ref = request.GET['locality']

    locality = Locality.objects.get(ref=locality_ref)
    suburbs = Suburb.objects.filter(locality_id=locality.id, status=True).order_by('-created_at')
    template = 'suburb/index.html'
    context = {
        'suburbs': suburbs,
        'city': city_ref,
        'locality': locality_ref,
        'region': region_ref,
        'locality_name': locality.locality_name
    }
    return render(request, template, context)


def new(request):
    city_ref = request.GET['city']
    region_ref = request.GET['region']
    locality_ref = request.GET['locality']

    if request.method == 'POST':
        form = SuburbForm(request.POST)
        if form.is_valid():
            suburb = form.save(commit=False)
            suburb.locality = Locality.objects.get(ref=locality_ref)
            suburb.save()
            messages.add_message(request, messages.SUCCESS, 'Suburb added successfully')
            return redirect('/suburbs/?locality='+locality_ref+'&city='+ city_ref+'&region='+region_ref)
    else:
        form = SuburbForm()

    context = {
        'city': city_ref,
        'region': region_ref,
        'locality': locality_ref,
        'form': form,
    }
    return render(request, 'suburb/new.html', context)


def edit(request, suburb):
    city_ref = request.GET['city']
    region_ref = request.GET['region']
    locality_ref = request.GET['locality']
    suburb = Suburb.objects.get(ref=suburb)

    if request.method == 'POST':
        form = SuburbForm(request.POST, instance=suburb)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Suburb updated successfully')
            return redirect('/suburbs/?locality=' + locality_ref + '&city=' + city_ref + '&region=' + region_ref)
    else:
        form = SuburbForm(instance=suburb)

    context = {
        'city': city_ref,
        'region': region_ref,
        'locality': locality_ref,
        'form': form,
    }
    return render(request, 'suburb/edit.html', context)



def delete(request, suburb):
    city_ref = request.GET['city']
    region_ref = request.GET['region']
    locality_ref = request.GET['locality']
    Suburb.objects.filter(ref=suburb).update(status=False)
    messages.add_message(request, messages.SUCCESS, 'Suburb removed successfully')
    return redirect('/suburbs/?locality=' + locality_ref + '&city=' + city_ref + '&region=' + region_ref)