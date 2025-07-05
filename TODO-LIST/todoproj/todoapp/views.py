# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.viewsets import ViewSet
#
# from .models import TODOAPP
# from .serializers import TODOSerializer
#
#
# class TODOViews(ViewSet):
#     # list the details from the db table
#     def list(self,request):
#         app_data = TODOAPP.objects.all()
#         serializer = TODOSerializer(app_data,many=True)
#         return Response(serializer.data)
#
#     def create(self,request):
#         work_name = request.get('work_name')
#
#         if not work_name:
#             return Response({"error": "Work name is required"}, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer = TODOSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request,pk=None):
#         pk = request.GET.get('id')  # ✅ Get ID query param
#         work_name = request.GET.get('work_name')  # ✅ Get new task name
#         try:
#             todo_instance = TODOAPP.objects.get(pk=pk)
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#         serializer = TODOSerializer(todo_instance,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request,pk=None):
#         try:
#             todo_instance = TODOAPP.objects.get(pk=pk)
#             print(f"{pk}")
#         except TODOAPP.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         todo_instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
# from rest_framework import status
# from .models import TODOAPP
# from .serializers import TODOSerializer
#
#
# class TODOViews(ModelViewSet):
#     queryset = TODOAPP.objects.all()
#     serializer_class = TODOSerializer
#
#     #  Override `list()` to support query parameters
#     def list(self, request):
#         # get the id from the url
#         id: object = request.query_params.get('id')
#         print('id passed:', id)
#         # select all objects from the db table
#         filering_id: object = TODOAPP.objects.all()
#         # check the id by filter
#         if id:
#             filering_id = filering_id.filter(id=id)
#         print('print filtered id :', filering_id)
#
#         # conver filter into serializer
#         serializer = self.get_serializer(filering_id, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     #  Override `create()` to support query parameters
#     def create(self, request):
#         id = request.query_params.get('id')  # get the id parameter
#         work_name = request.query_params.get('work_name')
#         print('id : ', id)
#         print('work_name:', work_name)
#
#         # create the user
#         try:
#             user = TODOAPP.objects.create(id=id,work_name=work_name)
#             # serializer = self.get_serializer(user)
#             return Response(user.data, status=status.HTTP_200_OK)
#         except TODOAPP.DoesNotExit:
#             return Response({'errors': 'The error was user not created properly'}, status=status.HTTP_400_BAD_REQUEST)
#
#         return Response({'errors :', 'user was not created with this id'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, pk=None):
#         id = request.query_params.get('id')  # get the id parameter
#         work_name = request.query_params.get('work_name')
#         print('id : ', id)
#         print('work_name:', work_name)
#         if not id and not work_name:
#             return Response({'error': 'ID is missing'}, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             # Fetch the instance using the provided `id`
#             instance = TODOAPP.objects.get(id=id)
#             print('instance id :', instance)
#         except TODOAPP.DoesNotExist:
#             return Response({'error': 'Instance not found'}, status=status.HTTP_404_NOT_FOUND)
#
#         # Use the serializer to validate and update the instance
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk=None):
#         id = request.query_params.get('id')
#         print(f'id passed : {pk}')
#         if not pk:
#             return Response({'error': 'ID is missing'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             instance = TODOAPP.objects.get(id=pk)
#             instance.delete()
#             return Response({'message': 'Instance deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#         except TODOAPP.DoesNotExist:
#             return Response({'error': 'Instance not found'}, status=status.HTTP_404_NOT_FOUND)

