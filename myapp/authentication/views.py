from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse, HttpResponseRedirect, loader, reverse

# Create your views here.


def index(request):
    template = loader.get_template("authentication/index.html")
    context = dict()
    if request.user.is_authenticated:
        # return something like is authenticated as tom
        context["authenticated"] = "Authenticated as " + request.user.username
    else:
        context["authenticated"] = "Not authenticated"
    return HttpResponse(template.render(context, request))


def login_func(request):
    # django login the user by username and password
    username = request.POST["username"]
    password = request.POST["password"]
    # authenticate the user
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        # that is not the best way to handle that lol
        pass
    return HttpResponseRedirect(reverse("authentication:index"))
