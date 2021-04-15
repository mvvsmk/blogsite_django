from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login {username}! ')
            return redirect('users-login')
    else: 
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form })

@login_required #implimets authorisation
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form' : u_form,
        'p_form' : p_form       
    }

    return render(request, 'users/profile.html',context)
