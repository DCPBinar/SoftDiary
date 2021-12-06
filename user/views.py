from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate,   login
from django.contrib.auth.forms import AuthenticationForm
from .models import Student, Teacher
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')


class RedirectView(View):
    def post(self, request):
        if request.user.is_superuser:
            return HttpResponseRedirect('/')
        elif Teacher.objects.filter(user=request.user).exists():
            return HttpResponseRedirect('teacher/profile/')
        elif Student.objects.filter(user=request.user).exists():
            return HttpResponseRedirect('student/profile/')
        else:
            return HttpResponse('Bad request')
