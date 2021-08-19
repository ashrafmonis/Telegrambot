from telegram import*
from telegram.ext import*
bot=Bot("1998089241:AAG5-g3tmqwJBHc7VYgoUww6j6lyRBs-kss")
updater=Updater("1998089241:AAG5-g3tmqwJBHc7VYgoUww6j6lyRBs-kss",use_context=True)
dispatcher=updater.dispatcher

def intro(update:Update, context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi I am a Datascientist,"
             "How can i help you?",
        )
start=CommandHandler('Hi',intro)
dispatcher.add_handler(start)
updater.start_polling()
print(bot.get_me())
def detail(update:Update, context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Great this is a good career choice in todays world it highly demanded,"
             "becouse many companies take the feedback by using the Data Science Technology.",
        )
start1=CommandHandler('i_want_make_career_Datascience',detail)
dispatcher.add_handler(start1)
updater.start_polling()

def profile(update:Update, context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="There are three profiles in Datascince:"
             "                            1-Data scientist"
             "                            2-Data engineer"
             "                            3-Data analyst.",
        )
start2=CommandHandler('positions',profile)
dispatcher.add_handler(start2)
updater.start_polling()

def Role_responsibilities(update:Update, context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Data scientists: Design data modeling processes to create algorithms and predictive models and perform custom analysis.,"
"Data analysts: Manipulate large data sets and use them to identify trends and reach meaningful conclusions to inform strategic business decisions.,"
"Data engineers: Clean, aggregate, and organize data from disparate sources and transfer it to data warehouses.,"
"Business intelligence specialists: Identify trends in data sets."
"Data architects: Design, create, and manage an organization’s data architecture.",
        )
start3=CommandHandler('Roles',Role_responsibilities)
dispatcher.add_handler(start3)
updater.start_polling()

def Skills(update:Update, context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="1-math and statistics"
             "2-programming in R or Python language"  
             "3-SQL"
             "4-Data structure and algorithms "
             "5-Ms Exel(Adv)"
             "6-probability and permutation combination"
             "7-Machine Learning 8-Deep Learning.",
        )
start4=CommandHandler('skills_required',Skills)
dispatcher.add_handler(start4)
updater.start_polling()