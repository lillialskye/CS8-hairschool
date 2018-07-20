from .models import C_Scheduling
from rest_framework import serializers

class CSchedulingSerializer(serializers.ModelSerializer)
	
    class meta:
	model = C_Scheduling
	fields= ('Services', 'Price', 'Stylist', 'Date', 'Time') 

