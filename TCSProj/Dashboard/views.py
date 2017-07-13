from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render
# from django.contrib.auth import authenticate, logout, login
# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# from TCSProj import settings
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework import generics
from Dashboard.serializers import ClientSerializer
from ComplaintsForum.models import Client
# from django.utils.encoding import smart_unicode
# from rest_framework import renderers
from django.shortcuts import render


@login_required(login_url='/login/')

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

    u= User.objects.all().order_by('?')[:5]

    context = {
        'u' : u
    }
    return render(request, 'dashboard.html',context)

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

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