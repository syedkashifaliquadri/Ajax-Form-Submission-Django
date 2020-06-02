from django.urls import path
from . import views


urlpatterns = [
	path('add_email/', views.add_email, name='add_email'),  # index view at /
]