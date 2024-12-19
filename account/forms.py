from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'id': 'email',
        'type': 'email',
        'placeholder': 'Email'
      }
    )
  )
  password = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'id': 'password',
        'type': 'password',
        'placeholder': 'Password'
      }
    )
  )

from django.core.mail import send_mail
from django.conf import settings

class ContactUsForm(forms.Form):
  full_name = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "id": "full_name",
        "placeholder": "Enter Your Full Name",
        "type": "text",
      }
    ),
  )

  email = forms.EmailField(
    widget=forms.TextInput(
      attrs={
        "id": "email",
        "placeholder": "Enter your Email address",
        "type": "email",
      }
    )
  )
  message = forms.CharField(
    widget=forms.Textarea(
      attrs={
        "id": "message",
        'placeholder': "Write Us Your Question Here..."
      }
    )
  )

  def send(self):
    message = f"Full Name: {self.cleaned_data['full_name']}\n"
    message += f"Email: {self.cleaned_data['email']}\n"
    message += f"Message: {self.cleaned_data['message']}\n"

    send_mail(
      "Contact Us Form Submission",
      message,
      from_email=settings.EMAIL_HOST_USER,
      recipient_list=[settings.EMAIL_HOST_USER],
      fail_silently=False,
    )
