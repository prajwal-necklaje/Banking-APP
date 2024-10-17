
from .models import Account
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DepositForm
from .models import Account
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def account_list(request):
    query = request.GET.get('account_number')

    if query:
        accounts = Account.objects.filter(
            Q(account_number__icontains=query) | 
            Q(user__username__icontains=query)
        )
    else:
        accounts = Account.objects.all()
    return render(request, 'core/account_list.html', {'accounts': accounts})

@login_required
def deposit_money(request):
    account = Account.objects.get(user=request.user)

    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit_amount = form.cleaned_data['deposit_amount']
            deposit_method = form.cleaned_data['deposit_method']
            
            # Update account balance
            account.account_balance += deposit_amount
            account.save()

            # Here you can handle deposit_method logic if needed
            # For example, you could add logging or notifications
            
            return redirect('deposit_success')  # Redirect to a success page

    else:
        form = DepositForm()

    return render(request, 'core/deposit.html', {'form': form, 'account': account})