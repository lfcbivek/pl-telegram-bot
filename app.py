from dotenv import load_dotenv
from fixtures import getFixtures
load_dotenv()
from standings import getStandings
import os
from telegram.ext import Updater, CommandHandler
from fpl_profile import FPLProfile

def standings(update,context):
    
    getStandings()
    # print(context.args[0])
    with open("standings.txt","r") as f:
        standings = f.read()
    update.message.reply_text(standings)
 
def fixtures(update,context):
    try:
        try:
            getFixtures(context.args[0])
        
        except IndexError:
            getFixtures(1)    
        with open("fixtures.txt","r") as f:
            fixtures = f.read()
        update.message.reply_text(fixtures)
        
    except (KeyError) as e:
        update.message.reply_text("Invalid command format")
    
    
def fpl(update,context):
    FPLProfile(context.args[0])
    with open("fpl_profile.txt","r") as f:
        fpl_data = f.read()
    update.message.reply_text(fpl_data)
   
def main():    
    updater = Updater(os.environ["BOT_TOKEN"],use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('standings',standings))
    dp.add_handler(CommandHandler('fixtures',fixtures))
    dp.add_handler(CommandHandler('fpl',fpl))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(os.environ["PORT"]),
                          url_path=os.environ["BOT_TOKEN"])
    updater.bot.setWebhook('https://pl-telegram-bot.herokuapp.com/' + os.environ["BOT_TOKEN"])
    updater.idle()
    
if __name__ == '__main__':
    main()