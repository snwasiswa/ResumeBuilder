from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegistrationForm, LoginForm, Profile, UserForm, UserProfileForm


# Create your views here.
def home(request):
    # View for the home page
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('contact'))

    return render(request, 'home.html')


def registration(request):
    """View for user registration"""
    form = RegistrationForm(request.POST or None)

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('home'))

    if request.method == 'POST':

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            group = Group.objects.get(name='Owners')
            # Add new user to Owners group
            user.groups.add(group)
            # Create Profile for new user
            Profile.objects.create(user=user)

            login(request, user)
            messages.success(request, 'Welcome! Your account has been successfully created')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})


def user_login(request):
    """ Login View for Instructors"""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('home'))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            credentials = form.cleaned_data
            user = authenticate(request, password=credentials['password'], username=credentials['username'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Welcome back, " + request.user.first_name + "! You are logged in as " +
                                     request.user.username + ".")
                    return redirect('home')
                else:
                    messages.info(request, 'You account has been disabled')
            else:
                messages.info(request, 'Your credentials are invalid')

    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout(request):
    """Custom Log out request"""

    logout(request)
    messages.success(request, 'You have successfully logged out from Resume Builder')
    return render(request, 'account/logout.html')


@login_required
def edit_profile(request):
    """View to edit profile"""
    if request.method == 'POST':
        form = UserForm(instance=request.user, data=request.POST)
        profile_form = UserProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.success(request, 'Profile has been successfully updated')
        else:
            messages.error(request, 'Error updating your profile')

    else:
        form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'account/edit_profile.html',
                  {'form': form, 'profile_form': profile_form})
