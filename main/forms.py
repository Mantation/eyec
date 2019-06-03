from django import forms
from .models import Messages

class MessagesForm(forms.ModelForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={ 'rows': 10}),required=True)
    class Meta:
        model = Messages
        fieds = ('firstname','lastname','email','message')
        exclude = ['notes_id']
        #include = ['notes','Profile_id','pub_date',]
