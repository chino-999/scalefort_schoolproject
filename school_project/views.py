# from django.shortcuts import render
# from rest_framework.viewSets import ViewSet
from .models import School, Student
from .serializers import SchoolSerializer,StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
# Create your views here.


# Custom Pagination

class StandardResultsSetPagination(PageNumberPagination):

    page_size = 4  # default items per page

    page_size_query_param = 'page_size'  # allow client to override

    max_page_size = 100  # maximum limit

class SchoolViewSet(APIView):

    def get(self,request):
        queryset = School.objects.all()
        name = request.query_params.get('name')

        address = request.query_params.get('address')

        type = request.query_params.get('type')

        if name:
            queryset = queryset.filter(name__icontains=name)

        if address:
            queryset = queryset.filter(address=address)

        if type:
            queryset = queryset.filter(type=type)

        serializer = SchoolSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data)


    def post(self,request):
        serializer = SchoolSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class getsingleschool(APIView):
    def get(self, request, pk):
        queryset = School.objects.get(pk=pk)
        serializer = SchoolSerializer(queryset,context={'request': request})
        return Response(serializer.data)


class SchoolListCreateView2(generics.ListCreateAPIView):


    queryset = School.objects.all()

    serializer_class = SchoolSerializer

    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ('name', 'address', 'type',)



"""-----------------------------------------------------------------------------------------------------------------------"""



class StudentViewSet(APIView):

    def get(self,request):
        queryset = Student.objects.all()
        name = request.query_params.get('name')

        age = request.query_params.get('age')

        school = request.query_params.get('school')

        if name:
            queryset = queryset.filter(name__icontains=name)

        if age:
            queryset = queryset.filter(age=age)

        if school:
            queryset = queryset.filter(school__icontains=name)

        serializer = StudentSerializer(queryset,many=True, context={'request': request})
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class getsinglestudent(APIView):

    def get_object(self,pk):

        try:

            return Student.objects.get(pk=pk)

        except Student.DoesNotExist:

            return None

    def get(self, request, pk):
#        queryset = self.get_object(pk)
        queryset = Student.objects.get(pk=pk)
        serializer = StudentSerializer(queryset, context={'request': request})
        return Response(serializer.data)


class StudentListCreateView2(generics.ListCreateAPIView):


    queryset = Student.objects.all()

    serializer_class = StudentSerializer

    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ('name', 'age', 'school',)