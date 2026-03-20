import telebot
from telebot import types

API_TOKEN = 'YOUR_API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = "Welcome to the Taxi Booking Bot!\nPlease choose an option:"  
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Book a Taxi")
    item2 = types.KeyboardButton("Cancel Booking")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Book a Taxi")
def book_taxi(message):
    booking_message = "Please select your pickup location:"  
    # Define inline buttons for location selection
    markup = types.InlineKeyboardMarkup()  
    button1 = types.InlineKeyboardButton("Location A", callback_data="location_a")
    button2 = types.InlineKeyboardButton("Location B", callback_data="location_b")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, booking_message, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "location_a":
        bot.send_message(call.message.chat.id, "You have selected Location A.")
    elif call.data == "location_b":
        bot.send_message(call.message.chat.id, "You have selected Location B.")

bot.polling()