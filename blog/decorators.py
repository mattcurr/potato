from django.http import HttpResponsePermanentRedirect
from google.appengine.api import users

def login_required(func):
    def _wrapper(request, *args, **kwargs):
        user = users.get_current_user()
        
        if user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponsePermanentRedirect(users.create_login_url(request.get_full_path()))

    return _wrapper

