# coding=utf-8
import logging
import json
from datetime import datetime
import base64

from google.appengine.ext import ndb

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

import dripcil
from dripcil.gae_ndb import File
from .models import Invoice

import time
from dripcil.apns import APNs, Frame, Payload

import StringIO

from .jc_niffy import s


PDF_MIMETYPE = 'application/pdf'


def home(request):

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


def _parse_invoice(d):
    d['date'] = datetime.strptime(d['date'], '%Y-%m-%d').date()
    bin = None
    if 'file' in d:
        bin = d.get('file')
        if bin:
            bin = base64.b64decode(bin)
        del d['file']
    return d, bin


@csrf_exempt
@json_response
def invoice_create(request):
    if request.method == 'POST':
        params, bin = _parse_invoice(json.loads(request.body))

        if bin:
            f = File(data=bin, name=params.get('description'), mimetype=PDF_MIMETYPE)
            f.put()
            params['file_key'] = f.key

        inv = Invoice(**params)
        inv.put()
        return inv

    return None


def download(request, id):

    logging.info(id)

    f = File.get_by_id(long(id))

    response = HttpResponse(content_type=PDF_MIMETYPE)
    response['Content-Disposition'] = 'attachment; filename=' + dripcil.slugify(f.name) + '.pdf'
    response.write(f.data)

    return response


def template_render(request, tpl, params={}):
    return render(request, tpl, params)

@json_response
def do_notification(request):
    received_json_data=json.loads(request.body)
    logging.info(received_json_data)

    apns = APNs(use_sandbox=True, cert_file='niffy/apns-dev-cert.pem', key_file='niffy/apns-dev-key-plain.pem')

    # Send a notification
    token_hex = '502051FC4CC3CAE61C461967A789EC427684464C6387CEBB7BD708E2E2DD167C'
    payload = Payload(alert="New invoice from " + received_json_data['business_name'], sound="default", badge=1, custom=received_json_data)
    apns.gateway_server.send_notification(token_hex, payload)
    return None


# @json_response
# def persons(request):
#     return Person.query()


# @json_response
# def students(request):
#     # TODO:
#     org = Organization.query().get()
#     logging.info(org.key)
#     return Person.query_students(org.key)
