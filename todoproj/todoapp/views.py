from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import todoapp
# Create your views here.
# class todo_view(viewsets.ModelViewSet):
#     # list 
#     def list(self,request):
#         todo = todoapp.objects.all()
#         return Response(todo.values())
    
#     # create
#     def create(self,request):
#         try:
#             id = request.data.get('id')
#             name = request.data.get('name')
#             age = request.data.get('age')
#             if id is None or name is None or age is None:
#                 return Response({'Unknown':'Value'},status=status.HTTP_400_BAD_REQUEST)
            
#             users = todoapp.objects.create(id=id,name=name,age=age)
#             return Response({'successfull':'Account create'},status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        
#     def update(self,request,pk=None):
#         try:
#             id = request.data.get('id')
#             name = request.data.get('name')
#             age = request.data.get('age')

#             if id is None:
#                 return Response({'Unknow':'Value'},status=status.HTTP_400_BAD_REQUEST)
            
#             users = todoapp.objects.get(pk=id)
#             users.name = name
#             users.age = age
#             users.save()
#             return Response({'Updated':'Successfully'},status=status.HTTP_202_ACCEPTED)
#         except todoapp.DoesNotExist:
#             return Response({'Error':'Showing Error'},status=status.HTTP_400_BAD_REQUEST)
        
#     def destroy(self,request,pk=None):

#         try:
#             id = request.data.get('id')
#             name = request.data.get('name')
#             age = request.data.get('age')

#             users = todoapp.objects.get(pk=id)
#             users.delete()
#             return Response({"Delete":"Successfully"},status=status.HTTP_202_ACCEPTED)
#         except todoapp.DoesNotExist:
#             return Response({"Error":"Showing Error"},status=status.HTTP_400_BAD_REQUEST)

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import todoapp

class todo_view(viewsets.ViewSet):

    def list(self, request):
        data = []
        for todo in todoapp.objects.all():
            data.append({
                "id": todo.id,
                "name": todo.name,
                "age": todo.age
            })
        return Response(data)

    def create(self, request):
        id = request.data.get('id')
        name = request.data.get('name')
        age = request.data.get('age')

        if not id or not name or not age:
            return Response({'error': 'Missing fields'}, status=400)

        new = todoapp.objects.create(pk=id, name=name, age=age)
        return Response({
            'message': 'Created successfully',
            'id': new.id,
            'name': new.name,
            'age': new.age  
        }, status=201)
    
    def update(self, request,pk=None):
      

        try:
            users = todoapp.objects.get(pk=pk)
            users.name = request.data.get("name",users.name)
            users.age = request.data.get("age",users.age)
            users.save()
            return Response({
                'Message' : 'Successfully Updated',
                'id' : users.id,
                'name' : users.name,
                'age' : users.age
            },status=status.HTTP_200_OK)
        except todoapp.DoesNotExist:
            return Response({'Error':'Showing Error'},status=status.HTTP_400_BAD_REQUEST)
        

    def partial_update(self, request , pk=None):
        
        try:
            users = todoapp.objects.get(pk=pk)

            if 'name'in request.data:
                users.name = request.data.get("name",users.name)
            if 'age' in request.data:
                users.age = request.data.get("age",users.age)
            users.save()
            return Response({
                'Message' : 'Successfully Updated',
                'id' : users.id,
                'name' : users.name,
                'age' : users.age
            },status=status.HTTP_200_OK)
        except todoapp.DoesNotExist:
            return Response({'Error':'Showing Error'},status=status.HTTP_400_BAD_REQUEST)
            

            
    # delete 
    def destroy(self,request,pk=None):
        try:
            users = todoapp.objects.get(pk=pk)
            users.delete()
            return Response({
                'Deleted' : 'Successflly'
            },status=status.HTTP_200_OK)
        except todoapp.DoesNotExist:
            return Response({
                'Error' : 'It was Showing Error'
            },status=status.HTTP_400_BAD_REQUEST)
    

    
