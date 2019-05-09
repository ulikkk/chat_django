from django.urls.conf import path

from chat import views

app_name = 'chat'

urlpatterns = [
    path('', views.ChatView.as_view(), name='chat'),
]
