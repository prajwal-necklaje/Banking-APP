from django import forms
from .models import CreditCard


class CreditCardForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Card Holder Name"}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Card Number"}))
    month = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Expiry Year"}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Expiry Month"}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"CVV"}))


    class Meta:
        model = CreditCard
        fields = ['name', 'number', 'month', 'year', 'cvv', 'card_type']

class DepositForm(forms.Form):
    deposit_amount = forms.DecimalField(max_digits=12, decimal_places=2, required=True, label="Deposit Amount")
    deposit_method = forms.ChoiceField(
        choices=[
            ('bank_transfer', 'Bank Transfer'),
            ('credit_card', 'Credit Card'),
            ('mobile_wallet', 'Mobile Wallet'),
            ('cash_deposit', 'Cash Deposit'),
        ],
        required=True,
        label="Deposit Method"
    )