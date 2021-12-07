from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from user.models import Student, Grade, Mark
from django.db.models import Avg
import plotly.express as px
import pandas as pd
import os
import datetime
import numpy as np
from itertools import zip_longest


class ProfileView(ListView):
    template_name = 'teacher_profile.html'
    model = Grade

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        time_template = {
            'morning': [datetime.time(6, 0, 0), datetime.time(12, 59, 59)],
            'day': [datetime.time(13, 0, 0), datetime.time(17, 59, 59)],
            'evening': [datetime.time(18, 0, 0), datetime.time(21, 59, 59)],
            'night': [datetime.time(22, 0, 0), datetime.time(23, 59, 59), datetime.time(0, 0, 0), datetime.time(5, 59, 59)]
        }

        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time()

        if time_template['morning'][0] < current_time < time_template['morning'][1]:
            context['time'] = 'Доброе утро'
        elif time_template['day'][0] < current_time < time_template['day'][1]:
            context['time'] = 'Добрый день'
        elif time_template['evening'][0] < current_time < time_template['evening'][1]:
            context['time'] = 'Добрый вечер'
        elif time_template['night'][0] < current_time < time_template['night'][1] or time_template['night'][2] < \
                current_time < time_template['night'][3]:
            context['time'] = 'Доброй ночи'


        context['grades'] = Grade.objects.all()

        return context


class GradeView(ListView):
    model = Student
    template_name = 'grade.html'

    def get_context_data(self, **kwargs):
        grade_id = self.kwargs['grade_id']
        grade = Grade.objects.get(id=grade_id)
        students = Student.objects.filter(grade_id=grade_id)
        mark = Mark.objects.all()
        context = super().get_context_data(**kwargs)
        context['avg_exist'] = True
        self.request.session['grade_id'] = grade_id
        context['students'] = students
        context['grade'] = grade

        flag = 1

        for i in students:
            if not Mark.objects.filter(student_id=i.id).exists():
                flag = 0
                break

        if flag == 1:
            try:
                os.mkdir(f'static/charts/{grade.grade}')
            except Exception:
                pass

            dry_data = []

            for i in students:
                mark_1 = Mark.objects.filter(student_id=i.id)
                a = [round(mark_1.aggregate(Avg(f'criteria_{i}'))[f'criteria_{i}__avg']) for i in range(1, 10)]
                dry_data.append(a)
            data = [round(np.ma.average(i)) for i in zip_longest(*dry_data)]

            df = pd.DataFrame(dict(
                r=data,
                theta=['Целеполагание', 'Мотивация', 'Планирование',
                       'Системное мышление', 'Аналитическое мышление',
                       'Генерация идей', 'Применение информации',
                       'Коммуникативные навыки', 'Командная работа']))
            chart = px.line_polar(df, r='r', theta='theta', line_close=True, )
            chart.update_traces(fill='toself')

            chart.write_image(f'static/charts/' + str(grade.grade) + '/' + str(len(mark)) + '.png')

            context['chart_avg'] = '/charts/' + str(grade.grade) + '/' + str(len(mark)) + '.png'

        else:
            context[' '] = False

        return context


