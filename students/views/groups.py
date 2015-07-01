# -*- coding: utf-8 -*-
__author__ = 'dgaievskiy'

from django.http import HttpResponse
from django.shortcuts import render


# Views for groups
def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'MiM-123',
         'lead_student': u'Джек Деніелс',
         'lead_student_id': 1},
        {'id': 2,
         'name': u'MiM-124',
         'lead_student': u'Джон Голт',
         'lead_student_id': 2},
        {'id': 3,
         'name': u'MiM-125',
         'lead_student': u'Джим Моррісон',
         'lead_student_id': 3}
    )
    return render(request, 'students/groups_list.html',
                  {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
