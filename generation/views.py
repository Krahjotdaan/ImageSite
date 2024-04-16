from django.shortcuts import render, redirect
from generation.forms import *


number = 0
style = ""
format = ""
quality = ""

def home(request):
    context = {}
    if request.method == 'POST':
        form = StyleForm(request.POST)

        number = form.data['number_of_images']
        style = form.data['style']
        format = form.data['format']
        quality = form.data['quality'] + ', качество'

        return redirect("home.html")
    
    else:
        context['form'] = StyleForm()
        return render(request, 'home.html', context)