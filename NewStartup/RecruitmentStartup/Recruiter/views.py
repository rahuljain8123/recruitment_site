from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Job
# Create your views here.
def home(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        jobs = Job.objects.filter(title__icontains=search_query)
    else:
        jobs = Job.objects.all()
    return render(request, 'index.html', {'jobs': jobs})

def about_page(request):
    # Add any necessary context data here
    return render(request, 'about.html')
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')