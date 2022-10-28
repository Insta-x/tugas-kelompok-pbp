from turtle import title
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.db.models import Count, Sum
from requests import request
from authentication.models import User
from .models import Project, Donation
import json

def show_projects(request):
    context = {'logged_in' : request.user.is_authenticated}

    return render(request, 'show_projects.html', context)

def get_projects(request):
    data = Project.objects.filter(title__icontains=request.GET.get('search')).annotate(like_count=Count('liked_by')).order_by('-like_count')

    return HttpResponse(json.dumps(encode_projects(data, request.user.id)), content_type='application/json')

def like_project(request):
    if request.user.is_authenticated:
        project_id = request.POST.get('id')
        project = Project.objects.get(pk=project_id)
        if request.user in project.liked_by.all():
            project.liked_by.remove(request.user)
        else:
            project.liked_by.add(request.user)
        return HttpResponse(json.dumps([encode_project(project, request.user.id), ]), content_type='application/json')

def show_project(request, id):
    project = Project.objects.get(pk=id)

    # print(Donation.objects.filter(project_id=id).aggregate(Sum('amount'))['amount__sum'])

    return render(request, 'show_project.html', {'project' : encode_project(project, request.user.id)})

def encode_projects(data_query_set, user_id):
    data_list = []
    for e in data_query_set:
        data_list.append(encode_project(e, user_id))
    return data_list

def encode_project(project, user_id):
    dict_data = json.loads(serializers.serialize('json', [project, ])[1:-1])
    dict_data['fields']['current_donation'] = Donation.objects.filter(project_id=project.pk).aggregate(Sum('amount'))['amount__sum'] or 0
    dict_data['fields']['owner_username'] = User.objects.get(pk=dict_data['fields']['user_id']).username
    dict_data['fields']['like_count'] = len(dict_data['fields']['liked_by'])
    dict_data['fields']['is_liked'] = user_id in dict_data['fields']['liked_by']
    del dict_data['fields']['liked_by']
    return dict_data