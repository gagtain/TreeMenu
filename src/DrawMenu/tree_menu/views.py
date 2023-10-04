from django.http import HttpRequest
from django.shortcuts import render
# Create your views here.

def index(request: HttpRequest, *args, **kwargs):
    print(args, kwargs)
    return render(request=request, template_name='tree_menu/index.html')