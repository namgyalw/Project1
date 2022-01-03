from rest_framework import serializers
from library.models import Student


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ['id','Name','Gender','Age','Grade']