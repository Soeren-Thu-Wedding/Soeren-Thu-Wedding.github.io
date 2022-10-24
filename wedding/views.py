from django.conf import settings
from django.shortcuts import render


def home(request):
    dt = settings.WEDDING_DATE_DATETIME_UTC
    wedding_date_datetime = {
        'year': dt.year,
        'month': dt.month,
        'day': dt.day,
        'hour': dt.hour,
        'minute': dt.minute
    }
    return render(request, 'home.html', context={
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'website_url': settings.WEDDING_WEBSITE_URL,
        'couple_name': settings.BRIDE_AND_GROOM,
        'wedding_location': settings.WEDDING_LOCATION,
        'wedding_date': settings.WEDDING_DATE,
        'wedding_date_datetime': wedding_date_datetime,
    })
