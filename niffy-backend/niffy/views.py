# coding=utf-8
import logging
import json
from datetime import datetime

from google.appengine.ext import ndb

from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.conf import settings

from .models import Invoice


def home(request):

    # TODO: dummy data
    invs = [{
        'business_name': 'Teaching InNovation',
        'total': u'456,23 €',
        'date': u'2016-10-06',
    }, {
        'business_name': 'Wild Fortress',
        'total': u'143.422,11 €',
        'date': u'2016-10-04',
    }, {
        'business_name': 'Continente',
        'total': u'45,51 €',
        'date': u'2016-10-01',
    }]

    return template_render(request, 'home.html', {
        'invoices': Invoice.query(),
    })


def json_response(func):
    """
    A decorator thats takes a view response and turns it
    into json. If a callback is added through GET or POST
    the response is JSONP.
    """
    def decorator(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        if isinstance(response, HttpResponse):
            return response
        elif isinstance(response, ndb.Model):
            return JsonResponse(response.to_json())
        elif isinstance(response, ndb.Query):
            return JsonResponse([e.to_json() for e in response], safe=False)
        else:
            return JsonResponse(response, safe=False)
    return decorator


@csrf_exempt
@json_response
def invoice_create(request):
    if request.method == 'POST':
        logging.info(request.body)
        d = json.loads(request.body)
        d['date'] = datetime.strptime(d['date'], '%Y-%m-%d').date()
        inv = Invoice(**d)
        inv.put()
        return inv

    return None


def template_render(request, tpl, params={}):
    return render(request, tpl, params)


# @json_response
# def persons(request):
#     return Person.query()


# @json_response
# def students(request):
#     # TODO:
#     org = Organization.query().get()
#     logging.info(org.key)
#     return Person.query_students(org.key)
