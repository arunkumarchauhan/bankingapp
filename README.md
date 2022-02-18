 Postgres local installation does not require as db is hosted on heroku<br><br>
 ##Steps to run on localserver:<br><br>
1.Postgres should be installed:<br>
2.create db in postgres and replace dbname in settings.py file<br>
3.run command python manage.py makemigrations<br>
4.run command python manage.py migrate<br>
5.run command python manage.py runserver<br>
6.To insert data from provided json url to db use api  1 below <br>
7.now you can start using other the api for querying<br>

#local_base_url='http://localhost:8000/banking/api/'
#deployed_base_url='https://bankingxkcd.herokuapp.com/banking/api/'

#base_url=local_base_url or deployed_base_url

#mere this url 'https://bankingxkcd.herokuapp.com' will give not found as nothing is setup on root url

1.Add Transactions from json url provided to DB<br>
request type=GET<br>
url=base_url+v1/enter-data<br>
response=List of json datas inserted in db<br>
<br><br>
2. Get transaction by date:<br>
 request type=GET <br>
 url =base_url+'v1/transactions/26-06-17'<br>
 <br>
3.Get balance by date<br>
request type=GET <br>
 url =base_url+'v1/balance/26-06-17'<br><br>

4.Get Transation Detail by object id:<br>
 request type=GET <br>
 url =base_url+'v1/details/1'<br><br>

5.Add Transaction Detail:<br>
 request type=POST<br>
 url =base_url+'v1/add'<br>
body=<br>
{<br>
    "account":123,<br>
    "transaction_details":"My temp transaction",<br>
    "withdrawal_amt":1000,<br>
    "deposit_amt":0,<br>
    "balance_amt":0<br>
}<br>

