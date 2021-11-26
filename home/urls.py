from django.urls import path, include
from .views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name='home')
]