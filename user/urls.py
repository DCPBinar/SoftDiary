from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView
from .views import RedirectView
from .forms import UserLoginForm

urlpatterns = [
    path('login/',
         CustomLoginView.as_view(template_name='register/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='register/logout.html'),
         name='logout'),
    path('', RedirectView.as_view(), name='redirect'),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
]
