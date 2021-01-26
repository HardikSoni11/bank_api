from django.db.models import fields
from rest_framework import serializers
from .models import BankDetail

class BankDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankDetail
        fields = '__all__'