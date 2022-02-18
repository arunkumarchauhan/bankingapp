
from rest_framework import serializers
from datetime import datetime

from .models import Transaction


class TransactionApiDataSerializer(serializers.Serializer):
    account = serializers.IntegerField(source='Account No')
    date = serializers.SerializerMethodField(allow_null=True,method_name='get_date')
    value_date = serializers.SerializerMethodField(allow_null=True,method_name='get_value_date')
    transaction_details = serializers.CharField(max_length=500, allow_blank=True,source='Transaction Details')
    withdrawal_amt = serializers.SerializerMethodField( allow_null=True,default=0,method_name='get_widthdrawal_amt')
    deposit_amt = serializers.SerializerMethodField( allow_null=True,default=0,method_name='get_deposit_amt')
    balance_amt = serializers.SerializerMethodField( allow_null=True,default=0,method_name='get_balance_amt')

    def get_date(self, data):

        date_temp=data.get('Date',None)
        if date_temp and date_temp!='':
            return str(datetime.strptime(date_temp, '%d %b %y'))[:10]
        return None

    def get_value_date(self, data):

        date_temp=data.get('Value Date',None)
        if date_temp and date_temp!='':
            return str(datetime.strptime(date_temp, '%d %b %y'))[:10]
        return None



    def get_widthdrawal_amt(self, data):
        amt=data.get('Withdrawal AMT',None)
        amt=amt.replace(',','')

        if amt is not None and amt !='':
            return float(amt)
        return 0

    def get_deposit_amt(self, data):
        amt=data.get('Deposit AMT',None)
        amt=amt.replace(',','')

        if amt is not None and amt !='':
            return float(amt)
        return 0
    def get_balance_amt(self, data):
        amt=data.get('Balance AMT',None)
        amt=amt.replace(',','')

        if amt is not None and amt !='':
            return float(amt)
        return 0


class GetTranscationByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'