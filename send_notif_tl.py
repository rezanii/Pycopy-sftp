import requests

TELEGRAM_BOT_TOKEN = '466843477:AAHTmU4SvOwNaNrnSqo3KgoKtfecOXvRnNE'
chat_id = "-578006901"
base_url = "https://api.telegram.org/bot" + TELEGRAM_BOT_TOKEN

b = place_project_bid(session)
if b:
    print('*********************')
    print(("Tes placed: %s" % b))
    parameters = {
        "chat_id" : chat_id,
        "text" : message,     
    }
    resp = requests.get(base_url + "/sendMessage", data = parameters)