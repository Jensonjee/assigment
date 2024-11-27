from django import forms
from .models import student,facultyreg,report


class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields=('name','email','phone_no','dob','admission_no','course','batch','username','password')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone_no':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.TextInput(attrs={'class':'form-control'}),
            'admission_no':forms.TextInput(attrs={'class':'form-control'}),
            'course':forms.TextInput(attrs={'class':'form-control'}),
            'batch':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }

        
class facultyform(forms.ModelForm):
    class Meta:
        model=facultyreg
        fields=('name','email','phone_no','dob','password')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone_no':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }


class reportform(forms.ModelForm):
    class Meta:
        model=report
        fields=('event','report')
        widgets={
            'event':forms.TextInput(attrs={'class':'form-control'}),
            'report':forms.FileInput(attrs={'class':'form-control'}),
        }
