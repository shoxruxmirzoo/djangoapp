import telebot, requests
from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponse
from .models import User
# Create your views here.

bot = telebot.TeleBot(settings.TOKEN)

def web_hook_view(request):
    if request.method == 'POST':
        json_string = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])

        return HttpResponse('OK')

@bot.message_handler(commands = ['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Salom')

@bot.message_handler(command_types = 'text')
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Vachaaach')
