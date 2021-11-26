from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import RedirectView
from .forms import UserLoginForm

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='register/login.html', authentication_form=UserLoginForm),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='register/logout.html'),
         name='logout'),
    path('', RedirectView.as_view(), name='redirect'),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
]
