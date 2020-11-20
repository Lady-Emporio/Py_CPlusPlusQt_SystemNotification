# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse
import datetime
from django.db import connection
from django.http import JsonResponse
from .models import Notification,GroupNotification,NotificationState
from django.core import serializers
import json

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request,IsFilter):
    sql="""
      SELECT
 	    GroupNotification.id as GroupId,
 	    GroupNotification.name as GroupName,
	    Notification.id as NotId,
	    Notification.name as NotName,
	    NotificationState.name as NotStateName,
	    NotificationState.red as red,
	    NotificationState.green as green,
	    NotificationState.blue as blue,
	    NotificationState.back_red as back_red,
	    NotificationState.back_green as back_green,
	    NotificationState.back_blue as back_blue,
	    Notification.period as NotPeriod,
	    NotificationHistory.period as HistoryPeriod,
	    HistoryState.name as HistoryStateName
     FROM Notification
     LEFT JOIN GroupNotification
     ON GroupNotification.id=Notification.parent
     LEFT JOIN NotificationState
     ON NotificationState.id=Notification.state
      LEFT JOIN NotificationHistory
      ON NotificationHistory.notification=Notification.id
    LEFT JOIN NotificationState  as HistoryState
     ON HistoryState.id=NotificationHistory.state

        Par1qqqq1

    ORDER BY GroupNotification.id, Notification.id,NotificationHistory.period DESC
    """
    if IsFilter=="today":
        sql=sql.replace("Par1qqqq1"," WHERE date('now','start of month')=date(Notification.period ,'start of month') ")
    elif IsFilter=="active":
        sql=sql.replace("Par1qqqq1"," WHERE Notification.state=1 ")
    else:
        sql=sql.replace("Par1qqqq1","")
    data=[]
    with connection.cursor() as c:
        c.execute(sql)
        result=c.fetchall()

        colNombers={}
        for i in range(len(c.cursor.description)):
            colNombers[c.cursor.description[i][0]]=i

        """
        GroupData={
            "name":"",
            "id":-1,
            "quests":[],
        }
        questData={
            "name":"",
            "period":"",
            "state":"",
            "history":[],
        }
        historyData={
            "period":"ww",
            "state":"ww",
        }"""
        #Это может быть эта же группа, но добавить новую задачу
        #Это может быть эта же группа, но добавить новую историю к задаче
        #Это может быть новая группа.

        LastGroupId=-1
        LastNotId=-1

        for row in result:

            if  LastGroupId==row[colNombers["GroupId"]]:
                #Продолжается эта группа. Может быть новая задача в этой строке или новая история.
                if LastNotId==row[colNombers["NotId"]]:
                    # просто новая история
                    if "active"!=IsFilter:
                        __saveHistory(data,colNombers,row)
                else:
                    #Просто новая задача
                    LastNotId=row[colNombers["NotId"]]
                    __createNewQuest(data,colNombers,row)
                    if "active"!=IsFilter:
                        __saveHistory(data,colNombers,row)
            else:
                #Новая группа
                LastGroupId=row[colNombers["GroupId"]]
                __createNewGroup(data,colNombers,row)
                LastNotId=row[colNombers["NotId"]]
                __createNewQuest(data,colNombers,row)
                if "active"!=IsFilter:
                    __saveHistory(data,colNombers,row)

    return render(request,"mainPage.html",{"content":data,"filter":IsFilter})

# Получить список выполняемых задач
# Обновить задачу
# Создать задачу
@csrf_exempt
def api_active(request):
    #qs = Notification.objects.filter(state=1)
    #qs_json = serializers.serialize('json', qs,ensure_ascii=False)
    #return HttpResponse(qs_json, content_type='application/json')

    sql="""
    select
    Notification.id,
    Notification.name,
    GroupNotification.id,
    GroupNotification.name
    FROM Notification
    LEFT JOIN GroupNotification ON
    GroupNotification.id=Notification.parent
    WHERE Notification.state=1
    ORDER BY GroupNotification.id
    """
    data=[]
    with connection.cursor() as c:
        c.execute(sql)
        result=c.fetchall()
        for row in result:
            data.append({
            "NotId":row[0],
            "NotName":row[1],
            "GroupId":row[2],
            "GroupName":row[3],
            })
    qs_json = json.dumps(data, indent=4,ensure_ascii=False)
    return HttpResponse(qs_json, content_type='application/json')


from .forms import NotificationFormCreate,NotificationFormUpdate
from django.http import Http404
@csrf_exempt
def api_create(request):
    if request.method == 'POST':
        form = NotificationFormCreate(request.POST)
        if form.is_valid():
            GroupName = form.cleaned_data['GroupName']

            obj = Notification.objects.create()
            obj.name=form.cleaned_data['NotName'];
            if GroupName:
                parent=GroupNotification.objects.create()
                parent.name=GroupName
                parent.save()
                obj.parent=parent
            obj.save()
            return HttpResponse("Twilight")
    else:
        form = NotificationFormCreate()

    return render(request, "mainPage.html", {'form': form})

@csrf_exempt
def api_update(request,pk):
    try:
        obj = Notification.objects.get(pk=pk)
    except Notification.DoesNotExist:
        return HttpResponse("Model Notification not found.",status=404)

    if request.method == 'POST':
        form = NotificationFormUpdate(request.POST)
        if form.is_valid():
            StateId = form.cleaned_data['StateId']

            try:
                state = NotificationState.objects.get(pk=StateId)
            except NotificationState.DoesNotExist:
                return HttpResponse("Model NotificationState not found.",status=404)
            obj.state=state
            obj.period=datetime.datetime.now()
            obj.save()
            return HttpResponse("Twilight")
    else:
        qs_json = serializers.serialize('json', [obj,],ensure_ascii=False)
        return HttpResponse(qs_json, content_type='application/json')

    return render(request, "mainPage.html", {'form': form})

def __getThisGroup(data):
    return data[-1]

def __getThisQuest(data):
    return data[-1]["quests"][-1]

def __createNewGroup(data,colNombers,row):
    GroupData={
            "name":row[colNombers["GroupName"]],
            "id":row[colNombers["GroupId"]],
            "quests":[],
        }
    data.append(GroupData)

def __createNewQuest(data,colNombers,row):
    GroupData=__getThisGroup(data)

    questData={
            "name":row[colNombers["NotName"]],
            "period":row[colNombers["NotPeriod"]],
            "state":row[colNombers["NotStateName"]],
            "history":[],
    }
    for i in ["red","green","blue"]:
        val=row[colNombers[i]]
        questData[i]=val if val!=None else 255

    for i in ["back_red","back_green","back_blue"]:
        val=row[colNombers[i]]
        questData[i]=val if val!=None else 0

    GroupData["quests"].append(questData)

def __saveHistory(data,colNombers,row):
    historyData={
            "period":row[colNombers["HistoryPeriod"]],
            "state":row[colNombers["HistoryStateName"]],
    }
    nowQuetst=__getThisQuest(data)
    nowQuetst["history"].append(historyData)