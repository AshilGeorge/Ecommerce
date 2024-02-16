from django import forms
from django.contrib.auth.models import User
from ecommerceapp.models import Carts,Orders

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets={
           'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your FirstName'}),
           'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your LastName'}),
           'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your UserName'}),
           'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Pssword'}),
           'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Email'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your UserName'}),
           'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Pssword'})

        }

class CartForm(forms.ModelForm):
    class Meta:
        model=Carts
        fields=['quantity']
        widgets={
            'quantity':forms.NumberInput(attrs={'class':'form-control'})
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=['address','email']
        widgets={
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})


        }
        