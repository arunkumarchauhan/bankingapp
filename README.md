 base_url='http://localhost:8000/'
 Get transaction by date:
 request type=GET 
 url =base_url+'v1/transactions/26-06-17'
 
 Get balance by date
request type=GET 
 url =base_url+'v1/balance/26-06-17'

Get Transation Detail by object id:
 request type=GET 
 url =base_url+'v1/details/1'

Add Transaction Detail:
 request type=POST
 url =base_url+'v1/add'
body=
{
    "account":123,
    "transaction_details":"My temp transaction",
    "withdrawal_amt":1000,
    "deposit_amt":0,
    "balance_amt":0
}