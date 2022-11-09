from django.shortcuts import render

from rest_framework import generics, status,views
from rest_framework.views import APIView

from rest_framework.response import Response

from .serializers import*
from .models import*

# Create your views here.
from .utils import Util



admin_email = 'bbosalj@gmail.com'
#now i will be sending the emails here to alert that a booking gas been made


class ConsultView(APIView):
    serializer_class= ConsultSerializer
    def post(self, request,*args,**kwargs):
        name = request.data.get('name',False)
        phone = request.data.get('phone',False)
        category= request.data.get('category',False)

        
        if name and phone and category:
            #go ahead and create the object
            consult = Consultation(name=name,phone=phone,category=category)
            consult.save()
            return Response({
                'status':True,
                'message':'Consultation placed'
            },status=status.HTTP_200_OK)
        else:
            return Response({
                'status':False,
                'message':'provide name,phone and category'
            })


class BookingView(APIView):
    def post(self,request, *args, **kwargs):
        name = request.data.get('name',False)
        phone = request.data.get('phone',False)
        description = request.data.get('description',False)
        location = request.data.get('location',False)


        if name and phone:
            booking = Booking(
                name=name,phone=phone,description=description,location=location
            )
            booking.save()
            #after booking is placed
            email_body = 'Booking made, details,{0},{1},{2},{3}'.format(name,phone,description,location)
            data = {
                'email_body':email_body,
                'to_email':admin_email,
                'email_subject':'Booking successful'
            }
            Util.send_email(data)
            return Response({
                'status':True,
                'name':name,
                'phone':phone,
                'status':True,
                'message':'Booking was successful'
            })
        else:
            return Response({
                'status':False,
                'message':'provide phone and name'
            })

#==create transaction record====
class CreateTrans(APIView):
    def post(self,request, *args, **kwargs):
        phone = request.data.get('phone',False)
        customer_name = request.data.get('customer_name',False)
        amount = request.data.get('amount',False)
        action = request.data.get('action',False)

        if phone and customer_name and amount and action:
            transaction = Transaction(
                phone = phone,
                customer_name = customer_name,
                amount = amount,
                action = action,
            )
            transaction.save()
            email_body = 'Transaction details,{0},{1},{2},{3}'.format(
                transaction.real_trans_id,customer_name,phone,amount,action,)
            data = {
                'email_body':email_body,
                'to_email':admin_email,
                'email_subject':'Transaction successful'
            }
            Util.send_email(data)
            return Response({
                'status':True,
                'trans_id':transaction.real_trans_id,
                'customer_name':customer_name,
                'amount':amount,
                'total_collected':transaction.final_collected,
                'action':action,
                'message':'Transaction made successfully'
            })
        else:
            return Response({
                'status':False,
                'message':'Some details are missing'
            })