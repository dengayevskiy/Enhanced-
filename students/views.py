# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

# Views for students
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Джек',
         'last_name': u'Деніелс',
         'ticket': 2135,
         'image': 'img/1.jpg'},
        {'id': 2,
         'first_name': u'Майкл',
         'last_name': u'Джексон',
         'ticket': 2136,
         'image': 'img/2.jpg'},
        {'id': 3,
         'first_name': u'Володимир',
         'last_name': u'Путін',
         'ticket': 2137,
         'image': 'img/3.jpg'}
    )
    return render(request, 'students/students_list.html',
                  {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student</h1>' % sid)


# Views for groups
def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)


# Views for journal
def journal(request):
    return render(request, 'students/journal.html', {})
