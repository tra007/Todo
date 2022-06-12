from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from . import forms
from .services import create_user
from .decorator import loginInSite


# Create your views here.
@loginInSite
def userLogin(request):
    if request.method == "POST":
        form = forms.loginForm(request.POST)
        if form.is_valid():
            cleanData = form.cleaned_data
            user = authenticate(request, username=cleanData["username"], password=cleanData["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "welcome.")
                    return redirect("Todo:HomePage")
                else:
                    messages.info(request, "your account banded.")
                    return redirect("User:Login")
            else:
                messages.error(request, "username or password incorrect.")
                return redirect("User:Login")

    else:
        form = forms.loginForm()
    return render(request, "profiles/login.html", {"form": form})


@loginInSite
def registerUser(request):
    if request.method == "POST":
        form = forms.registerForm(request.POST)
        if form.is_valid():
            cleanData = form.cleaned_data
            user = create_user(email=cleanData["email"], firstName=cleanData["name"], password=cleanData["password"])
            login(request, user)
            return redirect("Todo:HomePage")
        else:
            messages.error(request, "have some problem try later")
            return redirect("User:Register")
    else:
        form = forms.registerForm()
    return render(request, "profiles/register.html", {"form": form})
