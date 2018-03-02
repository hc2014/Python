from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def show(request):
    from myblog import models
    if request.method=='POST':
        plan_code=request.POST['plan_code']
        plan_name=request.POST['plan_name']
        obj = models.TldTplanInfo(plan_code=plan_code, plan_name=plan_name)
        obj.save()

    plan_list=models.TldTplanInfo.objects.all()
    return render(request,"show.html",{'plan_list':plan_list})

@csrf_exempt
def deleteplan(request):
    from myblog import models
    plan_code = request.POST['plan_code']
    models.TldTplanInfo.objects.filter(plan_code=plan_code).delete()

    return HttpResponse("删除成功")


@csrf_exempt
def editplan(request):
    from myblog import models
    plan_code = request.POST['plan_code']
    plan_name = request.POST['plan_name']
    obj = models.TldTplanInfo.objects.get(plan_code=plan_code)
    obj.plan_name = plan_name
    obj.save()

    return HttpResponse("修改成功")