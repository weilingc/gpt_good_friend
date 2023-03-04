from fastapi import FastAPI, Request, HTTPException
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import openai
import settings

openai.api_key = settings.OPENAI_API_KEY
line_bot_api = LineBotApi(settings.LINE_BOT_TOKEN)
handler = WebhookHandler(settings.LINE_BOT_SECRET)

app = FastAPI()


def generate_response(message):
    # Note: you need to be using OpenAI Python v0.27.0 for the code below to work
    conversation = []
    conversation.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
        )
    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    return response['choices'][0]['message']['content'].strip()

@app.post("/")
async def echoBot(request: Request):
    signature = request.headers["X-Line-Signature"]
    body = await request.body()
    try:
        handler.handle(body.decode(), signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Missing Parameters")
    return "OK"


@handler.add(MessageEvent, message=(TextMessage))
def handling_message(event):
    replyToken = event.reply_token
    if isinstance(event.message, TextMessage):
        messages = event.message.text
        ai_response = generate_response(messages)
        echoMessages = TextSendMessage(text=ai_response)
        line_bot_api.reply_message(reply_token=replyToken, messages=echoMessages)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
