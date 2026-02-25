from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Expense, Profile
from decimal import Decimal

@receiver(post_save, sender=Expense)
def update_profile_balance(sender, instance, created, **kwargs):
    """
    Sistema de automatización: Actualiza el perfil financiero 
    cada vez que se crea un nuevo registro de gasto/ingreso.
    """
    if created:  # Solo si el registro es nuevo
        profile, _ = Profile.objects.get_or_create(user=instance.user)
        
        if instance.expense_type.lower() == 'positive':
            profile.balance += instance.amount
            profile.income += instance.amount
        else:
            profile.balance -= instance.amount
            profile.expense += instance.amount
            
        profile.save()