#
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
# from rest_framework import status
# from .models import TODOAPP
#
#
# class TODOViews(ModelViewSet):
#     queryset = TODOAPP.objects.all()
#
#     #  Override `list()` to support query parameters
#     def list(self, request):
#         all_row = TODOAPP.objects.all()
#         print('list all rows :', all_row)
#         return Response(all_row.values(), status=status.HTTP_200_OK)
#
#     #  Override `create()` to support query parameters
#     def create(self, request):
#         id = request.data.get('id')
#         work_name = request.data.get('work_name')
#
#         print('id : ', id)
#         print('work_name:', work_name)
#
#         # create the user
#         try:
#             # id = int(id)
#             user = TODOAPP.objects.create(id=id, work_name=work_name)
#             # return Response({'id': user.id, 'work_name': user.work_name}, status=status.HTTP_200_OK)
#             return Response({user.id, user.work_name}, status=status.HTTP_200_OK)
#         except Exception as ex:
#             return Response({'errors': str(ex)}, status=status.HTTP_400_BAD_REQUEST)
#
#         return Response({'errors :', 'user was not created with this id'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, pk=None):
#         id = request.data.get('id')  # get the id parameter
#         work_name = request.data.get('work_name')
#         print('id : ', id)
#         print('work_name:', work_name)
#
#         if not id and not work_name:
#             return Response({'error': 'ID is missing'}, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             # Fetch the instance using the provided `id`
#             instance = TODOAPP.objects.get(id=id)
#             print('instance id :', instance)
#             instance.work_name = work_name
#             instance.save()
#             return Response({instance.id, instance.work_name}, status=status.HTTP_200_OK)
#         except TODOAPP.DoesNotExist:
#             return Response({'error': 'Instance not found'}, status=status.HTTP_404_NOT_FOUND)
#         return Response({'eror :', ' data was not updated in db'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk=None):
#         id = request.data.get('id')
#         work_name = request.data.get('work_name')
#         print(f'id passed : {id}')
#         if not id:
#             return Response({'error': 'ID is missing'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             instance = TODOAPP.objects.get(id=id,work_name=work_name)
#             print('instace :', instance)
#             instance.delete()
#             return Response({instance.id, instance.work_name}, status=status.HTTP_200_OK)
#         except TODOAPP.DoesNotExist:
#             return Response({'error': 'Instance not found'}, status=status.HTTP_404_NOT_FOUND)
#         return Response({'error': 'id was not deleted from db'})


# without using serializer in queryset

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import TODOAPP
from .serializers import TODOSerializer


class TODOViews(ModelViewSet):
    queryset = TODOAPP.objects.all()
    serializer_class = TODOSerializer

    #  Override `list()` to support query parameters
    def list(self, request):
        # get the id from the url
        id: object = request.query_params.get('id')
        print('id passed:', id)
        # select all objects from the db table
        filering_id: object = TODOAPP.objects.all()
        # check the id by filter
        if id:
            filering_id = filering_id.filter(id=id)
        print('print filtered id :', filering_id)

        # conver filter into serializer
        # serializer = self.get_serializer(filering_id, many=True)
        return Response(filering_id.values(), status=status.HTTP_200_OK)

    #  Override `create()` to support query parameters
    def create(self, request):
        id = request.query_params.get('id')  # get the id parameter
        work_name = request.query_params.get('work_name')
        print(f'id was passed : {id}')
        print(f'work_name was passed : {work_name}')

        # create the user
        try:
            user = TODOAPP.objects.create(id=id, work_name=work_name)
            return Response({"Successfully Inserted", "id:", user.id, "work_name:", user.work_name},
                            status=status.HTTP_200_OK)
        except TODOAPP.DoesNotExist:
            return Response({'errors': 'The error was user not created properly'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'errors :', 'user was not created with this id'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        id = request.query_params.get('id')  # get the id parameter
        work_name = request.query_params.get('work_name')
        print('id : ', id)
        print('work_name:', work_name)
        if not id and not work_name:
            return Response({'error': 'ID is missing'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # Fetch the instance using the provided `id`
            instance = TODOAPP.objects.get(id=id)
            instance.work_name = work_name
            print('instance id :', instance)
            instance.save()
            return Response({"message": "record was inserted successfully","id":instance.id,"work_name" : instance.work_name},  status=status.HTTP_200_OK)
        except TODOAPP.DoesNotExist:
            return Response({'error': 'Instance not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        id = request.query_params.get('id')
        print(f'id passed : {pk}')
        if not pk:
            return Response({'error': 'ID is missing'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = TODOAPP.objects.get(id=pk)
            instance.delete()
            return Response({'message': 'Instance deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except TODOAPP.DoesNotExist:
            return Response({'error': 'Instance not found'}, status=status.HTTP_404_NOT_FOUND)
