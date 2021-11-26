from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from user.models import Student, Grade, Mark
from django.db.models import Avg
import plotly.express as px
from statistics import mean
import pandas as pd
import os
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
        self.request.session['grade_id'] = grade_id
        context['students'] = students
        context['grade'] = grade

        try:
            os.mkdir(f'static/charts/{grade.grade}')
        except Exception:
            pass

        data_1 = []

        for i in students:
            a = []
            mark = Mark.objects.filter(student_id=i.id)
            a.append(round(mark.aggregate(Avg('criteria_1'))['criteria_1__avg']))
            a.append(round(mark.aggregate(Avg('criteria_2'))['criteria_2__avg']))
            a.append(round(mark.aggregate(Avg('criteria_3'))['criteria_3__avg']))
            a.append(round(mark.aggregate(Avg('criteria_4'))['criteria_4__avg']))
            a.append(round(mark.aggregate(Avg('criteria_5'))['criteria_5__avg']))
            a.append(round(mark.aggregate(Avg('criteria_6'))['criteria_6__avg']))
            a.append(round(mark.aggregate(Avg('criteria_7'))['criteria_7__avg']))
            a.append(round(mark.aggregate(Avg('criteria_8'))['criteria_8__avg']))
            a.append(round(mark.aggregate(Avg('criteria_9'))['criteria_9__avg']))
            data_1.append(a)

        data = []

        for i in range(len(data_1)):
            a = []
            b = []

            if i == 1:
                break

            n = len(data_1)

            for j in range(n):
                b.append(data_1[j - 1][0])
            a.append(round(mean(b)))
            b.clear()

            for j in range(n):
                b.append(data_1[j - 1][1])
            a.append(round(mean(b)))
            b.clear()

            for j in range(n):
                b.append(data_1[j - 1][2])
            a.append(round(mean(b)))
            b.clear()

            for j in range(n):
                b.append(data_1[j - 1][3])
            a.append(round(mean(b)))
            b.clear()

            for j in range(n):
                b.append(data_1[j - 1][4])
            a.append(round(mean(b)))
            b.clear()

            for j in range(n):
                b.append(data_1[j - 1][5])
            a.append(round(mean(b)))
            b.clear()

            for j in range(n):
                b.append(data_1[j - 1][6])
            a.append(round(mean(b)))
            b.clear()

            for j in range(n):
                b.append(data_1[j - 1][7])
            a.append(round(mean(b)))
            b.clear()

            for j in range(n):
                b.append(data_1[j - 1][8])
            a.append(round(mean(b)))
            b.clear()

            data = a

        print(data)

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


        return context


class StudentDetail(DetailView):
    model = Student
    template_name = 'student.html'

    def get_context_data(self, **kwargs):
        student = Student.objects.get(id=self.kwargs['pk'])
        username = student.user.username
        previous = datetime.datetime(2000, 1, 1, 1, 1, 1)
        next = datetime.datetime(2022, 1, 1, 1, 1, 1)
        is_time = True

        # АЛГОРИТМ ПРОВЕРКИ ВРЕМЕНИ

        context = super().get_context_data(**kwargs)

        self.request.session['student_id'] = student.id
        context['student'] = student

        if Mark.objects.filter(student_id=self.kwargs['pk']).exists():
            context['stat'] = True
        else:
            context['stat'] = False

        context['grade_id'] = self.request.session.get('grade_id', None)
        context['is_time'] = is_time

        username = student.user.username
        mark = Mark.objects.filter(student_id=student.id)

        try:
            os.mkdir(f'static/charts/{username}')
        except Exception:
            pass

        if next > datetime.datetime.now() > previous:
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

        context['chart_1'] = 'charts/' + username + '/1.png'
        context['chart_2'] = 'charts/' + username + '/2.png'
        context['chart_3'] = 'charts/' + username + '/3.png'
        context['chart_4'] = 'charts/' + username + '/4.png'
        context['chart_5'] = 'charts/' + username + '/5.png'
        context['chart_6'] = 'charts/' + username + '/6.png'
        context['chart_7'] = 'charts/' + username + '/7.png'
        context['chart_8'] = 'charts/' + username + '/8.png'
        context['chart_9'] = 'charts/' + username + '/9.png'

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
