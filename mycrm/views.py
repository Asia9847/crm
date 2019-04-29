from rest_framework import generics, status, viewsets
from mycrm.serializer import StudentSerializer, TeacherSerializer, CourseSerializer
from mycrm.models import Student, Teacher, Course


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def get_column_name(request):

    if request.method == 'POST':
        data_name = request.data['data_name']
        column_name = []
        field = ''
        if(data_name=='teacher'):
            field = Teacher._meta.fields
        if (data_name == 'student'):
            field = Student._meta.fields
        if (data_name == 'course'):
            field = Course._meta.fields
        for f in field:
            column_name.append(f.name)
        data = {
            'column_name':column_name
        }
        return Response(data=data)
