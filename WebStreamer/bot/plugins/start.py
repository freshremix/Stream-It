from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#A New User Started Using Your Bot: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id})"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry Sir, You are Not Allowed to use me. Contact my [Support Group](https://t.me/fluxbots).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Please Join My Updates Channel To Use Me!🔐\n\n Due To Overload, Only Channel Subscribers Can Use Me!!**",
                    reply_markup=InlineKeyboardMarkup(
                       [
                            [
                                InlineKeyboardButton("📢 Join Updates Channel 📢", url=f"t.me/{Var.UPDATES_CHANNEL}")
                            ],
                       ]
 
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="Something Went Wrong. Contact my [Support Group](https://t.me/fluxsupport).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text="\n<b>👋Hi There! \n\n✨ I'm A Telegram Bot 🤖 That Can Generate Permanent Download 📥 Links 📎 For Provided Telegram File/Media.\n\nClick /help For More Information Regarding Bot.\n\n🧑‍💻 Developer : @rulebreakerzzz \n⚡️ Channel : @fluxbots \n👮‍♂️ Support : @fluxsupport </b>\n\n ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(' Channel ', url='t.me/fluxbots'), InlineKeyboardButton(' Support ', url='t.me/fluxsupport')],
                    [InlineKeyboardButton(' Developer ', url='t.me/rulebreakerzzz'), InlineKeyboardButton(' Source ', url='https://bit.ly/flux-streamer')]
                ]
            ),
            disable_web_page_preview=True
        )
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry Sir, You Are Not Allowed To Use Me. Contact My [Developer](t.me/rulebreakerzzz).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Please Join My Updates Channel To Use This Bot!\n\nDue to Overload, Only Channel Subscribers Can Use This Bot!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("📢 Join Updates Channel 📢", url=f"t.me/{Var.UPDATES_CHANNEL}")
                            ],

                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="Something went Wrong. Contact my [Developer](t.me/rulebreakerzzz).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text = """\n\n <b>Your Permanent Download Link 📎 Has Been Generated.</b>\n
<b>📂 File Name :</b> {}\n
<b>📦 File Size :</b> {}\n
<b>📎 Download Link :</b> {}\n
<b>Permanent Download Link Is Generatd</b>\n
©⚡️Channel : @fluxbots """
        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Download Link  📥", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#A New User Started Using Your Bot: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id})"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sorry Sir, You are Not Allowed to Use Me. Contact my [Developer](https://t.me/rulebreakerzzz).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                reply_markup=InlineKeyboardMarkup(
                  [
                            [
                                InlineKeyboardButton("📢 Join Updates Channel 📢", url=f"t.me/{Var.UPDATES_CHANNEL}")
                            ],

                  ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [Developer](https://t.me/rulebreakerzzz).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="📌**It's Not That Tough 😒😒!\n\n• Send Me Any Telegram File/Media & I'll Provide You The Permanent Download Link...\n\n• Provided Link Can Be Used To Download/Stream Files Through My Server.\n\n• For Streaming, Just Copy The Mono Link And Paste It In Your Video Player.\n\n• Also Supported in Channels!\n\n© @rulebreakerzzz | @fluxbots**", 
  parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(' Channel ', url='t.me/fluxbots'), InlineKeyboardButton(' Support ', url='t.me/fluxsupport')],
                [InlineKeyboardButton(' Developer ', url='t.me/rulebreakerzzz'), InlineKeyboardButton(' Source ', url='https://github.com/workforce-bot4917/StreamIt')]
            ]
        )
    )

@StreamBot.on_message(filters.command('about') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#A New User Started Using Your Bot: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id})"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sorry Sir, You are Banned to use me. Contact my [Developer](https://t.me/rulebreakerzzz).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                reply_markup=InlineKeyboardMarkup(
                [
                            [
                                InlineKeyboardButton("📢 Join Updates Channel 📢", url=f"t.me/{Var.UPDATES_CHANNEL}")
                            ],

                ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [Developer](https://t.me/rulebreakerzzz).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""**🤖 Bot : FluxStream\n\n🔑 Version : 1.9.5\n\n♻️ Source : Click Below\n\n👑 Github : Click Below\n\n🧑‍💻 Developer : 亗 PROFESSOR 亗 \n\n✨ Last Updated : 18-Oct-21 \n\n  **""", 
  parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('   ♻️ Source       ', url='https://bit.ly/flux-streamer'), InlineKeyboardButton('   👑 Github   ', url='https://github.com/fluxbots')],
                [InlineKeyboardButton('  🧑‍💻 Developer  ', url='t.me/rulebreakerzzz'), InlineKeyboardButton('   🔰 Channel     ', url='t.me/fluxbots')]
            ]
        )
    )
    
@StreamBot.on_message(filters.command('channel') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#A New User Started Using Your Bot: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id})"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sorry Sir, You are Not Allowed To Use Me. Contact my [Developer](https://t.me/rulebreakerzzz).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                reply_markup=InlineKeyboardMarkup(
               [
                            [
                                InlineKeyboardButton("📢 Join Updates Channel 📢", url=f"t.me/{Var.UPDATES_CHANNEL}")
                            ],
                ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [Developer](https://t.me/rulebreakerzzz).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""**\n 🍀 Want To Get Updated ✨ About New Bots And Updates.🍀**""",
  parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('📢  Join Updates Channel  📢', url='t.me/fluxbots')]
            ]
        )
    )
@StreamBot.on_message(filters.command('support') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sorry Sir, You are Banned to use me. Contact my [Developer](https://t.me/rulebreakerzzz).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                reply_markup=InlineKeyboardMarkup(
               [
                            [
                                InlineKeyboardButton("📢 Join Updates Channel 📢", url=f"t.me/{Var.UPDATES_CHANNEL}")
                            ],

                ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [Developer](https://t.me/rulebreakerzzz).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""**\n ✨ Want to Request A Feature/Bot or Report A Bug To Developers ? ✨**""", 
  parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('💬 Support Group 💬', url='t.me/fluxsupport')]
            ]
        )
    )
@StreamBot.on_message(filters.command('dev') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sorry Sir, You are Banned to use me. Contact my [Developer](https://t.me/rulebreakerzzz).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                reply_markup=InlineKeyboardMarkup(
               [
                            [
                                InlineKeyboardButton("📢 Join Updates Channel 📢", url=f"t.me/{Var.UPDATES_CHANNEL}")
                            ],

                ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [Developer](https://t.me/rulebreakerzzz).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""**\n 🤪 I Won't Reply Mostly But Then Also I've to Complete The Formality As Other Devs Are Giving Their UserID.✌️**""", 
  parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('⚜️ Godfather ⚜️', url='t.me/rulebreakerzzz')]
            ]
        )
    )


       
