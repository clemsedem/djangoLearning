from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
from region.models import Region
from django.contrib import messages

def index(request):
    ref = request.GET['region']
    print('path', request.get_full_path())
    region = Region.objects.get(ref=ref)
    cities = City.objects.filter(region_id=region.id, status=True).order_by('-created_at')
    template = 'city/index.html'
    context = {
        'cities': cities,
        'region_id': region.id,
        'region': region.region_name,
        'ref': ref,
        'path': request.get_full_path()
    }
    return render(request, template, context)


def new(request):
    ref = request.GET['region']

    if request.method == "POST":
        form = CityForm(request.POST)
        ref = request.POST['ref']
        if form.is_valid():
            city = form.save(commit=False)
            city.region = Region.objects.get(ref=ref)
            city.save()
            messages.add_message(request, messages.SUCCESS, 'City added successfully')
            return redirect('/cities/?region=' + ref)
    else:
        form = CityForm()

    context = {
        'ref': ref,
        'form': form,
    }
    return render(request, 'city/new.html', context)

    # ref = request.GET['region']
    # form = CityForm()
    # context = {
    #     'ref': ref,
    #     'form': form,
    # }
    # return render(request, 'city/new.html', context)


def create(request):
    form_data = CityForm(request.POST)
    ref = request.POST['ref']
    if form_data.is_valid():
        city = form_data.save(commit=False)
        city.region = Region.objects.get(ref=ref)
        city.save()
        messages.add_message(request, messages.SUCCESS, 'City added successfully')
        return redirect('/cities/?region='+ref)

    form = CityForm()
    context = {
        'ref': ref,
        'form': form,
    }
    return render(request, 'city/new.html', context)


