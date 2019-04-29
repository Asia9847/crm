from rest_framework import serializers
from mycrm.models import Teacher, Student, Course


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'phone')


class StudentSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='course.name')
    class Meta:
        model = Student
        fields = ('id', 'name', 'age', 'course')


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source='teacher.name')
    class Meta:
        model = Course
        fields = ('id', 'name', 'teacher')
