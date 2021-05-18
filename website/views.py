from django.shortcuts import render
import datetime


# Create your views here.
def base_page_view(request):
    return render(request, 'website/base.html')


def home_page_view(request):
    context = {
        'data': datetime.datetime.now()
    }
    return render(request, 'website/home.html', context)


def template_1_page_view(request):
    return render(request, 'website/template_1.html')


def template_2_page_view(request):
    return render(request, 'website/template_2.html')
