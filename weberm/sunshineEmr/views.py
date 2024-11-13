from django.http import HttpResponse


def index(request):
    data = {"content": "Gfg is the best"}
    return render(request, "index.html", data)