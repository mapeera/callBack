from rest_framework import serializers
from consult.models import*


class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ('__all__')
       


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('__all__')

        

class CreateTrans(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('__all__')
