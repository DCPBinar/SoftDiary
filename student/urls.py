from django.urls import path
from .views import ProfileView, TestView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='student_profile'),
    path('profile/test', TestView.as_view(), name='test')
]