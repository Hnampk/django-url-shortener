from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import KirrURL

# Create your views here.


def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    print("shortcode", shortcode)
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    
    return HttpResponseRedirect(obj.url)
    
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    #     obj_url = obj.url
    #     return HttpResponse("hello {sc}".format(sc=obj_url))
    # except:
        # return HttpResponse("Shortcode not found: {sc}".format(sc=shortcode))


class KirrClassBasedView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
