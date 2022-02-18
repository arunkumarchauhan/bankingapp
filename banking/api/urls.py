from django.urls import path, include,re_path
from django.contrib import admin

from .views import AddDataToTable, GetTransactionDataOnDate, GetBalanceAmountOnDate, GetTransactionDetailbyId, \
    AddTransaction

urlpatterns = [
    path('v1/enter-data', AddDataToTable.as_view(), name='enter_data_to_table_from_api'),
re_path('v1/transactions.*', GetTransactionDataOnDate.as_view(), name='get_transaction_data_on_date'),
re_path('v1/balance.*', GetBalanceAmountOnDate.as_view(), name='get_transaction_data_on_date'),
re_path('v1/details.*', GetTransactionDetailbyId.as_view(), name='get_transaction_details'),
path('v1/add', AddTransaction.as_view(), name='add_transaction_details'),
]