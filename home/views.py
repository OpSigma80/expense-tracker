from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='/admin/login/')
def home(request):
    profile = Profile.objects.filter(user=request.user).first()
    
    # Si el usuario no tiene perfil, crear uno automáticamente
    if not profile:
        profile = Profile.objects.create(
            user=request.user, 
            balance=0, 
            expense=0,
            income=0  # ← Campo agregado
        )
    
    expenses = Expense.objects.filter(user=request.user)
    
    if request.method == 'POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type')
        
        expense = Expense(name=text, amount=amount, expense_type=expense_type, user=request.user)
        expense.save()
        
        if expense_type == 'Positive':
            profile.balance += float(amount)
        else:
            profile.expense += float(amount)
            profile.balance -= float(amount)
        profile.save()
        return redirect('/')
    
    context = {'profile': profile, 'expenses': expenses}
    return render(request, 'home.html', context)