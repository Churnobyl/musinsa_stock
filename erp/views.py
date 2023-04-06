from django.shortcuts import render, redirect
from .models import Stuff


def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/erp')
    else:
        return redirect('/sign-in')


def erp(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_stuff = Stuff.objects.all().order_by('-updated_at')
            return render(request, 'erp/home.html', {'all_stuff': all_stuff})
        else:
            return redirect('/sign-in')
    elif request.method == 'POST':
        pass


def detailed_erp(request, id):
    pass