from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if not field.widget.attrs.get('placeholder'):
                field.widget.attrs['placeholder'] = field.label

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            'firstname',
            'lastname',
            'email',
            'phone',
            'address',
            'city',
            'state',
            'zip_code',
            'country',
            'status',
            'message',
            'notes',
        ]
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'address': forms.Textarea(attrs={'placeholder': 'Address', 'rows': 2}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Zip Code'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'rows': 3}),
            'notes': forms.Textarea(attrs={'placeholder': 'Notes (optional)', 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super(AddRecordForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Only apply form-control if it's not a Select
            if not isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-control'
