from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext



def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('home.html',
                             context_instance=context)

def login(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response('registration/login.html', context_instance=context)

def create_account(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response('registration/create_account.html', context_instance=context)