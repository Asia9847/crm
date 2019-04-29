"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from mycrm.views import TeacherViewSet, StudentViewSet, CourseViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from mycrm import views

courses_detail = CourseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
courses_list = CourseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
teachers_detail = TeacherViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
teachers_list = TeacherViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
students_detail = StudentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
student_list = StudentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
urlpatterns = [
    path('get_column_name/', views.get_column_name),
    path('courses/', courses_list, name='course-list'),
    path('courses/<int:pk>/', courses_detail, name='course-detail'),
    path('teachers/', teachers_list, name='teacher-list'),
    path('teachers/<int:pk>/', teachers_detail, name='teacher-detail'),
    path('students/', student_list, name='student-list'),
    path('students/<int:pk>/', students_detail, name='student-detail')

]
urlpatterns = format_suffix_patterns(urlpatterns)
