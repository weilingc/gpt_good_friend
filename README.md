# gpt good friend

ngrok, fastAPI, LINE BOT, openai

# System Requirements
* Ubuntu
* Python 3.8

# Deployments

``` virtualenv (new folder)```
``` source bin/activate ```
``` pip install -r requirements ```
``` apt install ngrok ```


* 啟動 fastAPI 服務
``` uvicorn main:app --reload ```

* 啟動 ngrok
``` ngrok http 8000```

* LINE Developer
console > Basci settings > Channel secret > Issue settings.py LINE_BOT_SECRET = 'line bot secret'
console > Message API > Webhook settings > Webhook URL (https://xxxxxx.ngrok.io/)
console > Message API > Channel access token > Channel access token > Issue settings.py LINE_BOT_TOKEN = 'line bot token'

* OpenAI
https://beta.openai.com/account/api-keys > Create new secret Key > setting.py OPENAI_API_KEY = 'openai secret key'




