from django.shortcuts import render
from api.models import Student
from rest_framework.views import APIView
from api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    
    return render(request,"index.html")

def student(request):
    student=Student.objects.all()
    
    return render(request,"student.html",{'student':student})

# def signup(request):
#     if request.method == 'POST':
#         form=SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user=form
#             auth_login(request,user)
#             return render(request,"student.html")
#         else:
#             form=SignupForm()
        
#     return render(request,"signup.html",{'form':form})

# def login(request):
#     username=request.POST['username']
#     password=request.POST['password']
#     user=authenticate(request,username=username,password=password)
#     if user is not None:
#         auth_login(request,user)
#         return render(request,"student.html")
#     else:
#         return render(request,"index.html")


class StudentList(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StudentDetail(APIView):
    def get(self,request,pk):
        student=Student.objects.get(pk=pk)
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self,request,pk):
        student=Student.objects.get(pk=pk)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student=Student.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)