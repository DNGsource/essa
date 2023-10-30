#      .
#    .

import asyncio
import base64
import io
import os
from pathlib import Path
from ShazamAPI import Shazam
from telethon.tl import functions, types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from validators.url import url
from telethon import events
from pytube import YouTube, Search
from essa import essa 
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.tools import media_type
from ..helpers.functions import name_dl, song_dl, video_dl, yt_search
from ..helpers.utils import _catutils, reply_id
from . import BOTLOG, BOTLOG_CHATID
LOGS = logging.getLogger(__name__)

async def DownloadVideo(videoLink, Quality):
    try:
        Result = YouTube(videoLink).streams.order_by('resolution').filter(res=f"{Quality}p", progressive=True).first().download()
        return Result
    except:
        return False

async def DownloadAudio(videoLink):
    try:
        Video = YouTube(videoLink)
        Title = (Video.title).replace('"', '_')
        Title = (Title).replace('/', '_')
        Title = (Title).replace('\\', '_')
        Title = (Title).replace('/', '_')
        Title = (Title).replace(':', '_')
        Title = (Title).replace('*', '_')
        Title = (Title).replace('?', '_')
        Title = (Title).replace('|', '_')
        Title = (Title).replace('>', '_')
        Title = (Title).replace('<', '_')
        Download = Video.streams.filter(type = "audio").last().download(filename=f"{Title}.mp3")
        return Download
    except:
        return False


# #      .
#    .
async def SearchVideo(query):
    Video = Search(query)
    return Video.results


# CODE BY : T.me/E_I_I7
@.on(events.NewMessage(outgoing=True, pattern=r'.تحميل فيديو ?(.*)'))
async def DownloadByURLs(event):
    sender = await event.get_chat()

    Download_info = ((event.message.message).replace(".تحميل فيديو", "")).split(' ')
    order = await event.edit("**جاري تحميل الفيديو...**")
    if len(Download_info) == 3:
        # advanced download
        quality = Download_info[1]
        videoLink = Download_info[2]
        if int(quality) == 144 or int(quality) == 360 or int(quality) == 480 or int(quality) == 720 or int(quality) == 1080:
            GetVideo = await DownloadVideo(videoLink, quality)
            if GetVideo != False:
                Title = GetVideo.replace("/app/", "")
                Title = Title.replace(".mp4", "")
                
                order = await event.edit("**جاري ارسال الفيديو...**")
                sendFile = await event.reply(f'عنوان الفيديو : {Title}', file=f'{GetVideo}')
                order = await event.edit("**تم ارسال.**")
            else:
                order = await event.edit("**هذا الفيديو لا يدعم هذه الجودة. حاول تغيير جودة الفيديو**")
        else:
            order = await event.edit("**بالرجاء اختيار جودة المناسبة 144 - 360 - 480 - 720 - 1080**")
    else:
        # Defualt download 360p
        videoLink = Download_info[1]
        GetVideo = await DownloadVideo(videoLink, 360)
        if GetVideo != False:
            Title = GetVideo.replace("/app/", "")
            Title = Title.replace(".mp4", "")
            
            order = await event.edit("**جاري ارسال الفيديو...**")
            sendFile = await event.reply(f'عنوان الفيديو : {Title}', file=f'{GetVideo}')
            order = await event.edit("**تم ارسال.**")
        else:
            order = await event.edit("**هذا الفيديو لا يدعم الجودة الافتراضية 360. حاول تغيير جودة الفيديو. - 144 - 360 - 480 - 720 - 1080**")


# DOWNLOAD BY URLs senzir
@essa.on(events.NewMessage(outgoing=True, pattern=r'.تحميل صوت ?(.*)'))
async def DownloadAudioByURLs(event):
    sender = await event.get_chat()

    videoLink = ((event.message.message).replace(".تحميل صوت", "")).strip()
    order = await event.edit("**جاري تحميل الصوت...**")


    GetVideo = await DownloadAudio(videoLink)
    if GetVideo != False:
        Title = GetVideo.replace("/app/", "")
        Title = Title.replace(".mp3", "")
        
        order = await event.edit("**جاري ارسال الصوت...**")
        sendFile = await event.reply(f'عنوان الاغنية : {Title}', file=f'{GetVideo}')
        order = await event.edit("**تم ارسال.**")
    else:
        order = await event.edit("**لا يمكن تحميل هذا الفيديو كصوت**")


