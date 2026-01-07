from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile, Expense

class ProfileModelTest(TestCase):
    """Tests para el modelo Profile"""
    
    def setUp(self):
        """Configuración inicial - se ejecuta antes de cada test"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            balance=1000,
            expense=200,
            income=1200
        )
    
    def test_profile_creation(self):
        """Test: Verificar que el perfil se crea correctamente"""
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.balance, 1000)
        self.assertEqual(self.profile.expense, 200)
        self.assertEqual(self.profile.income, 1200)
    
    """def test_profile_str(self):
        Test: Verificar la representación en string del perfil
        # Si tienes un método __str__ en tu modelo Profile
        self.assertEqual(str(self.profile), 'testuser')"""


class ExpenseModelTest(TestCase):
    """Tests para el modelo Expense"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.expense = Expense.objects.create(
            user=self.user,
            name='Compra supermercado',
            amount=150.50,
            expense_type='Negative'
        )
    
    def test_expense_creation(self):
        """Test: Verificar que el gasto se crea correctamente"""
        self.assertEqual(self.expense.name, 'Compra supermercado')
        self.assertEqual(self.expense.amount, 150.50)
        self.assertEqual(self.expense.expense_type, 'Negative')
        self.assertEqual(self.expense.user, self.user)


class HomeViewTest(TestCase):
    """Tests para la vista principal"""
    
    def setUp(self):
        """Crear usuario y cliente para hacer requests"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            balance=0,
            expense=0,
            income=0
        )
    
    def test_home_view_without_login(self):
        """Test: Usuario no autenticado debe ser redirigido al login"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # 302 = Redirect
        self.assertIn('/admin/login/', response['Location'])
    
    """def test_home_view_with_login(self):
       Test: Usuario autenticado puede ver la página
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # 200 = OK
        self.assertContains(response, 'testuser')  # Verificar que aparece el username"""
    
    def test_add_expense_negative(self):
        """Test: Agregar un gasto (Negative) reduce el balance"""
        self.client.login(username='testuser', password='testpass123')
        
        # Recargar el perfil para asegurar que tiene el balance correcto
        self.profile.refresh_from_db()
        initial_balance = self.profile.balance if self.profile.balance is not None else 0
        
        # Hacer POST para agregar gasto
        response = self.client.post('/', {
            'text': 'Comida',
            'amount': '50',
            'expense_type': 'Negative'
        })
        
        # Verificar redirección
        self.assertEqual(response.status_code, 302)
        
        # Recargar el perfil desde la BD
        self.profile.refresh_from_db()
        
        # Verificar que el balance disminuyó
        self.assertEqual(self.profile.balance, initial_balance - 50)
        self.assertEqual(self.profile.expense, 50)
        
        # Verificar que el gasto se guardó
        expense = Expense.objects.filter(user=self.user, name='Comida').first()
        self.assertIsNotNone(expense)
        self.assertEqual(expense.amount, 50)
    
    def test_add_income_positive(self):
        """Test: Agregar un ingreso (Positive) aumenta el balance"""
        self.client.login(username='testuser', password='testpass123')
        
        initial_balance = self.profile.balance
        
        response = self.client.post('/', {
            'text': 'Salario',
            'amount': '1000',
            'expense_type': 'Positive'
        })
        
        self.assertEqual(response.status_code, 302)
        
        self.profile.refresh_from_db()
        
        # Verificar que el balance aumentó
        self.assertEqual(self.profile.balance, initial_balance + 1000)
        
        # Verificar que el ingreso se guardó
        income = Expense.objects.filter(user=self.user, name='Salario').first()
        self.assertIsNotNone(income)
        self.assertEqual(income.expense_type, 'Positive')


class UserIntegrationTest(TestCase):
    """Tests de integración - Flujo completo de usuario"""
    
    def test_complete_user_flow(self):
        """Test: Flujo completo - Crear usuario, agregar gastos e ingresos"""
        # 1. Crear usuario
        user = User.objects.create_user(username='john', password='pass123')
        profile = Profile.objects.create(
            user=user,
            balance=0,
            expense=0,
            income=0
        )
        
        # 2. Login
        client = Client()
        logged_in = client.login(username='john', password='pass123')
        self.assertTrue(logged_in)
        
        # 3. Agregar ingreso
        client.post('/', {
            'text': 'Salario',
            'amount': '2000',
            'expense_type': 'Positive'
        })
        
        # 4. Agregar gastos
        client.post('/', {
            'text': 'Renta',
            'amount': '500',
            'expense_type': 'Negative'
        })
        
        client.post('/', {
            'text': 'Comida',
            'amount': '300',
            'expense_type': 'Negative'
        })
        
        # 5. Verificar balance final
        profile.refresh_from_db()
        expected_balance = 2000 - 500 - 300  # = 1200
        self.assertEqual(profile.balance, expected_balance)
        
        # 6. Verificar que hay 3 transacciones
        total_expenses = Expense.objects.filter(user=user).count()
        self.assertEqual(total_expenses, 3)