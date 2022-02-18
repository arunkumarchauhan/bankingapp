from django import forms
from django.contrib.postgres.forms import SimpleArrayField



class AddTransactionForm(forms.Form):
    account = forms.IntegerField(required=True)
    transaction_details = forms.CharField(required=True)
    withdrawal_amt = forms.FloatField( required=True)
    deposit_amt = forms.FloatField( required=True)
    balance_amt = forms.FloatField( required=True)

