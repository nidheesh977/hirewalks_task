from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm
from .models import CustomUser

# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        print(request.POST)
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
        print(password)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("accounts:login")

        return redirect("/")

class SignupView(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("account:dashboard")
        form = SignupForm()
        return render(request, 'accounts/register.html', {'form': form})
    
    def post(self, request):
        form = SignupForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = CustomUser.objects.create(
                email = form.cleaned_data["email"],
                is_seller = form.cleaned_data["is_seller"]
            )
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect('/')
        return render(request, 'accounts/register.html', {'form': form, "values": request.POST})

def logout_view(request):
    logout(request)
    return redirect("accounts:login")