# SEARCH Video senzir
@essa.on(events.NewMessage(outgoing=True, pattern=r'.بحث فيديو ?(.*)'))
async def DownloadByURLs(event):
    sender = await event.get_chat()

    Download_info = ((event.message.message).replace(".بحث فيديو", "")).split('-')
    order = await event.edit("**جاري البحث...**")

    if len(Download_info) == 3:
        # advanced download
        quality = Download_info[1]
        query = Download_info[2]

        if int(quality) == 144 or int(quality) == 360 or int(quality) == 480 or int(quality) == 720 or int(quality) == 1080:
            GetVideo = await SearchVideo(query)
            videoLink = GetVideo[0].watch_url
            GetVideo_ = await DownloadVideo(str(videoLink), int(quality))


            if GetVideo_ != False:
                Title = GetVideo_.replace("/app/", "")
                Title = Title.replace(".mp4", "")
                
                order = await event.edit("**جاري ارسال الفيديو...**")
                sendFile = await event.reply(f'عنوان الفيديو : {Title}', file=f'{GetVideo_}')
                order = await event.edit("**تم ارسال.**")
            else:
                order = await event.edit("**هذا الفيديو لا يدعم هذه الجودة. حاول تغيير جودة الفيديو**")
        else:
            order = await event.edit("**بالرجاء اختيار جودة المناسبة 144 - 360 - 480 - 720 - 1080**")
    else:
        # Defualt download 360p
        query = Download_info[1]

        GetVideo = await SearchVideo(query)
        videoLink = GetVideo[0].watch_url
        GetVideo_ = await DownloadVideo(videoLink, 360)
        if GetVideo_ != False:
            Title = GetVideo_.replace("/app/", "")
            Title = Title.replace(".mp4", "")
            
            order = await event.edit("**جاري ارسال الفيديو...**")
            sendFile = await event.reply(f'عنوان الفيديو : {Title}', file=f'{GetVideo_}')
            order = await event.edit("**تم ارسال.**")
        else:
            order = await event.edit("**هذا الفيديو لا يدعم الجودة الافتراضية 360. حاول تغيير جودة الفيديو. - 144 - 360 - 480 - 720 - 1080**")



# SEARCH AUDIO senzir
@essa.on(events.NewMessage(outgoing=True, pattern=r'.بحث صوت ?(.*)'))
async def DownloadAudioByURLs(event):
    sender = await event.get_chat()

    query = ((event.message.message).replace(".بحث صوت", "")).strip()
    order = await event.edit("**جاري البحث...**")

    GetVideo = await SearchVideo(query)
    videoLink = GetVideo[0].watch_url
    GetVideo_ = await DownloadAudio(str(videoLink))
    if GetVideo_ != False:
        Title = GetVideo_.replace("/app/", "")
        Title = Title.replace(".mp3", "")
        
        order = await event.edit("**جاري ارسال الصوت...**")
        sendFile = await event.reply(f'عنوان الاغنية : {Title}', file=f'{GetVideo_}')
        order = await event.edit("**تم ارسال.**")
    else:
        order = await event.edit("**لا يمكن تحميل هذا الفيديو كصوت**")


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
  
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(event.chat_id, sandy, caption=sandy.text)
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
        if BOTLOG:
            if DelaySpam is not True:
                if event.is_private:
                    await event.client.send_message(BOTLOG_CHATID, "**⎈ ⦙ التڪـرار  ♽**\n" + f"**⌔︙ تم تنفيذ التكرار بنجاح في ▷** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** {counter} **عدد المرات مع الرسالة أدناه**")
                else:
                    await event.client.send_message(BOTLOG_CHATID, "**⎈ ⦙ التڪـرار  ♽**\n" + f"**⌔︙ تم تنفيذ التكرار بنجاح في ▷** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **مـع** {counter} **عدد المرات مع الرسالة أدناه**")
            elif event.is_private:
                await event.client.send_message(BOTLOG_CHATID, "**⎈ ⦙ التكرار الوقتي 💢**\n" + f"**⌔︙ تم تنفيذ التكرار الوقتي  بنجاح في ▷** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** {counter} **عدد المرات مع الرسالة أدناه مع التأخير** {sleeptimet} ** الثوانـي ⏱**")
            else:
                await event.client.send_message(BOTLOG_CHATID, "**⎈ ⦙ التكرار الوقتي 💢**\n" + f"**⌔︙ تم تنفيذ التكرار الوقتي  بنجاح في ▷** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **مـع** {counter} **عدد المرات مع الرسالة أدناه مع التأخير** {sleeptimet} ** الثوانـي ⏱**")

            sandy = await event.client.send_file(BOTLOG_CHATID, sandy)
            await _catutils.unsavegif(event, sandy)
        return
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    else:
        return
    if DelaySpam is not True:
        if BOTLOG:
            if event.is_private:
                await event.client.send_message(BOTLOG_CHATID, "**⎈ ⦙ التڪـرار  ♽**\n" + f"**⌔︙ تم تنفيذ التكرار بنجاح في ▷** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** {counter} **رسائـل الـ  ✉️ :** \n" + f"⌔︙ `{spam_message}`")
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**⎈ ⦙ التڪـرار  ♽**\n"
                    + f"**⎈ ⦙ تم تنفيذ التكرار بنجاح في ▷** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشـة مـع** {counter} **رسائـل الـ  ✉️ :** \n"
                    + f"⎈ ⦙ `{spam_message}`",
                )
    elif BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⎈ ⦙ التكرار الوقتي 💢**\n"
                + f"**⎈ ⦙ تم تنفيذ التكرار الوقتي  بنجاح في ▷** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** {sleeptimet} seconds and with {counter} **رسائـل الـ  ✉️ :** \n"
                + f"⎈ ⦙ `{spam_message}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⎈ ⦙ التكرار الوقتي 💢**\n"
                + f"**⎈ ⦙ تم تنفيذ التكرار الوقتي  بنجاح في ▷** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشـة مـع** {sleeptimet} **الثوانـي و مـع** {counter} **رسائـل الـ  ✉️ :** \n"
                + f"⎈ ⦙ `{spam_message}`",
            )

