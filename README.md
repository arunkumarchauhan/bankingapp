 Postgres local installation does not require db in hosted on heroku
Steps to run on localserver:
1.Postgres should be installed:
2.create db in postgres and replace dbname in settings.py file
3.run command python manage.py makemigrations
4.run command python manage.py migrate
5.run command python manage.py runserver
6.To insert data from provided json url to db use api  1 below 
7.now you can start using other the api for querying

local_base_url='http://localhost:8000/banking/api/'
deployed_base_url='https://bankingxkcd.herokuapp.com/banking/api/'

base_url=local_base_url or deployed_base_url

mere this url 'https://bankingxkcd.herokuapp.com' will give not found as nothing is setup on root url

1.Add Transactions from json url provided to DB
request type=GET
url=base_url+v1/enter-data
response=List of json datas inserted in db

2. Get transaction by date:
 request type=GET 
 url =base_url+'v1/transactions/26-06-17'
 
 3.Get balance by date
request type=GET 
 url =base_url+'v1/balance/26-06-17'

4.Get Transation Detail by object id:
 request type=GET 
 url =base_url+'v1/details/1'

5.Add Transaction Detail:
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

