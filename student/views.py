from django.views.generic import TemplateView
from user.models import Mark
from django.db.models import Avg
import datetime


class ProfileView(TemplateView):
    template_name = 'student_profile.html'

    def get_context_data(self, **kwargs):
        template = {
            4: 'R',
            3: 'E',
            2: 'U',
            1: 'M'
        }

        time_template = {
            'morning': [datetime.time(6, 0, 0), datetime.time(12, 59, 59)],
            'day': [datetime.time(13, 0, 0), datetime.time(17, 59, 59)],
            'evening': [datetime.time(18, 0, 0), datetime.time(21, 59, 59)],
            'night': [datetime.time(22, 0, 0), datetime.time(23, 59, 59), datetime.time(0, 0, 0), datetime.time(5, 59, 59)]
        }
        context = super().get_context_data(**kwargs)

        mark = Mark.objects.filter(student_id=self.request.user.student.id)

        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time()

        if time_template['morning'][0] < current_time < time_template['morning'][1]:
            context['time'] = 'Доброе утро'
        elif time_template['day'][0] < current_time < time_template['day'][1]:
            context['time'] = 'Добрый день'
        elif time_template['evening'][0] < current_time < time_template['evening'][1]:
            context['time'] = 'Добрый вечер'
        elif time_template['night'][0] < current_time < time_template['night'][1] or time_template['night'][2] < current_time < time_template['night'][3]:
            context['time'] = 'Доброй ночи'

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

            context['chart_1'] = 'charts/' + username + '/1_' + str(len(mark)) + '.png'
            context['chart_2'] = 'charts/' + username + '/2_' + str(len(mark)) + '.png'
            context['chart_3'] = 'charts/' + username + '/3_' + str(len(mark)) + '.png'
            context['chart_4'] = 'charts/' + username + '/4_' + str(len(mark)) + '.png'
            context['chart_5'] = 'charts/' + username + '/5_' + str(len(mark)) + '.png'
            context['chart_6'] = 'charts/' + username + '/6_' + str(len(mark)) + '.png'
            context['chart_7'] = 'charts/' + username + '/7_' + str(len(mark)) + '.png'
            context['chart_8'] = 'charts/' + username + '/8_' + str(len(mark)) + '.png'
            context['chart_9'] = 'charts/' + username + '/9_' + str(len(mark)) + '.png'

            context['exist'] = True
        else:
            context['exist'] = False
        return context


class TestView(TemplateView):
    template_name = 'test.html'

    def post(self, request):
        pass