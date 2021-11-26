from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from .models import Student, Teacher


class RedirectView(TemplateView):
    def post(self, request):
        if request.user.is_superuser:
            return HttpResponseRedirect('/')
        elif Teacher.objects.filter(user=request.user).exists():
            return HttpResponseRedirect('teacher/profile/')
        elif Student.objects.filter(user=request.user).exists():
            return HttpResponseRedirect('student/profile/')
        else:
            return HttpResponse('Bad request')
