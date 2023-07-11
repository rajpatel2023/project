from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Usersignup, userprofileform
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Profile
from django.contrib.auth.models import User


# Create your views here.
class home(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.request.user)
        data = Profile.objects.filter(user=user).values()
        return render(request, "user/home.html", {"data": data})


class profile(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.request.user)
        data = Profile.objects.get(user=user)
        form = userprofileform(instance=data)
        return render(request, "user/profile.html", {"form": form})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=self.request.user)
        instance = Profile.objects.get(user=user)
        form = userprofileform(request.POST, instance=instance)
        import pdb

        pdb.set_trace()
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(
                request, "user/profile.html", {"form": form, "error": form.error}
            )


class signup(View):
    def get(self, request, *args, **kwargs):
        form = Usersignup()
        return render(request, "user/signup.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = Usersignup(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(
                request, "user/signup.html", {"form": form, "error": form.error}
            )


def signup(request):
    if request.method == "POST":
        form = Usersignup(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            return redirect("home")

    else:
        form = Usersignup()
    return render(request, "user/signup.html", {"form": form})
