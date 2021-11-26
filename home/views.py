from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'home.html'

    def post(self, request):
        return HttpResponseRedirect('/')
