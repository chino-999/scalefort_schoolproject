from django.urls import path, include
from school_project import views
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet,StudentViewSet,StudentListCreateView2,SchoolListCreateView2


# router = DefaultRouter()
# router.register('schools',SchoolViewSet)
# router.register('students',StudentViewSet)


urlpatterns = [
    path('school/',views.SchoolViewSet.as_view(), name="school-details"),
    path('student/',views.StudentViewSet.as_view(), name="student-details"),
    path('school/<int:pk>',views.getsingleschool.as_view(), name="school-detail"),
    path('student/<int:pk>',views.getsinglestudent.as_view(), name="student-detail"),
    path('students/', StudentListCreateView2.as_view(), name="student-details"),
    path('schools/',SchoolListCreateView2.as_view(),name="student-details"),
]