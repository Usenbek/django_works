from django.shortcuts import render
from django.http import HttpResponse
from .models import Thing
from .form import ThingForm


def home(request):
    return render(request, 'base.html')


"""select * from thing"""
def things(request):
    things = Thing.objects.all() 
    return render(request, 'things/thing.html', context={'things': things})


def thing_detail(request, thing_id):
    thing = Thing.objects.filter(id=thing_id).first()
    return render(request, 'things/thing_detail.html', context={'thing': thing})

def make_thing(request):
    if request.method == 'GET':
        form = ThingForm()
        return render(request, 'things/make_thing.html', context={'form': form})
    elif request.method == "POST":
        form = ThingForm(request.POST, request.FILES)
        if form.is_valid():
           Thing.objects.create(
               Title = form.cleaned_data['Title'],
               description = form.cleaned_data['description'],
               value = form.cleaned_data['value'],
               photo = form.cleaned_data['photo']
           ) 
        # Thing.objects.create(
        # Title = request.POST.get('Title'),
        # description = request.POST.get('description'),
        # value = request.POST.get('value'),
        # photo = request.FILES.get('photo')

        # )
        return HttpResponse("Thing created")
        