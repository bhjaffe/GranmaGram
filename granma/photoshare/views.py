from django.shortcuts import render, redirect, render_to_response
from django.template.context import RequestContext
from photoshare.forms import UserProfileForm



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


def edit_profile(request):
    context = RequestContext(request,
                        {'request': request,
                            'user': request.user})
    data = { "profile_form": UserProfileForm(initial={'email': request.user.userprofile.email, 'full_name': request.user.userprofile.full_name})}
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            profile = request.user.userprofile
            profile.email = email
            profile.full_name = full_name
            profile.save()
            return redirect('/', context_instance=context)
    else:
        return render(request, "registration/edit_profile.html", data)
