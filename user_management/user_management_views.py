from django.shortcuts import render, redirect
from user_management.forms import CustomAuthForm 
from django.contrib.auth import login, logout

def login_view(request):
    form = CustomAuthForm()
    if request.method == 'POST':
        form = CustomAuthForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
