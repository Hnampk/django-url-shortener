from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    return HttpResponse("hello {sc}".format(sc=shortcode))

class KirrClassBasedView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse("hello again {sc}".format(sc=shortcode))

