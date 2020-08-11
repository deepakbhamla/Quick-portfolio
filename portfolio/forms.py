# make sure this is at the top if it isn't already
from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True,)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].widget.attrs['placeholder'] = self.fields['contact_name'].label or ' Name'            
        self.fields['contact_email'].widget.attrs['placeholder'] = self.fields['contact_email'].label or ' Email'    
        self.fields['content'].widget.attrs['placeholder'] = self.fields['content'].label or ' Message'            