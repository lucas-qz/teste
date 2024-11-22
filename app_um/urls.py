from django.urls import path
from . import views as vw
urlpatterns = [
    path('',vw.portfolio,name='portfolio'),  # MODELO DE URL
]