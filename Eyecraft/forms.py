from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import LensProduct,CustomerDetails
from django.contrib.auth.models import User


class LensProductForm(forms.ModelForm):
    class Meta:
        model = LensProduct
        fields = ['productName', 'productDesc', 'productPrice', 'productImage', 'productRating', 'productCategory']
    
    import re

def clean_productName(self):
    productName = self.cleaned_data.get('productName')
    if not re.match(r'^[A-Za-z\s\-]+$', productName):
        raise forms.ValidationError("Product name can only contain letters, spaces, and hyphens.")
    return productName


class CustomerForm(UserCreationForm):
    password1=forms.CharField(label="Enter password:",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm password:",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

        labels={
            'username':'Enter Username:',
            'first_name':'Enter First Name:',
            'last_name':'Enter Last Name:',
            'email':'Enter Email:',
        }

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
        
class userAuthentication(AuthenticationForm):
    username=forms.CharField(label="Enter Username:",widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="Enter Password:",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','password']


from django import forms
from django.core.exceptions import ValidationError
import re
from .models import CustomerDetails

class customerDetailsform(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ['custname', 'custEmail', 'custAddress', 'custcontact', 'pincode']

    # ✅ Email Validation
    def clean_custEmail(self):
        email = self.cleaned_data.get("custEmail")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):  # ✅ Basic Email Format Check
            raise ValidationError("Enter a valid email address.")
        return email

    # ✅ Pincode Validation
    def clean_pincode(self):
        pincode = self.cleaned_data.get("pincode")
        if not re.match(r"^\d{6}$", pincode):  # ✅ Only 6-Digit Numbers Allowed
            raise ValidationError("Enter a valid 6-digit PIN code.")
        return pincode





