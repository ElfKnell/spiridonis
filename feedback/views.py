from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ContactSerializer


class ContactView(APIView):
    def post(self, request, *args, **kwargs):
        serailizer_class = ContactSerializer(data=request.data)
        if serailizer_class.is_valid():
            data = serailizer_class.validated_data
            email_from = data.get('email')
            name = data.get('name')
            subject = data.get('subject')
            message = data.get('message')
            message_name = ' '.join([name, message])
            recipient_list = ('akyrych84@gmail.com', )
            send_mail(subject, message_name, email_from, recipient_list)
            return Response({"success": "Sent"}, status=status.HTTP_200_OK)
        return Response({"success": "Failed"}, status=status.HTTP_400_BAD_REQUEST)
