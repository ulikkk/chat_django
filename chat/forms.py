from django import forms
from django.contrib.auth import get_user_model

from chat.models import ChatMessage

class MessageForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=get_user_model().objects.all(),
        disabled=True,
    )

    class Meta:
        model = ChatMessage
        fields = ['message', 'user', ]
