# pages/views.py
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('<h1 style="color:#f25;">Hello, World!</h1>')