from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from .models import ListToDo, DateTime
from .decorators import require_ajax


# Create your views here.
@login_required
def homePage(request):
    today = date.today()
    user = request.user
    try:
        yesterdayDateQuery = DateTime.manage.get_queryset_user(user).get(time=today - timedelta(days=1))
    except ObjectDoesNotExist:
        yesterdayDateQuery = None
    todayDateQuery, created = DateTime.objects.get_or_create(time=today, owner=user)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.POST:
        tomorrow, creat = DateTime.objects.get_or_create(owner=user, time=today + timedelta(days=1))
        return JsonResponse({"id": tomorrow.id}, status=200)
    return render(request, "todo/homPage.html", {"yesterday": yesterdayDateQuery, "today": todayDateQuery, })


@login_required
def detail(request, id):
    user = request.user
    getDay = get_object_or_404(DateTime, pk=id, owner=user)
    todayInfo = getDay.listtodo_set.all().order_by("start")
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.POST:
        item = request.POST
        if item["startH"]:
            startMinutes = item["startM"] if item["startM"] else "00"
            startTime = f'{item["startH"]}:{startMinutes}'
        else:
            startTime = None

        if item["finishH"]:
            finishMinutes = item["finishM"] if item["finishM"] else "00"
            finishTime = f'{item["finishH"]}:{finishMinutes}'
        else:
            finishTime = None
        newJob = todayInfo.create(date=getDay, job=item["job"], start=startTime,
                                  finish=finishTime)
        newJob.save()
        t = render_to_string('items.html', {'item': newJob})
        return JsonResponse({"data": t}, status=200)
    return render(request, "todo/detail.html", {"todo": todayInfo, "day": getDay})


@login_required
@require_ajax
@require_POST
def changeStatus(request):
    user = request.user
    itemID = int(request.POST.get("id"))
    try:
        item = ListToDo.objects.get(id=itemID, date__owner=user)
        if item.don:
            item.don = False
        else:
            item.don = True
        item.save()
        return JsonResponse({"status": "ok"})
    except ObjectDoesNotExist:
        return JsonResponse({"status": "cant do this"})


@login_required
@require_ajax
@require_POST
def deleteJob(request):
    user = request.user
    itemID = int(request.POST.get("id"))
    try:
        item = ListToDo.objects.get(id=itemID, date__owner=user)
        id = item.id
        item.delete()
        return JsonResponse({"id": id})
    except ObjectDoesNotExist:
        return JsonResponse({"status": "cant do this"})
