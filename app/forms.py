from django import forms
from .models import MY_MO


class MY_FO(forms.ModelForm):
    class Meta:
        model = MY_MO
        fields = ['id','name','email','password'] 
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }
        
            
            
            
          