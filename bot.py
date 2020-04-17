from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
from covid19uncle import GlobalCovid19,ThaiCovid19

app = Flask(__name__)

line_bot_api = LineBotApi('') #Channel access token
handler = WebhookHandler('') #Channel secret Line

thai = ThaiCovid19()

# app route
@app.route("/")
def hello():
    return "Hello World! 23/3/2563 23:16"

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# line route
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=call_back(event.message.text)))


def call_back(message):
    message = message.replace(' ', '')
    message = message.lower()

    res = 'ต้องการอะไร'
    res+= '\n -อัพเดต, update'
    return res

if __name__ == "__main__":
    app.run()

# https://medium.com/@geidtiphong/line-bot-%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%87%E0%B8%B9%E0%B9%80%E0%B8%82%E0%B8%B5%E0%B8%A2%E0%B8%A7%E0%B8%99%E0%B9%89%E0%B8%AD%E0%B8%A2-python-f3947f67cf1b