from __future__ import print_function
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.db.models import Count
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework import generics
from Dashboard.serializers import ClientSerializer
from ComplaintsForum.models import Client, ServiceSelected
from django.shortcuts import render
from Dashboard.fusioncharts import FusionCharts
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from ComplaintsForum.models import *
from reportlab.pdfgen import canvas
# from django.contrib.formtools.preview import FormPreview
# from django.http import HttpResponseRedirect
# from myapp.models import SomeModel

@login_required(login_url='/login')


def my_service_client(request):

    read = Service.objects.all()
    # print (posts)
    return render(request, "spare1.html", {'posts': read})


def service_list(request):
    posts = Service.objects.all()
    print (posts)
    return render(request, "spare1.html", {'posts': posts})

def post_list(request):
    posts = ServiceSelected.objects.all()
    print (posts)
    return render(request, "spare.html", {'posts': posts})


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

"""
def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'Dashboard_SealDeal.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Dashboard_SealDeal.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')
    return render(request, 'dashboard.html')
"""
import os
from django.template import Context
from django import template
from django.template.loader import get_template
def pdf_vieww(request):
    template = get_template("dashboard.html")
    context = Context({"data": report_data})
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')

def pdf_view(request):
    #path = os.expanduser('~/D:/pdf/')
    #f = open(path+TCS, "r")
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="SealDeal.pdf"'
    p = canvas.Canvas(response)
    p.drawString(25, 700,"Hey %s welcome to SealDeal. Further transactions will be forwarded to %s."%( request.user.username,request.user.email))
    p.showPage()
    p.save()
    return response

def DashboardCust(request):
    posts = ServiceSelected.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'dashboard_cust.html', context)

def Dashboard(request):

    u = User.objects.all().order_by('?')[:6]
    query=request.GET.get("q")
    if query:
        u = u.filter(
            Q(username__iexact=query)|
            Q(email__iexact=query)
            ).distinct()

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
    column2D = FusionCharts("column3D", "ex1", "100%", "50%", "chart-1", "json", dataSource)
    pie2D = FusionCharts("pie3d", "ex2", "100%", "400", "chart-2", "json", dataSource)


    context = {
        'u': u,
        'output': column2D.render(),
        'output1': pie2D.render(),
        'download': pdf_view

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
