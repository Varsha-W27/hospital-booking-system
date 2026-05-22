from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Appointment


# Home Page
def home(request):

    return render(request, 'home.html')


# Login Page
from django.contrib import messages
from django.contrib.auth import authenticate, login


def login_user(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/')

        else:

            messages.error(
                request,
                'Invalid username or password'
            )

    return render(request, 'login.html')


# Book Appointment
@login_required
def book_appointment(request):

    if request.method == 'POST':

        doctor_name = request.POST['doctor_name']

        appointment_date = request.POST['appointment_date']

        appointment_time = request.POST['appointment_time']

        Appointment.objects.create(
            user=request.user,
            doctor_name=doctor_name,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        )

        return render(request, 'success.html')

    return render(request, 'book.html')
from django.contrib.auth import logout

def logout_user(request):

    logout(request)

    return redirect('/')

@login_required
def my_appointments(request):

    appointments = Appointment.objects.filter(
        user=request.user
    )

    return render(
        request,
        'my_appointments.html',
        {'appointments': appointments}
    )
    
from django.shortcuts import get_object_or_404

@login_required
def cancel_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id,
        user=request.user
    )

    appointment.delete()

    return redirect('/myappointments/')
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signup_user(request):

    if request.method == 'POST':

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('/')

    return render(request, 'signup.html')