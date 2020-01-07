from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Region
from my_validators import required_field, letters_n_space_only, region_already_exist
from django.core.exceptions import ValidationError
from django.contrib import messages


def index(request):
    regions = Region.objects.filter(status=True).order_by('-created_at')
    template = 'region/index.html'
    context = {
        'regions': regions,
    }
    return render(request, template, context)


def new(request):
    return render(request, 'region/new.html')


def edit(request, ref):
    region = Region.objects.get(ref=ref)
    template = 'region/edit.html'
    context = {'region': region}
    return render(request, template, context)


def create(request):
    region_name = request.POST['region']
    try:
        region_name = required_field(region_name)
        region_name = letters_n_space_only(region_name)
        region_name = region_already_exist(region_name)

        region = Region(region_name=region_name)
        region.save()
        messages.add_message(request, messages.SUCCESS, 'Region added successfully')
        return redirect('region_index')
    except ValidationError as e:
        return HttpResponse(e)


def update(request):
    new_region = request.POST['region']
    ref = request.POST['jref']
    try:
        new_region = required_field(new_region)
        new_region = letters_n_space_only(new_region)
        region_update = Region.objects.filter(ref=ref)
        region_update.update(region_name=new_region)
        return redirect('region_index')
    except ValidationError as e:
        return HttpResponse(e)



def delete(request, ref):
    region = Region.objects.filter(ref=ref)
    region.update(status=False)
    messages.add_message(request, messages.SUCCESS, 'Region removed successfully')
    return redirect('region_index')

