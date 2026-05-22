from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),

    path('book/', views.book_appointment),

    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('myappointments/', views.my_appointments),
    path(
    'cancel/<int:id>/',
    views.cancel_appointment,
    name='cancel_appointment'
),
    path('signup/', views.signup_user),
]