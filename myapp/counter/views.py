from django.shortcuts import HttpResponse, HttpResponseRedirect, render, loader, reverse

# global counter state
counter = 0

# Create your views here.


def index(request):
    template = loader.get_template("counter/index.html")
    global counter
    context = {"counter":  counter}
    return HttpResponse(template.render(context, request))

def plus(request):
    global counter
    counter += 1
    return HttpResponseRedirect(reverse("counter:index"))

def minus(request):
    global counter
    counter -= 1
    return HttpResponseRedirect(reverse("counter:index"))
