from django.http import HttpResponse
from django.shortcuts import render
from nigerian_only.decorator import whitelisted_country_only

# Create your views here.

def home(request):
    return HttpResponse('Hello, welcome to the homepage')


@whitelisted_country_only
def protected_view(request):
    return HttpResponse('Hello, This view is only for users from Nigerian')


def custom_403_view(request, exception):
    return render(request, 'test_app/403.html', status=403)