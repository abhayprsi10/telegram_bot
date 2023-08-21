import telebot
from datetime import datetime 

token = "bot_token"

bot= telebot.TeleBot(token)

@bot.message_handler(['start','hello'])
def start(msg):
  bot.reply_to(msg,"welcome to apsbot")

@bot.message_handler(['help'])
def start(msg):
  bot.reply_to(msg,""" /start and /hello ->greetings
  /help -> get all the commands list 
  /time  -> get date and time information
  you can use it as a calculator as well""")

@bot.message_handler(['time','time?','time ?'])
def time(msg):
  cur=datetime.now()

  # dt=cur.strftime("%d/%m/%Y")
  dt=cur.strftime("%d/%B/%Y")

  # tm=cur.strftime("%H:%M:%S")
  tm=cur.strftime("%I:%M:%S %p")

  bot.reply_to(msg,"Date --> "+dt+"\nTime --> "+tm)


# @bot.message_handler(['delete'])
# def delete(msg):
#   # bot=telebot.telebot(token)
  
#   updates=bot.get_updates()
#   chat_id=updates[-1].message.chat_id
#   msg_id=updates[-1].message.message_id   

#   bot.delete_message(chat_id=chat_id,message_id=msg_id)
#   print("the msg has been deleted")


@bot.message_handler()
def custom(msg):
  try:
    ans=eval(msg.text.strip())
  except Exception as e:
    ans="this can't be evaluated" 

  bot.reply_to(msg,ans) 




bot.polling()