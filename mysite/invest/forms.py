from django import forms
import time

class addCompanyData(forms.Form):
    company = forms.CharField(label='company', max_length=100)
    date = forms.DateField(label='date', initial=time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y")))
    companyprice = forms.DecimalField(label='companyprice',max_digits=10,decimal_places=2)

class deleteCompanyData(forms.Form):
    company = forms.CharField(label='company', max_length=100)
    date = forms.DateField(label='date', initial=time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y")))

class deleteCompanyidData(forms.Form):
    companyid = forms.DecimalField(label='companyid',max_digits=8,decimal_places=0)

class compareCompany(forms.Form):
	selectCompany = forms.CharField(label='selectCompany', max_length=100)
