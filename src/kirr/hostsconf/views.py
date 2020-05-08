from django.conf import settings
from django.http import HttpResponseRedirect

DEFAULT_REDIRECT_URL = getattr(settings, 'DEFAULT_REDIRECT_URL')

def wildcard_redirect(request, path=None):
    newurl = DEFAULT_REDIRECT_URL

    if path is not None:
        newurl = DEFAULT_REDIRECT_URL + '/' + path

    return HttpResponseRedirect(newurl)