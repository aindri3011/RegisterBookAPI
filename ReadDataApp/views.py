from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import batchcreationSerializer, updateBatchSerializer

from .services.student import getUserDetails, getStudentDetails, \
                                getUserLoggedOnSpecificDate, createbatch, \
                                updateBatch, getStudentDetailsUsingEmail


class get_student_summary_api(APIView):

    def get(self, request):
        uid = request.GET.get('uid')

        if uid != '':
            ob1 = getUserDetails(uid)
            return_data = ob1.start_process()
            if return_data:
                return Response(return_data, status=status.HTTP_201_CREATED)
            return Response(return_data, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = batchcreationSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = createbatch(serializer)
            batch_data = ob1.start_process()
            if batch_data:
                return Response(batch_data, status.HTTP_201_CREATED)
            else:
                return Response("process error", status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = updateBatchSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = updateBatch(serializer)
            return_data = ob1.start_process()
            if return_data:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("process error", status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class get_summary_from_phone(APIView):

    def get(self, request):
        phone = request.GET.get('phone')

        print('------getting in views', phone, type(phone))

        if phone != '':
            ob1 = getStudentDetails(phone)
            return_data = ob1.start_process()
            if return_data:
                return Response(return_data, status=status.HTTP_201_CREATED)
            return Response(return_data, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)


class get_list_from_registrationDate(APIView):

    def get(self, request):
        regDate = request.GET.get('regDate')

        print('------getting in views', regDate, type(regDate))

        if regDate != '':
            ob1 = getUserLoggedOnSpecificDate(regDate)
            return_data = ob1.start_process()
            if return_data:
                return Response(return_data, status=status.HTTP_201_CREATED)
            return Response(return_data, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)


class get_summary_from_email(APIView):

    def get(self, request):
        email = request.GET.get('email')

        print('------getting in views', email, type(email))

        if email != '':
            ob1 = getStudentDetailsUsingEmail(email)
            return_data = ob1.start_process()
            if return_data:
                return Response(return_data, status=status.HTTP_201_CREATED)
            return Response(return_data, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)
