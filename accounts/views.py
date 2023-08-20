from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.


def register_view(request):
    form = UserCreationForm(request. POST or None)

    if form. is_valid():
        user_obj = form. save()
        return redirect('/login')

    context = {"form": form}
    return render(request, "accounts/register.html", context)


def login_view(request):

    # login creado con AuthenticationForm

    # gonen : negonego
    # pimpa : *pimpollo09*

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)

    context = {"form": form}
    return render(request, "accounts/login.html", context)


""" login creado con authenticate 

def login_view(request):

    # if request.user.is_authenticated:
    #    return render(request, "accounts/already-logged-in.html", {})

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # remvoe this !!!
        # print(username, password)
        # remove this !!!

        user = authenticate(request, username=username, password=password)

        if user is None:

            context = {"error": "Invalid username or password."}
            return render(request, "accounts/login.html", context)

        login(request, user)
        return redirect('/admin')

    return render(request, "accounts/login.html", {})

"""


def logout_view(request):

    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})
