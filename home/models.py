from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

# Usamos constantes para evitar errores de dedo (Typos)
TRANSACTION_TYPES = (
    ('positive', 'Ingreso'),
    ('negative', 'Egreso'),
)

class Profile(models.Model):
    # OneToOneField es mejor aquí: un usuario tiene UN perfil único
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # DecimalField para precisión financiera exacta
    income = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    
    # Nota: expense y balance se podrían calcular dinámicamente, 
    # pero si los dejas aquí, asegúrate de que sean Decimal.
    expense = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"Perfil de {self.user.username} - Balance: {self.balance}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    name = models.CharField(max_length=100, verbose_name="Concepto")
    
    # Monto con validación para que no sea negativo
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    
    expense_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    
    # Un ingeniero siempre sabe CUÁNDO ocurrió algo
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.expense_type}): ${self.amount}"

    class Meta:
        verbose_name = "Gasto/Ingreso"
        verbose_name_plural = "Gastos e Ingresos"
        ordering = ['-created_at'] # Los más recientes primero