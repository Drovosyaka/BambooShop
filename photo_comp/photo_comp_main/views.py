from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PhotoComp, Category
from .permissions import *
from .serializers import PhotoCompSerializer

class PhotoCompAPIList(generics.ListCreateAPIView):
    queryset = PhotoComp.objects.all()
    serializer_class = PhotoCompSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class PhotoCompAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = PhotoComp.objects.all()
    serializer_class = PhotoCompSerializer
    permission_classes = (IsAuthenticated, )

class PhotoCompAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = PhotoComp.objects.all()
    serializer_class = PhotoCompSerializer
    permission_classes = (IsAdminOrReadOnly, )

#class PhotoCompAPIView(APIView):
#    def get(self, request):
#        w = PhotoComp.objects.all()
#        return Response({'posts': PhotoCompSerializer(w, many=True).data})
#
#    def post(self, request):
#        serializer = PhotoCompSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#
#        return Response({'post': serializer.data})
#
#    def put(self, request, *args, **kwargs):
#        pk = kwargs.get("pk", None)
#        if not pk:
#            return Response({"error": "Method PUT is not allowed"})
#
#        try:
#            instance = PhotoComp.objects.get(pk=pk)
#        except:
#            return Response({"error": "Objects does not exist"})
#
#        serializer = PhotoCompSerializer(data=request.data, instance=instance)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response({"post": serializer.data})

#class PhotoCompAPIView(generics.ListAPIView):
#    queryset = PhotoComp.objects.all()
#    serializer_class = PhotoCompSerializer
