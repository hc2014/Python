from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def show(request):
    from myblog import models
    plan_list=models.TldTplanInfo.objects.all()
    return render(request,"show.html",{'plan_list':plan_list})
