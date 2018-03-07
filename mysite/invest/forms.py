from django import forms
import time

class ChooseForm(forms.Form):
    company = forms.CharField(label='company', max_length=100)
    date = forms.DateField(label='date', initial=time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y")))

class chooseCompany(forms.Form):
	selectCompany = forms.CharField(label='selectCompany', max_length=100)
