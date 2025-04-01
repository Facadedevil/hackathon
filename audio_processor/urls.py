from django.urls import path
from . import views

app_name = 'audio_processor'
urlpatterns = [
    path('generate-summary/', views.generate_summary, name='generate_summary'),
]