from google.appengine.api import users

def user_processor(request):
    user = users.get_current_user()
    context = {
        'user': user,
    }
    
    if user:
        context['logout_url'] = users.create_logout_url('/')
    else:
        context['login_url'] = users.create_login_url('')
    return context
