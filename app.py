from dotenv import load_dotenv
from fixtures import getFixtures
load_dotenv()
from standings import getStandings
import os
from telegram.ext import Updater, CommandHandler
from fpl_profile import FPLProfile

datas = {
    "dawadi":1738049,
    "chhetri": 4354,
    "ray": 723092,
    "neku": 670039,
    "macee":21350,
    "sandesh": 269642,
    "joshi":202071,
    "syame": 16273,
    "kidd": 40438,
    "model": 65429,
    "bivek": 2703
    
}


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
    id = context.args[0]
    if isinstance(context.args[0], str):
        try:
            if datas[context.args[0]]:
                id = datas[context.args[0]]
        except:
            pass    
    FPLProfile(id)
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