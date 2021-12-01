from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from user.models import Student, Grade, Mark
from django.db.models import Avg
import plotly.express as px
import pandas as pd
import os
import numpy as np
from itertools import zip_longest
import datetime


class ProfileView(ListView):
    model = Grade
    template_name = 'teacher_profile.html'
    context_object_name = 'grades'


class GradeView(ListView):
    model = Student
    template_name = 'grade.html'

    def get_context_data(self, **kwargs):
        grade_id = self.kwargs['grade_id']
        grade = Grade.objects.get(id=grade_id)
        students = Student.objects.filter(grade_id=grade_id)
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
                mark = Mark.objects.filter(student_id=i.id)
                a = [round(mark.aggregate(Avg(f'criteria_{i}'))[f'criteria_{i}__avg']) for i in range(1, 10)]
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
            chart.write_image(f'static/charts/{grade.grade}/1.png')

            context['chart_avg'] = '/charts/' + str(grade.grade) + '/1.png'

        else:
            context['avg_exist'] = False

        return context


class StudentDetail(DetailView):
    model = Student
    template_name = 'student.html'

    def get_context_data(self, **kwargs):
        student = Student.objects.get(id=self.kwargs['pk'])
        username = student.user.username

        context = super().get_context_data(**kwargs)

        self.request.session['student_id'] = student.id
        context['student'] = student

        if Mark.objects.filter(student_id=self.kwargs['pk']).exists():
            context['stat'] = True
            username = student.user.username
            mark = Mark.objects.filter(student_id=student.id)

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
            chart.write_image(f'static/charts/{username}/1.png')

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
            chart.write_image(f'static/charts/{username}/2.png')

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
            chart.write_image(f'static/charts/{username}/3.png')

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
            chart.write_image(f'static/charts/{username}/4.png')

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
            chart.write_image(f'static/charts/{username}/5.png')

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
            chart.write_image(f'static/charts/{username}/6.png')

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
            chart.write_image(f'static/charts/{username}/7.png')

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
            chart.write_image(f'static/charts/{username}/8.png')

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
            chart.write_image(f'static/charts/{username}/9.png')
        else:
            context['stat'] = False

        context['chart_1'] = 'charts/' + username + '/1.png'
        context['chart_2'] = 'charts/' + username + '/2.png'
        context['chart_3'] = 'charts/' + username + '/3.png'
        context['chart_4'] = 'charts/' + username + '/4.png'
        context['chart_5'] = 'charts/' + username + '/5.png'
        context['chart_6'] = 'charts/' + username + '/6.png'
        context['chart_7'] = 'charts/' + username + '/7.png'
        context['chart_8'] = 'charts/' + username + '/8.png'
        context['chart_9'] = 'charts/' + username + '/9.png'

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
