from django.shortcuts import render
from django.http import HttpResponse
from .models import SmartphoneMadel


def get_madel(request):
    queryset = SmartphoneMadel.objects.only()
    print("\n", queryset.query)
    str_data = ""

    for i in queryset:
        str_data+=f"<li> {i}</li>"
    return HttpResponse(f"<ul> {str_data} </ul>")

