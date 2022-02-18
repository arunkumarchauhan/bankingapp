import datetime
import logging

from django.db import transaction
from django.db.models import Count, Sum, F
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import AddTransactionForm
from .models import Transaction
from .serializers import *

logger = logging.getLogger('django')
import requests
import json

class AddDataToTable(APIView):
    permission_classes = []
    authentication_class = []

    def get(self, request):
        try:
            response_API = requests.get(
                'https://s3-ap-southeast-1.amazonaws.com/he-public-data/bankAccountdde24ad.json')
            if response_API.status_code==200:
                print("HERE")
                serializer=TransactionApiDataSerializer(response_API.json(),many=True)
                json_data=json.dumps(serializer.data)
                dict_data=json.loads(json_data)

                with transaction.atomic():
                    for d in dict_data:

                        Transaction(account=d.get('account'),
                                    date=d.get('date'),
                                    value_date=d.get('value_date'),
                                    transaction_details=d.get('transaction_details'),
                                    withdrawal_amt=d.get('withdrawal_amt'),
                                    deposit_amt=d.get('deposit_amt'),
                                    balance_amt=d.get('balance_amt')).save()
                entered_data=Transaction.objects.all().values('account','date','value_date',
                                                              'transaction_details','withdrawal_amt'
                                                              ,'deposit_amt','balance_amt')
                return Response(data=entered_data,status=status.HTTP_200_OK)

            return Response(data={"message": "Something went wrong."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.exception(e)
            return Response(data={"message": "Something went wrong."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class GetTransactionDataOnDate(APIView):
    permission_classes = []
    authentication_class = []

    def get(self, request):
        try:
            full_path=request.get_full_path()
            date_temp=full_path.split('/')[-1]
            date=datetime.strptime(date_temp, '%d-%m-%y').date()

            particular_date_data=Transaction.objects.filter(date=date).values('account','date','value_date',
                                                              'transaction_details','withdrawal_amt'
                                                              ,'deposit_amt','balance_amt')
            return Response(data=particular_date_data,status=status.HTTP_200_OK)


        except Exception as e:
            logger.exception(e)
            return Response(data={"message": "Something went wrong."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetBalanceAmountOnDate(APIView):
    permission_classes = []
    authentication_class = []

    def get(self, request):
        try:
            full_path=request.get_full_path()
            date_temp=full_path.split('/')[-1]
            date=datetime.strptime(date_temp, '%d-%m-%y').date()

            particular_date_data=Transaction.objects.filter(date=date).aggregate(total_balance_amt=Sum('balance_amt'))
            return Response(data=particular_date_data,status=status.HTTP_200_OK)


        except Exception as e:
            logger.exception(e)
            return Response(data={"message": "Something went wrong."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetTransactionDetailbyId(APIView):
    permission_classes = []
    authentication_class = []

    def get(self, request):
        try:
            full_path=request.get_full_path()
            id_temp=full_path.split('/')[-1]
            id_temp=int(id_temp)
            res_data=Transaction.objects.get(id=id_temp)
            serializer=GetTranscationByIdSerializer(res_data)
            return Response(data=serializer.data,status=status.HTTP_200_OK)


        except Exception as e:
            logger.exception(e)
            return Response(data={"message": "Something went wrong."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddTransaction(APIView):
    permission_classes = []
    authentication_class = []

    def post(self, request):
        try:
            form=AddTransactionForm(request.data)
            if not form.is_valid():
                return Response(data=form.errors,status=status.HTTP_400_BAD_REQUEST)

            cleaned_data=form.cleaned_data
            date=datetime.today().date()

            account=cleaned_data.get('account')
            transaction_details=cleaned_data.get('transaction_details')
            withdrawal_amt=cleaned_data.get('withdrawal_amt')
            deposit_amt=cleaned_data.get('deposit_amt')
            balance_amt=cleaned_data.get('balance_amt')
            obj=Transaction(account=account,transaction_details=transaction_details
                                                       ,date=date,value_date=date,withdrawal_amt=withdrawal_amt,
                                                       deposit_amt=deposit_amt,balance_amt=balance_amt)
            obj.save()
            serializer = GetTranscationByIdSerializer(obj)
            return Response(data=serializer.data,status=status.HTTP_200_OK)


        except Exception as e:
            logger.exception(e)
            return Response(data={"message": "Something went wrong.",'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
