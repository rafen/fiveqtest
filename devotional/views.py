# -*- coding: utf-8 -*-
from django.shortcuts import render

from models import Devotional


def list_devotionals(request):
    """
    Return the list of devotional
    If a date is give by GET parameter filter by that date
    """
    date = request.GET.get('date')
    if date:
        devotionals = Devotional.objects.filter(date=date)
    else:
        devotionals = Devotional.objects.all().order_by('-date')

    context = {
        'devotionals': devotionals,
        'date': date,
    }

    return render(request, 'devotional/list_devotionals.html', context)
