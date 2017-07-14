from __future__ import print_function
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.db.models import Count
# from django.contrib.auth import authenticate, logout, login
# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# from TCSProj import settings
import json
from django.core import serializers
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework import generics
from Dashboard.serializers import ClientSerializer
from ComplaintsForum.models import Client, ServiceSelected
# from django.utils.encoding import smart_unicode
# from rest_framework import renderers
from django.shortcuts import render
from Dashboard.fusioncharts import FusionCharts
# from django.core import serializers

# json_data = serializers.serialize('json', data)
# return HttpResponse(json_data, mimetype='application/json')


@login_required(login_url='/login/')

def chart(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Service Progress",
        "subCaption": "XYZ Company",
        "xAxisName": "Services",
        "yAxisName": "No. of Clients",
        "numberPrefix": "",
        "theme": "fint",
        "labelDisplay": "auto",
    }

    # The data for the chart should be in an array where each element of the array is a JSON object
    # having the `label` and `value` as key value pair.

    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in ServiceSelected.objects.values('serviceSelected').annotate(dcount=Count('serviceSelected')):
        data = {}
        print(key)
        data['label'] = key['serviceSelected']
        data['value'] = key['dcount']
        dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D = FusionCharts("column2D", "ex1", "600", "350", "chart-1", "json", dataSource)
    return render(request, 'spare.html', {'output': column2D.render()})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer






def Dashboard(request):

    u= User.objects.all().order_by('?')[:6]

    dataSource = {}
    dataSource['chart'] = {
        "caption": "Service Progress",
        "subCaption": "XYZ Company",
        "xAxisName": "Services",
        "yAxisName": "No. of Clients",
        "numberPrefix": "",
        "theme": "fint",
        "labelDisplay": "auto",
    }

    # The data for the chart should be in an array where each element of the array is a JSON object
    # having the `label` and `value` as key value pair.

    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in ServiceSelected.objects.values('serviceSelected').annotate(dcount=Count('serviceSelected')):
        data = {}
        print(key)
        data['label'] = key['serviceSelected']
        data['value'] = key['dcount']
        dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D = FusionCharts("column2D", "ex1", "600", "350", "chart-1", "json", dataSource)
    context = {
        'u': u,
        'output': column2D.render(),
    }
    return render(request, 'dashboard.html', context)

    # return render(request, 'dashboard.html',context)

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# def json_search(request):
#     query = request.GET.get('query')
#     # api_key = locu_api
#     # ;
#     # locality = query.replace(' ', '%20')
#     final_url = "{% url 'dashboard_api' %}"
#     json_obj = urllib2.urlopen(final_url)
#     decoded_data = json.load(json_obj)
#     return render(request, 'spare.html',
#                        {'objects': decoded_data['objects']})