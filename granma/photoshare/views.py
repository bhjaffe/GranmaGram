from django.shortcuts import render, redirect, render_to_response
from django.template.context import RequestContext
from photoshare.forms import UserProfileForm
from models import UserProfile
from django.core.context_processors import csrf


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

def new_profile(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    # Check that user is logged in
    if request.user.is_authenticated():

        # If the user is submitting the form
        if request.method == "POST":

            # Get the instance of the form filled with the submitted data
            form = UserProfileForm(request.POST)

            # Django will check the form's validity for you
            if form.is_valid():

                # Saving the form will create a new profile object
                if form.save():

                    # After saving, redirect the user back to the index page
                    return redirect('/', context_instance=context)

        # Else if the user is looking at the form page
        else:
            form = UserProfileForm()
        data = {'form': form}
        return render(request, "registration/edit_profile.html", data)
    else:
        return redirect('/', context_instance=context)

def edit_profile(request):
    # Similar to the the detail view, we have to find the existing profile we are editing
    profile = request.user.userprofile

    # We still check to see if we are submitting the form
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            if form.save():
                return redirect("/profiles/{}".format(profile_id))

    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = UserProfileForm(instance=profile)
    data = {"profile": profile, "form": form}
    return render(request, "registration/edit_profile.html", data)