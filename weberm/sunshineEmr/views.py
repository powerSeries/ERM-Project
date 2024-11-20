from django.shortcuts import render

def index(request):
    data = {"content": "Gfg is the best"}
    return render(request, "index.html", data)