from datetime import date
from django.conf import settings
from django.shortcuts import render
# from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP


def home(request):
    dt = settings.WEDDING_DATE_DATETIME_UTC
    wedding_date_datetime = {
        'year': dt.year,
        'month': dt.month,
        'day': dt.day,
        'hour': dt.hour,
        'minute': dt.minute
    }
    is_wedding_week = date.today().isocalendar()[1] == dt.isocalendar()[1]
    return render(request, 'home.html', context={
        # 'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP,
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'website_url': settings.WEDDING_WEBSITE_URL,
        'couple_name': settings.BRIDE_AND_GROOM,
        'wedding_location': settings.WEDDING_LOCATION,
        'wedding_date': settings.WEDDING_DATE,
        'wedding_date_datetime': wedding_date_datetime,
        'is_wedding_week': is_wedding_week
    })
