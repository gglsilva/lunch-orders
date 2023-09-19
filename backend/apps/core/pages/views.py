from django.shortcuts import render, HttpResponse
from django.conf import settings
# Create your views here.
def core_home(request):
    print(f'\n{settings.TEMPLATES}\n' )
    return render(request, 'core/index.html')