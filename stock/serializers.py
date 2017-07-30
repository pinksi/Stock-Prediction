from rest_framework import serializers
from .models import Adbl

class AdblSerializer(serializers.ModelSerializer):

	class Meta:
		model=Adbl
		fields='__all__'	

		