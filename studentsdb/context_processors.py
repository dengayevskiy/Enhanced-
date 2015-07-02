__author__ = 'dgaievskiy'

from django.http import HttpRequest


def students_proc(request):
    return {'PORTAL_URL': request.scheme + "://" + HttpRequest.get_host(request)}
