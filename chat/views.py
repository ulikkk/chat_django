from django.views import generic
from chat.forms import MessageForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from chat.models import ChatMessage

class ChatView(generic.View):
    def get(self, request):
        # We want to show the last 10 messages, ordered most-recent-last
        chat_queryset = ChatMessage.objects.order_by("-created")[:10]
        chat_message_count = len(chat_queryset)
        if chat_message_count > 0:
            first_message_id = chat_queryset[len(chat_queryset)-1].id
        else:
            first_message_id = -1
        previous_id = -1
        if first_message_id != -1:
            try:
                previous_id = ChatMessage.objects.filter(pk__lt=first_message_id).order_by("-pk")[:1][0].id
            except IndexError:
                previous_id = -1
        chat_messages = reversed(chat_queryset)

        return render(request, "chat/chat_itself.html", {
            'chat_messages': chat_messages,
            'first_message_id' : previous_id,
        })
