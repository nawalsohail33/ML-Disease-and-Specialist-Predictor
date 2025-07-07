from django.urls import path
from .views import voice_diagnosis_view

urlpatterns = [
    path('', voice_diagnosis_view, name='voice_diagnosis'),
]

