from django.shortcuts import render, redirect

from cars_catalogue.cars.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from cars_catalogue.cars.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'index.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
    }
    return render(request, 'profile-create.html', context)


def catalogue(request):
    profile = get_profile()
    cars = Car.objects.all()
    cars_count = Car.objects.count()
    context = {
        'profile': profile,
        'cars': cars,
        'cars_count': cars_count,
    }
    return render(request, 'catalogue.html', context)


def create_car(request):
    if request.method == 'GET':
        form = CarCreateForm
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
    }

    return render(request, 'car-create.html', context)


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'car': car,
    }
    return render(request, 'car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car-delete.html', context)


def details_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_expenses = sum(c.price for c in cars)
    context = {
        'profile': profile,
        'total_expenses':total_expenses,
    }
    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    context = {
        'profile':profile,
        'form':form,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            cars.delete()
            form.save()
            return redirect('index')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile-delete.html', context)



