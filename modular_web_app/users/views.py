from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        # Check if input is email or username
        user = None
        if '@' in username_or_email:  # If it's an email address
            try:
                user = User.objects.get(email=username_or_email)
            except ObjectDoesNotExist:
                messages.error(request, "No user found with this email address.")
                return render(request, 'users/home.html')
        else:  # It's a username
            try:
                user = User.objects.get(username=username_or_email)
            except ObjectDoesNotExist:
                messages.error(request, "No user found with this username.")
                return render(request, 'users/home.html')

        # Authenticate user
        if user and user.check_password(password):
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid password.")
    
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'users/register.html')

        # Create the user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            # Optionally, store the phone number in the profile model
            # user.profile.phone = phone
            # user.profile.save()

            messages.success(request, 'Registration successful! Please log in.')
            return redirect('home')
        except Exception as e:
            messages.error(request, f"Error creating user: {str(e)}")

    return render(request, 'users/register.html')



def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, 'users/dashboard.html')


def logout(request):
    auth_logout(request)
    return redirect('home')



def quiz(request, topic):
    # For now, just render a template for the chosen topic
    return render(request, 'users/quiz.html', {'topic': topic})