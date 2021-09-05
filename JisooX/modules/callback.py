from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"⚡𝐊𝐆𝐌𝐔𝐒𝐈𝐂⚡
ᴘᴇɴɢᴀᴛᴜʀᴀɴ
1) ᴊᴀᴅɪᴋᴀɴ ʙᴏᴛ sᴇʙᴀɢᴀɪ ᴀᴅᴍɪɴ
2) ᴍᴜʟᴀɪ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ
3) ᴋɪʀɪᴍ ᴘᴇʀɪɴᴛᴀʜ » /userbotjoin
➢ ᴊɪᴋᴀ ᴀssɪsᴛᴀɴᴛ ᴛᴇʟᴀʜ ʙᴇʀɢᴀʙᴜɴɢ sᴇʟᴀᴍᴀᴛ ᴍᴇɴɪᴋᴍᴀᴛɪ.
➢ ᴊɪᴋᴀ ᴀssɪsᴛᴀɴᴛ ᴛɪᴅᴀᴋ ʙɪsᴀ ʙᴇʀɢᴀʙᴜɴɢ,sɪʟᴀᴋᴀɴ ᴍᴀsᴜᴋᴀɴ @KGAssistant ᴋᴇ ɢʀᴜᴘ ᴀɴᴅᴀ sᴇᴄᴀʀᴀ ᴍᴀɴᴜᴀʟ.",
                                reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "ɴᴇxᴛ", callback_data="cbinfo")
                       ]]
                    ))

@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""ᴘᴇʀɪɴᴛᴀʜ sᴇᴍᴜᴀ ᴀɴɢɢᴏᴛᴀ
➢ /play (judul lagu) - ᴜɴᴛᴜᴋ ᴍᴇᴍᴜᴛᴀʀ ʟᴀɢᴜ ʏᴀɴɢ ᴀɴᴅᴀ ᴍɪɴᴛᴀ
➢ /aplay (balas ke audio) - ᴜɴᴛᴜᴋ ᴍᴇᴍᴜᴛᴀʀ ʟᴀɢᴜ ᴅᴀʀɪ ᴀᴜᴅɪᴏ ғɪʟᴇ
➢ /ytplay (judul lagu) - ᴜɴᴛᴜᴋ ᴍᴇᴍᴜᴛᴀʀ ʟᴀɢᴜ ʏᴀɴɢ ᴀɴᴅᴀ ᴍɪɴᴛᴀ ᴛᴀɴᴘᴀ ᴘɪʟɪʜᴀɴ
➢ /song (judul lagu) - ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ʟᴀɢᴜ ᴅᴀʀɪ ʏᴏᴜᴛᴜʙᴇ
➢ /vsong (judul video) - ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ᴅᴀʀɪ ʏᴏᴜᴛᴜʙᴇ
➢ /lyrics (judul lagu) ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ʟɪʀɪᴋ ʟᴀɢᴜ
➢ /search (judul lagu/video) - ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ʟɪɴᴋ ᴅɪ ʏᴏᴜᴛᴜʙᴇ ᴅᴇɴɢᴀɴ ᴅᴇᴛᴀɪʟ<b>
</b>\n\nᴘᴇʀɪɴᴛᴀʜ sᴇᴍᴜᴀ ᴀᴅᴍɪɴ ɢʀᴜᴘ
➢ /pause - ᴜɴᴛᴜᴋ ᴍᴇɴᴊᴇᴅᴀ ᴘᴇᴍᴜᴛᴀʀᴀɴ ʟᴀɢᴜ
➢ /resume - ᴜɴᴛᴜᴋ ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ ᴘᴇᴍᴜᴛᴀʀᴀɴ ʟᴀɢᴜ
➢ /skip - ᴜɴᴛᴜᴋ ᴍᴇʟᴏᴍᴘᴀᴛɪ ᴋᴇ ʟᴀɢᴜ sᴇʟᴀɴᴊᴜᴛɴʏᴀ
➢ /end - ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀʜᴇɴᴛɪᴋᴀɴ ᴘᴇᴍᴜᴛᴀʀᴀɴ ʟᴀɢᴜ
➢ /reload - ᴜɴᴛᴜᴋ sᴇɢᴀʀᴋᴀɴ ᴅᴀғᴛᴀʀ ᴀᴅᴍɪɴ""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ᴋᴇᴍʙᴀʟɪ", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )
