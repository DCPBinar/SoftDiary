from django.contrib import admin
from .models import Student, Teacher, Grade, Mark

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Mark)