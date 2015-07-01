__author__ = 'dgaievskiy'

from django.http import HttpRequest


def students_proc(request):
    return {'PORTAL_URL': 'http://' + HttpRequest.get_host(request)}
