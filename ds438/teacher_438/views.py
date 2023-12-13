from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Teacher

def index(request):
    return render(request, "teacher_438/index.html")

@login_required
def profile(request):
    return render(request, "teacher_438/profile.html")

# def login(request):
#     return render(request, "registration/login.html")

# Create your views here.
