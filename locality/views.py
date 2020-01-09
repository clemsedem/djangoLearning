from django.shortcuts import render, redirect
from .models import Locality
from city.models import City
from .forms import LocalityForm
from django.contrib import messages


def index(request):
    city_ref = request.GET['city']
    region_ref = request.GET['region']
    city = City.objects.get(ref=city_ref)
    localities = Locality.objects.filter(city_id=city.id, status=True).order_by('-created_at')
    template = 'locality/index.html'
    context = {
        'city': city_ref,
        'city_name': city.city_name,
        'region': region_ref,
        'localities': localities
    }
    return render(request, template, context)


def new(request):
    city_ref = request.GET['city']
    region_ref = request.GET['region']

    if request.method == 'POST':
        form = LocalityForm(request.POST)
        if form.is_valid():
            locality = form.save(commit=False)
            locality.city = City.objects.get(ref=city_ref)
            locality.save()
            messages.add_message(request, messages.SUCCESS, 'Locality added successfully')
            return redirect('/localities/?city=' + city_ref + '&region=' + region_ref)
    else:
        form = LocalityForm()

    context = {
        'city': city_ref,
        'region': region_ref,
        'form': form,
    }
    return render(request, 'locality/new.html', context)


def edit(request, locality):
    region_ref = request.GET['region']
    city_ref = request.GET['city']
    c_locality = Locality.objects.get(ref=locality)
    if request.method == 'POST':
        form = LocalityForm(request.POST, instance=c_locality)
        if form.is_valid():
            # locality = form.save(commit=False)
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Locality updated successfully')
            return redirect('/localities/?city=' + city_ref + '&region=' + region_ref)
    else:
        form = LocalityForm(instance=c_locality)

    context = {
        'city': city_ref,
        'region': region_ref,
        'form': form,
    }
    return render(request, 'locality/edit.html', context)
    


def delete(request, locality):
    region = request.GET['region']
    city = request.GET['city']
    Locality.objects.filter(ref=locality).update(status=False)
    messages.add_message(request, messages.SUCCESS, 'Locality removed successfully')
    return redirect('/localities/?city=' + city + '&region=' + region)
