from django.contrib.auth.models import User
from django.core.urlresolvers import NoReverseMatch
from django.shortcuts import render, redirect, render_to_response
from django.template.context import RequestContext
from photoshare.forms import UserProfileForm, NewCircleForm
from photoshare.models import Group, GroupRoleUser


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

def profile(request):
    context = RequestContext(request,
                        {'request': request,
                            'user': request.user})
    grus = GroupRoleUser.objects.all()
    circles = []
    for gru in grus:
        if gru.user == request.user:
            circles.append(gru)
    data = {"full_name": request.user.userprofile.full_name, "email": request.user.userprofile.email, "circles": circles}
    return render(request, "registration/profile.html", data)


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
            try:
                return redirect(request.POST.get('next','/'))
            except NoReverseMatch:
                return redirect('/', context_instance=context)
        else:
            data["warning"] = True
            return render(request, "registration/edit_profile.html", data)
    else:
        return render(request, "registration/edit_profile.html", data)

def new_circle(request):
    context = RequestContext(request,
                        {'request': request,
                            'user': request.user})
    grus = GroupRoleUser.objects.all()
    circles = []
    for gru in grus:
        if gru.user == request.user:
            circles.append(gru)
    data = { "new_circle_form": NewCircleForm(), "full_name": request.user.userprofile.full_name, "email": request.user.userprofile.email, "circles": circles}
    if request.method == "POST":
        form = NewCircleForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],)
            new_user.save()
            profile = new_user.userprofile
            profile.full_name = form.cleaned_data['full_name']
            profile.save()
            group = Group(name = form.cleaned_data['full_name'], viewer = new_user)
            group.save()
            gru = GroupRoleUser(role = 'ADM', group = group, user = request.user)
            gru.save()
            return redirect('/profile/', context_instance=context)
        else:
            data["warning"] = True
            return render(request, "registration/new_circle.html", data)
    else:
        return render(request, "registration/new_circle.html", data)