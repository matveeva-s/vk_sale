from django.urls import path

import users.views as views

app_name = 'users'

urlpatterns = [
    path('me/', views.ProfileViewset.as_view(), name='profile'),
]
