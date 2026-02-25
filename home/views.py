from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Expense, Profile
from decimal import Decimal, InvalidOperation

@login_required(login_url='/admin/login/')
def home(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    expenses = Expense.objects.filter(user=request.user).order_by('-created_at')
    
    if request.method == 'POST':
        text = request.POST.get('text')
        amount_str = request.POST.get('amount')
        expense_type = request.POST.get('expense_type')

        try:
            amount = Decimal(amount_str)
            Expense.objects.create(
                user=request.user,
                name=text,
                amount=amount,
                expense_type=expense_type
            )
            messages.success(request, "¡Transacción guardada y balance actualizado!")
        except (InvalidOperation, ValueError):
            messages.error(request, "Error: El monto ingresado no es válido.")
            
        return redirect('/')
    
    return render(request, 'home.html', {'profile': profile, 'expenses': expenses})