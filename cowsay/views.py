from django.shortcuts import render

# Create your views here.
from cowsay.models import Cowsay
from cowsay.forms import CowsayForm
import subprocess

def index(request):
    if request.method == "POST":
        new_input = CowsayForm()
        form = CowsayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Cowsay.objects.create(
                input=data.get('input')
            )
            cow = subprocess.run(
                ['cowsay', data['input']], capture_output=True
            ).stdout.decode("utf-8")
            return render(request, "index.html", {'form': new_input, 'cow': cow})
                  
    form = CowsayForm()
    return render(request, "index.html", {"title": "Welcome to Cowsay!", "form": form})
    
def history(request):
    cowsay_history = Cowsay.objects.order_by('-id')[:10]
    return render(request, 'history.html', {'cowsay_history': cowsay_history})