
from django.db import models




class Transaction(models.Model):

    account = models.BigIntegerField(db_index=True,null=False)
    date = models.DateField(null=True,blank=True)
    value_date=models.DateField(null=True,blank=True)
    transaction_details = models.CharField(max_length=500,null=True,blank=True)
    withdrawal_amt = models.FloatField(default=0,null=True)
    deposit_amt=models.FloatField(default=0,null=True)
    balance_amt = models.FloatField(default=0,null=True)

    class Meta:
        db_table = 'transaction'
