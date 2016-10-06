# coding=utf-8
import logging

from google.appengine.ext import ndb

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.conf import settings

# from ludus.models import Person, Organization


def home(request):
    return template_render(request, 'home.html')


# def json_response(func):
#     """
#     A decorator thats takes a view response and turns it
#     into json. If a callback is added through GET or POST
#     the response is JSONP.
#     """
#     def decorator(request, *args, **kwargs):
#         response = func(request, *args, **kwargs)
#         if isinstance(response, HttpResponse):
#             return response
#         elif isinstance(response, ndb.Model):
#             return JsonResponse(response.to_json())
#         elif isinstance(response, ndb.Query):
#             return JsonResponse([e.to_json() for e in response], safe=False)
#         else:
#             return JsonResponse(response, safe=False)
#     return decorator


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