class StudentDetail(DetailView):
    model = Student
    template_name = 'student.html'

    def get_context_data(self, **kwargs):

        # TODO Очистка папки

        student = Student.objects.get(id=self.kwargs['pk'])
        username = student.user.username

        context = super().get_context_data(**kwargs)

        self.request.session['student_id'] = student.id
        context['student'] = student
        mark = Mark.objects.filter(student_id=self.kwargs['pk'])
        if mark.exists():
            context['stat'] = True
            username = student.user.username

            try:
                os.mkdir(f'static/charts/{username}')
            except Exception:
                pass

            x = []
            y = []
            for i in mark:
                x.append(i.date)
                y.append(i.criteria_1)

            y = [int(i) for i in y]

            chart = px.line(x=x,
                            y=y,
                            title='Целеполагание',
                            labels=dict(x='Дата', y='REUM'))
            chart.write_image(f'static/charts/{username}/1_{len(mark)}.png')

            # Мотивация

            x.clear()
            y.clear()
            for i in mark:
                x.append(i.date)
                y.append(i.criteria_2)

            y = [int(i) for i in y]

            chart = px.line(x=x,
                            y=y,
                            title='Мотивация',
                            labels=dict(x='Дата', y='REUM'))
            chart.write_image(f'static/charts/{username}/2_{len(mark)}.png')

            # Планирование

            x.clear()
            y.clear()

            for i in mark:
                x.append(i.date)
                y.append(i.criteria_3)

            y = [int(i) for i in y]

            chart = px.line(x=x,
                            y=y,
                            title='Планирование',
                            labels=dict(x='Дата', y='REUM'))
            chart.write_image(f'static/charts/{username}/3_{len(mark)}.png')

            # Системное мышление

            x.clear()
            y.clear()

            for i in mark:
                x.append(i.date)
                y.append(i.criteria_4)

            y = [int(i) for i in y]

            chart = px.line(x=x,
                            y=y,
                            title='Системное мышление',
                            labels=dict(x='Дата', y='REUM'))
            chart.write_image(f'static/charts/{username}/4_{len(mark)}.png')

            # Аналитическое мышление

            x.clear()
            y.clear()

            for i in mark:
                x.append(i.date)
                y.append(i.criteria_5)

            y = [int(i) for i in y]

            chart = px.line(x=x,
                            y=y,
                            title='Аналитическое мышление',
                            labels=dict(x='Дата', y='REUM'))
            chart.write_image(f'static/charts/{username}/5_{len(mark)}.png')

            # Генерация идей

            x.clear()
            y.clear()

            for i in mark:
                x.append(i.date)
                y.append(i.criteria_6)

            y = [int(i) for i in y]

            chart = px.line(x=x,
                            y=y,
                            title='Системное мышление',
                            labels=dict(x='Дата', y='REUM'))
            chart.write_image(f'static/charts/{username}/6_{len(mark)}.png')

            # Применение информации

            x.clear()
            y.clear()

            for i in mark:
                x.append(i.date)
                y.append(i.criteria_7)

            y = [int(i) for i in y]

            chart = px.line(x=x,
                            y=y,
                            title='Применение информации',
                            labels=dict(x='Дата', y='REUM'))
            chart.write_image(f'static/charts/{username}/7_{len(mark)}.png')

            # Коммуникативные навыки

            x.clear()
            y.clear()

            for i in mark:
                x.append(i.date)
                y.append(i.criteria_8)

            y = [int(i) for i in y]

            chart = px.line(x=x,
                            y=y,
                            title='Коммуникативные навыки',
                            labels=dict(x='Дата', y='REUM'))
            chart.write_image(f'static/charts/{username}/8_{len(mark)}.png')

            # Командная работа

            x.clear()
            y.clear()

            for i in mark:
                x.append(i.date)
                y.append(i.criteria_9)

            y = [int(i) for i in y]

            chart = px.line(x=x,
                            y=y,
                            title='Командная работа',
                            labels=dict(x='Дата', y='REUM'))
            chart.write_image(f'static/charts/{username}/9_{len(mark)}.png')
        else:
            context['stat'] = False

        context['chart_1'] = 'charts/' + username + '/1_' + str(len(mark)) + '.png'
        context['chart_2'] = 'charts/' + username + '/2_' + str(len(mark)) + '.png'
        context['chart_3'] = 'charts/' + username + '/3_' + str(len(mark)) + '.png'
        context['chart_4'] = 'charts/' + username + '/4_' + str(len(mark)) + '.png'
        context['chart_5'] = 'charts/' + username + '/5_' + str(len(mark)) + '.png'
        context['chart_6'] = 'charts/' + username + '/6_' + str(len(mark)) + '.png'
        context['chart_7'] = 'charts/' + username + '/7_' + str(len(mark)) + '.png'
        context['chart_8'] = 'charts/' + username + '/8_' + str(len(mark)) + '.png'
        context['chart_9'] = 'charts/' + username + '/9_' + str(len(mark)) + '.png'

        context['grade_id'] = self.request.session.get('grade_id', None)

        return context


class SuccessView(View):

    def post(self, request):
        mark = Mark()
        if request.method == "POST":
            mark.student = Student.objects.get(id=self.request.session.get('student_id', None))
            mark.criteria_1 = request.POST['criteria_1']
            mark.criteria_2 = request.POST['criteria_2']
            mark.criteria_3 = request.POST['criteria_3']
            mark.criteria_4 = request.POST['criteria_4']
            mark.criteria_5 = request.POST['criteria_5']
            mark.criteria_6 = request.POST['criteria_6']
            mark.criteria_7 = request.POST['criteria_7']
            mark.criteria_8 = request.POST['criteria_8']
            mark.criteria_9 = request.POST['criteria_9']
            mark.save()
            return render(request, 'success.html')
