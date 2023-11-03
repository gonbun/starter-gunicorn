from django.shortcuts import render, redirect

from django.utils import timezone
from .models import CalendarSchedule
from django.conf import settings
import datetime
import boto3
import investpy

dynamodb = boto3.resource('dynamodb', region_name=settings.AWS_REGION)
db = dynamodb.Table(settings.CYCLIC_DB)


# Create your views here.

def index(request):
    context = db.scan(
    )
    # print(context)
    # context = addCalendar('1/11/2023','5/11/2023')

    return render(request, 'calendar/index.html', context)


def delete_all():

    # context = db.get_item(TableName='splendid-puce-coyoteCyclicDB',Key={'pk': "485867", 'sk': "31/10/2023"})
    context = db.scan(
    )
    print(context)
    # context = {'messages': "hello"}
    # context = addCalendar('31/10/2023','1/11/2023')
    for x in context['Items']:
        deleteCalendar(x)
    # return render(request, 'calendar/index.html', context)


def addCalendar(from_date, to_date):
    economic_data = investpy.economic_calendar(time_zone='GMT +9:00', countries=['japan', 'united states'],
                                               from_date=from_date, to_date=to_date)
    for x, data in economic_data.iterrows():
        db.put_item(
            TableName='splendid-puce-coyoteCyclicDB',
            Item={
                'pk': str(data.date),
                'sk': str(data.id),
                'time': str(data.time),
                'zone': str(data.zone),
                'currency': data.currency,
                'importance': data.importance,
                'event': data.event,
                'actual': data.actual,
                'forecast': data.forecast,
                'previous': data.previous,
                'updated_at': str(datetime.datetime.today())
            }
        )
    item = db.get_item(TableName='splendid-puce-coyoteCyclicDB', Key={'pk': "485867", 'sk': "31/10/2023"})
    return item


def deleteCalendar(obj):
    print(obj)
    item = db.delete_item(Key={'pk': obj["pk"], 'sk': obj["sk"]})
    print("deleted...")
