from django.urls import path
from .views import ProfileView, StudentDetail, GradeView, SuccessView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='teacher_profile'),
    path('profile/grade=<int:grade_id>', GradeView.as_view(), name='grade'),
    path('profile/student/id=<int:pk>', StudentDetail.as_view(), name='student_statistic'),
    path('profile/student/success', SuccessView.as_view(), name='success')
]