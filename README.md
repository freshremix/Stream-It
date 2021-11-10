# <p align="center"><h1> Stream-It </h1></p>
<p align="center">
    <a href="https://t.me/streamer_fluxbot/">
        <img src="https://telegra.ph/file/568dc6e14c0fb1cf56666.png" height="200" width="200" alt="FluxStreamerBot">
    </a>
</p>
<h4> ✨ I'm A Telegram Bot 🤖 That Can Generate Permanent Download 📥 Links 📎 For Provided Telegram File/Media.</h4>

* **Language:** [Python3](https://www.python.org)
* **Library:** [Pyrogram](https://docs.pyrogram.org)

### Features:
- Just Send Any Telegram File/Media And It Will Provide You A Permanent Download Link.
- In Channel Add Bot as Admin with Edit Rights And It Will Directly Generate Download Link.
- Just Copy The MonoLink And Paste In Your Video Player For Streaming.
- Force Subscription Of Channel Available.
- Awesome Interface

### Demo Bot:
<a href="https://t.me/streamer_fluxbot/"><img src="https://img.shields.io/badge/Demo-Telegram%20Bot-blue.svg?logo=telegram"></a>

## Configs:
- `API_ID` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.
- `API_HASH` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.
- `BOT_TOKEN` : Get the bot token from [@BotFather](https://telegram.dog/BotFather)
- `BIN_CHANNEL` : Create a new group (private/public), add [@missrose_bot](https://telegram.dog/MissRose_bot) as admin to the channel and type /id. Now copy paste the ID into this field.
- `OWNER_ID` : Your Telegram User ID
- `DATABASE_URL` : MongoDB URI for saving User IDs when they first Start the Bot. We will use that for Broadcasting to them. I will try to add more features related with Database. If you need help to get the URI you can ask in [Me Telegram](https://t.me/rulebreakerzzz).
- `UPDATES_CHANNEL` : Put a Public Channel Username, so every user have to Join that channel to use the bot. Must add bot to channel as Admin to work properly.
- `BANNED_CHANNELS` : Put IDs of Banned Channels where bot will not work. You can add multiple IDs & separate with <kbd>Space</kbd>.
- `SLEEP_THRESHOLD` : Set a sleep threshold for flood wait exceptions happening globally in this telegram bot instance, below which any request that raises a flood wait will be automatically invoked again after sleeping for the required amount of time. Flood wait exceptions requiring higher waiting times will be raised. Defaults to 60 seconds.
- `WORKERS` : Number of maximum concurrent workers for handling incoming updates. Defaults to `3`
- `PORT` : The port that you want your webapp to be listened to. Defaults to `8080`
- `WEB_SERVER_BIND_ADDRESS` : Your server bind adress. Defauls to `0.0.0.0`
- `NO_PORT` : If you don't want your port to be displayed. You should point your `PORT` to `80` (http) or `443` (https) for the links to work. Ignore this if you're on Heroku.
- `FQDN` :  A Fully Qualified Domain Name if present. Defaults to `WEB_SERVER_BIND_ADDRESS` </details>


## Deploy:

### Deploy Straight To Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Flux-Inc/Stream-It/)

Then Go To The <a href="#mandatory-vars">variables tab</a> for more info on setting up environmental variables. </details>

### Host it on VPS Locally :


```py
git clone https://github.com/Flux-Inc/Stream-It
cd Stream-It
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m WebStreamer
```
and to stop the whole bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

## Commands:
```
start - Start the bot
help - Get Help
about - About The Bot
channel - Updates Channel
support - Support Group
dev - Developer
broadcast - Broadcast Message [Owner]

```
##                                                                Developer : 亗 𝗣𝗥𝗢𝗙𝗘𝗦𝗦𝗢𝗥 亗 
<p align="center">
    <a href="https://t.me/rulebreakerzzz/">
        <img src="https://telegra.ph/file/0c04d249c7d383cd1f8d8.png" height="400" width="400" alt="FluxStreamerBot">
    </a>
</p>
