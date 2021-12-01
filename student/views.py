from django.views.generic import TemplateView
from user.models import Mark
from django.db.models import Avg


class ProfileView(TemplateView):
    template_name = 'student_profile.html'

    def get_context_data(self, **kwargs):
        template = {
            4: 'R',
            3: 'E',
            2: 'U',
            1: 'M'
        }
        context = super().get_context_data(**kwargs)

        mark = Mark.objects.filter(student_id=self.request.user.student.id)

        if Mark.objects.filter(student_id=self.request.user.student.id).exists():
            criteria_1 = mark.aggregate(Avg('criteria_1'))
            criteria_1 = criteria_1['criteria_1__avg']
            context['avg_0'] = template[round(criteria_1)]

            criteria_2 = mark.aggregate(Avg('criteria_2'))
            criteria_2 = criteria_2['criteria_2__avg']
            context['avg_1'] = template[round(criteria_2)]

            criteria_3 = mark.aggregate(Avg('criteria_3'))
            criteria_3 = criteria_3['criteria_3__avg']
            context['avg_2'] = template[round(criteria_3)]

            criteria_4 = mark.aggregate(Avg('criteria_4'))
            criteria_4 = criteria_4['criteria_4__avg']
            context['avg_3'] = template[round(criteria_4)]

            criteria_5 = mark.aggregate(Avg('criteria_5'))
            criteria_5 = criteria_5['criteria_5__avg']
            context['avg_4'] = template[round(criteria_5)]

            criteria_6 = mark.aggregate(Avg('criteria_6'))
            criteria_6 = criteria_6['criteria_6__avg']
            context['avg_5'] = template[round(criteria_6)]

            criteria_7 = mark.aggregate(Avg('criteria_7'))
            criteria_7 = criteria_7['criteria_7__avg']
            context['avg_6'] = template[round(criteria_7)]

            criteria_8 = mark.aggregate(Avg('criteria_8'))
            criteria_8 = criteria_8['criteria_8__avg']
            context['avg_7'] = template[round(criteria_8)]

            criteria_9 = mark.aggregate(Avg('criteria_9'))
            criteria_9 = criteria_9['criteria_9__avg']
            context['avg_8'] = template[round(criteria_9)]

            username = self.request.user.username

            context['chart_1'] = 'charts/' + username + '/1.png'
            context['chart_2'] = 'charts/' + username + '/2.png'
            context['chart_3'] = 'charts/' + username + '/3.png'
            context['chart_4'] = 'charts/' + username + '/4.png'
            context['chart_5'] = 'charts/' + username + '/5.png'
            context['chart_6'] = 'charts/' + username + '/6.png'
            context['chart_7'] = 'charts/' + username + '/7.png'
            context['chart_8'] = 'charts/' + username + '/8.png'
            context['chart_9'] = 'charts/' + username + '/9.png'

            context['exist'] = True
        else:
            context['exist'] = False
        return context


class TestView(TemplateView):
    template_name = 'test.html'

    def post(self, request):
        pass