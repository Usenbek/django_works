from django.shortcuts import render
from .models import Thing


def home(request):
    return render(request, 'base.html')


"""select * from thing"""
def things(request):
    things = Thing.objects.all()
    return render(request, 'things/thing.html', context={'things': things})


def thing_detail(request, thing_id):
    thing = Thing.objects.filter(id=thing_id).first()
    return render(request, 'things/thing_detail.html', context={'thing': thing})