from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Grade(models.Model):
    grade = models.IntegerField()

    def __str__(self):
        return f'{self.grade}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade_1 = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='g_1')
    grade_2 = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='g_2')
    grade_3 = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='g_3')
    grade_4 = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='g_4')
    grade_5 = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='g_5')

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    test_passed = models.BooleanField(default=False)
    teacher_1 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='t_1')
    teacher_2 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='t_2')
    teacher_3 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='t_3')
    teacher_4 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='t_4')
    teacher_5 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='t_5')
    teacher_6 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='t_6')
    teacher_7 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='t_7')
    teacher_8 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='t_8')
    teacher_9 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='t_9')
    teacher_10 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='t_10')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now())
    criteria_1 = models.CharField(max_length=1)  # Целеполагание
    criteria_2 = models.CharField(max_length=1)  # Мотивация
    criteria_3 = models.CharField(max_length=1)  # Планирование
    criteria_4 = models.CharField(max_length=1)  # Системное мышление
    criteria_5 = models.CharField(max_length=1)  # Аналитическое мышление
    criteria_6 = models.CharField(max_length=1)  # Генерация идей
    criteria_7 = models.CharField(max_length=1)  # Применение информации
    criteria_8 = models.CharField(max_length=1)  # Коммуникативные навыки
    criteria_9 = models.CharField(max_length=1)  # Командная работа


class TestMark(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    criteria_1 = models.CharField(max_length=1)  # Модальность
    criteria_2 = models.CharField(max_length=1)  # Воспроизведение
    criteria_3 = models.CharField(max_length=1)  # Внимание
    criteria_4 = models.CharField(max_length=1)  # Память
    criteria_5 = models.CharField(max_length=1)  # Темперамент

