from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Teacher
from django.contrib.auth import logout


def index(request):
    return render(request, "teacher_438/index.html")


@login_required
def profile(request):
    return render(request, "/teacher_438/profile.html")


def logout_view(request):
    logout(request)
    return redirect("/teacher_438/profile.html")
# Create your views here.
