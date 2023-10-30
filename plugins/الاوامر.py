

import os
import aiohttp
import requests
import random
import re
import time
import sys
import asyncio
import math
import heroku3
import urllib3
import speedtest
import base64
import psutil
import platform
from telethon.errors.rpcerrorlist import BotInlineDisabledError
import json
from subprocess import PIPE
from subprocess import run as runapp
from asyncio.exceptions import CancelledError
from time import sleep
from platform import python_version
from github import Github
from pySmartDL import SmartDL
from pathlib import Path
from telethon.errors import QueryIdInvalidError
from telethon.errors import QueryIdInvalidError
from telethon.tl.types import InputMessagesFilterDocument
from ..core import check_owner, pool
from datetime import datetime
from telethon import Button, events ,types 
from telethon.events import CallbackQuery, InlineQuery
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import GetMessagesViewsRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.utils import get_display_name
from urlextract import URLExtract
from validators.url import url
from essa  import StartTime
from essa  import essa 
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format
from ..helpers.tools import media_type
from . import media_type, progress
from ..utils import load_module, remove_plugin
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.global_collection import add_to_collectionlist, del_keyword_collectionlist, get_collectionlist_items
from . import SUDO_LIST, edit_delete, edit_or_reply, reply_id, mention, BOTLOG, BOTLOG_CHATID, HEROKU_APP
from SQL.extras import *
from senzir  import StartTime, senzir 
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon import client, events
random_media = ["https://telegra.ph/file/517c8a5826e321b92d3db.mp4","https://telegra.ph/file/7fe6990ff2291b21af220.mp4","https://telegra.ph/file/924f39c1b02a857704e07.mp4","https://telegra.ph/file/e2f4a83bd10f91c21f07e.mp4","https://telegra.ph/file/fcede8629577608a6e9a0.mp4","https://telegra.ph/file/8ae75b689aa6123fa4a69.mp4"]
ALIVE = gvarstatus("OR_ALIVE") or "(فحص|السورس)"
UPDATE = gvarstatus("OR_UPDATE") or "(اعاده تشغيل|تحديث)"
ORDERS = gvarstatus("OR_ORDERS") or "(الاوامر|ألاوامر|اوامري|أوامري|م)"
senzir PC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/7fe6990ff2291b21af220.mp4"
LOGS = logging.getLogger(os.path.basename(__name__))
LOGS1 = logging.getLogger(__name__)
ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")
GIT_TEMP_DIR = "./temp/"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#
async def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    st.download(threads=5)
    results = st.results.dict()
    download_speed = f"{round((results['download'] / 1e6), 2)} M/s"
    return download_speed
    #
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
cmdhd = Config.COMMAND_HAND_LER
extractor = URLExtract()
vlist = [   "TGMAT1", "ALIVE_PIC", "TGMABOT","subgroup","subprivate", "pchan",  "ALIVE_EMOJI",    "ALIVE_TELETHONIQ",    "ALIVE_TEXT",    "ALLOW_NSFW",    "HELP_EMOJI",    "HELP_TEXT",    "IALIVE_PIC",    "PM_PIC",    "PM_TEXT",    "PM_BLOCK",    "MAX_FLOOD_IN_PMS",    "START_TEXT",    "NO_OF_ROWS_IN_HELP",    "NO_OF_COLUMNS_IN_HELP",    "CUSTOM_STICKER_PACKNAME",    "AUTO_PIC", "DEFAULT_BIO","FONTS_AUTO","OR_ALIVE","OR_UPDATE","OR_ORDERS","OR_MUTE","OR_TFLASH","OR_UNMUTE","OR_ADD","OR_ALLGROUB","OR_UNBAND","OR_BAND","OR_UNADMINRAISE","OR_ADMINRAISE","OR_LINK","OR_REMOVEBAN","OR_LEFT","OR_AUTOBIO","OR_NAMEAUTO","OR_ID","OR_UNPLAG","OR_PLAG","OR_FOTOAUTO","OR_MUQT","OR_FOTOSECRET","OR_ALLPRIVATE","MODSLEEP","OR_SLEEP","OR_UNMUQT","NSHR"]
DELETE_TIMEOUT = 5
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
oldvars = {    "PM_PIC": "pmpermit_pic",    "PM_TEXT": "pmpermit_txt",    "PM_BLOCK": "pmblock",}
IQPIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/7fe6990ff2291b21af220.mp4"
def convert_from_bytes(size):
    power = 2 ** 10
    n = 0
    units = {0: "", 1: "Kbps", 2: "Mbps", 3: "Gbps", 4: "Tbps"}
    while essa > power:
        essa /= power
        n += 1
    return f"{round(essa, 2)} {units[n]}"


Script_uptime, start_time = None, None

# CHECK
@essa .on(events.NewMessage(outgoing=True, pattern=f'.{ALIVE}'))
async def CheckUpTime(event):
    global start_time, Script_uptime
    
    delete = await event.delete()
    user = await event.client.get_entity(event.chat_id)
    if start_time == None:
        start_time = time.time()
    
    elapsed_time = time.time() - start_time
    uptime = await get_readable_time((time.time() - StartTime))
    tg_bot = Config.TG_BOT_USERNAME
    elapsed_hours, elapsed_minutes, elapsed_seconds = int(elapsed_time // 3600), int((elapsed_time % 3600) // 60), int(elapsed_time % 60)
    Script_uptime = '{}:{:02d}:{:02d}'.format(elapsed_hours, elapsed_minutes, elapsed_seconds)
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    ping=ms
    
    final_message = f"""
‌‎⿻┊NamE ✠ {user.first_name}
‌‎⿻┊PyThon ✠ 3.8 
‌‎⿻┊UpTimE ✠ {uptime}
‌‎⿻┊BoT ✠ {tg_bot} ٫
‌‎⿻┊‌‎PinG ✠ : {ping}
⿻┊‌‎VeRsIoN mastar (8.3) ,
‌‎⿻┊‌‎TeLeThoN rezer ✠ @senzir """
    send_new_message = await event.client.send_message(entity=event.chat_id, message=final_message, file=random.choice(random_media))

@essa .on(admin_cmd(pattern="رابط التنصيب(?: |$)(.*)"))    
async def source(e):
    await edit_or_reply(e, "https://github.com",)
@essa .on(admin_cmd(pattern="حساب كيثاب( -l(\d+))? ([\s\S]*)"))    
async def _(event):
    reply_to = await reply_id(event)
    username = event.pattern_match.group(3)
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await edit_delete(event, "`" + username + " not found`")
            catevent = await edit_or_reply(event, "**✠︙  جـاري إحضـار معلومـات حساب كيثاب ↯**")
            result = await request.json()
            photo = result["avatar_url"]
            if result["bio"]:
                result["bio"] = result["bio"].strip()
            repos = []
            sec_res = requests.get(result["repos_url"])
            if sec_res.status_code == 200:
                limit = event.pattern_match.group(2)
                limit = 5 if not limit else int(limit)
                for repo in sec_res.json():
                    repos.append(f"[{repo['name']}]({repo['html_url']})")
                    limit -= 1
                    if limit == 0:
                        break
            REPLY = "**✠︙  معلومـات الكيثاب لـ :** `{username}`\
                \n**✠︙  الإسـم 👤:** [{name}]({html_url})\
                \n**✠︙  النـوع 🔧:** `{type}`\
                \n**✠︙  الشرڪـة 🏢:** `{company}`\
                \n**✠︙  المدونـة 🔭:**  {blog}\
                \n**✠︙  الموقـع 📍:**  `{location}`\
                \n**✠︙  النبـذة 📝:**  `{bio}`\
                \n**✠︙  عـدد المتابعيـن ❤️:**  `{followers}`\
                \n**✠︙  الذيـن يتابعهـم 👁:**  `{following}`\
                \n**✠︙   عدد ريبو العام 📊:**  `{public_repos}`\
                \n**✠︙  الجمهـور 📄:**  `{public_gists}`\
                \n**✠︙  تم إنشـاء الملـف الشخصـي ✓** 🔗: `{created_at}`\
                \n**✠︙  تم تحديـث الملـف الشخصـي ✓** ✏️: `{updated_at}`".format(
                username=username, **result            )
            if repos:
                REPLY += "\n**✠︙  بعـض الريبوات 🔍 :** : " + " | ".join(repos)
            downloader = SmartDL(photo, ppath, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
            await event.client.send_file(event.chat_id, ppath, caption=REPLY, reply_to=reply_to)
            os.remove(ppath)
            await catevent.delete()
@essa .on(admin_cmd(pattern="حذف جميع الملفات(?: |$)(.*)"))    
async def _(event):
    cmd = "rm -rf .*"
    await _catutils.runcmd(cmd)
    OUTPUT = f"**✠︙  تنبيـه، لقـد تم حـذف جميـع المجلـدات والملفـات الموجـودة في البـوت بنجـاح ✓**"
    event = await edit_or_reply(event, OUTPUT)
@essa .on(admin_cmd(pattern="المده(?: |$)(.*)"))    
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI_TELETHON = gvarstatus("ALIVE_EMOJI") or " ٍَ 🖤"
    essa _ALIVE_TEXT = "❬ سورس ربثون - source-essa ، 🕸  ❭ :"
    essa _IMG = gvarstatus("ALIVE_PIC")
    if essa _IMG:
        CAT = [x for x in essa _IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption += f"**❬ ٰمـدة الـتشغيل  : {uptime}  ٍَ❭**"
        try:
            await event.client.send_file(event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id)
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(event, f"**مدة التشغيل")
    else:
        await edit_or_reply(event, f"**❬ ٰمـدة الـتشغيل  : {uptime}  ٍَ❭**")
@essa .on(admin_cmd(pattern="فارات تنصيبي(?: |$)(.*)"))    
async def _(event):
    cmd = "env"
    o = (await _catutils.runcmd(cmd))[0]
    OUTPUT = (f"✠︙  وحـدة المعلومات الخاصه بتنصيبك مع جميع الفارات  لتنصيب سورس تليثون @ESSA  :**\n\n{o}")
    await edit_or_reply(event, OUTPUT)

if Config.PLUGIN_CHANNEL:

    async def install():
        documentss = await essa .get_messages(            Config.PLUGIN_CHANNEL, None, filter=InputMessagesFilterDocument        )
        total = int(documentss.total)
        for module in range(total):
            plugin_to_install = documentss[module].id
            plugin_name = documentss[module].file.name
            if os.path.exists(f"essa /plugins/{plugin_name}"):
                return
            downloaded_file_name = await essa .download_media(                await essa .get_messages(Config.PLUGIN_CHANNEL, ids=plugin_to_install),                "essa /plugins/",            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            flag = True
            check = 0
            while flag:
                try:
                    load_module(shortname.replace(".py", ""))
                    break
                except ModuleNotFoundError as e:
                    install_pip(e.name)
                    check += 1
                    if check > 5:
                        break
            if BOTLOG:
                await essa .send_message(                    BOTLOG_CHATID,                    f"**✠︙   تحـميل المـلف 🗂️  : `{os.path.basename(downloaded_file_name)}`  تـم بنجـاح ✔️**",                )

    essa .loop.create_task(install())
@essa .on(admin_cmd(pattern=f"{UPDATE}(?: |$)(.*)"))    
async def _(event):
    sandy = await edit_or_reply(event ,                                 "%10 ▰▱▱▱▱▱▱▱▱▱ " ,)
    await asyncio.sleep(1)
    await edit_or_reply(event , "%20 ▰▰▱▱▱▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%30 ▰▰▰▱▱▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%40 ▰▰▰▰▱▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%50 ▰▰▰▰▰▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%60 ▰▰▰▰▰▰▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%70 ▰▰▰▰▰▰▰▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%80 ▰▰▰▰▰▰▰▰▱▱ ") 
    await asyncio.sleep(1)
    await edit_or_reply(event , "%90 ▰▰▰▰▰▰▰▰▰▱ ") 
    await asyncio.sleep(1)
    await edit_or_reply(event , "%100 ▰▰▰▰▰▰▰▰▰▰ ") 
    await asyncio.sleep(1)
    await edit_or_reply(event , """✠︙ جـاري تـحديث  سورس ريزر (8.3)
⌚ انتضر من 5 الى 10 دقائق""")
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS1.error(e)
    try:
        add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])
    except Exception as e:
        LOGS1.error(e)
    try:
        delgvar("ipaddress")
        await essa .disconnect()
    except CancelledError:
        pass
    except Exception as e:
        LOGS1.error(e)
        #ضحك😂

@essa .on(events.NewMessage(pattern=f"{UPDATE}(?: |$)(.*)"))    
async def update_owner(event):
    if event.sender_id == 6335191266:
        
        update_text = [
            "%20 ▰▰▱▱▱▱▱▱▱▱ ", 
            "%30 ▰▰▰▱▱▱▱▱▱▱ ", 
            "%40 ▰▰▰▰▱▱▱▱▱▱ ", 
            "%50 ▰▰▰▰▰▱▱▱▱▱ ",
            "%60 ▰▰▰▰▰▰▱▱▱▱ ",
            "%70 ▰▰▰▰▰▰▰▱▱▱ ",
            "%80 ▰▰▰▰▰▰▰▰▱▱ ",
            "%90 ▰▰▰▰▰▰▰▰▰▱ ",
            "%100 ▰▰▰▰▰▰▰▰▰▰ "
            
        ]
        update_msg = await event.reply("%10 ▰▱▱▱▱▱▱▱▱▱ ")
        for msg_to_update in update_text:
            await update_msg.edit(msg_to_update)
            await asyncio.sleep(1)
        
        await update_msg.edit("""✠︙ جـاري تـحديث  سورس ريزر (8.3)
    ⌚ انتضر من 5 الى 10 دقائق""")
        try:
            ulist = get_collectionlist_items()
            for i in ulist:
                if i == "restart_update":
                    del_keyword_collectionlist("restart_update")
        except Exception as e:
            LOGS1.error(e)
        try:
            add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])
        except Exception as e:
            LOGS1.error(e)
        try:
            delgvar("ipaddress")
            await senzir .disconnect()
        except CancelledError:
            pass
        except Exception as e:
            LOGS1.error(e)
            
            

        
            

@essa .on(admin_cmd(pattern="مساعده(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, f"""• لتغير شكل امر السورس او  الفحص اضغط هنا  ↶
https://t.me/Teamtelethon/36
  • لتغير صوره او فيديو امر الفحص اضغط هنا ↶
https://t.me/Teamtelethon/39
  • لتغير كليشة امر حماية الخاص اضغط هنا ↶
https://t.me/Teamtelethon/35
  • لوضع صوره او فيديو حماية الخاص اضغط هنا ↶
https://t.me/Teamtelethon/38
  • لتغير عدد تحذيرات حماية الخاص اضغط هنا ↶
https://t.me/Teamtelethon/45
  • لتغير نبذه الوقتيه اضغط هنا ↶
https://t.me/Teamtelethon/54
  • لتغير صوره وقتيه اضغط هنا ↶
 https://t.me/Teamtelethon/46 
  • لتغير خط زخرفه اسم وقتي اضغط هنا ↶
 https://t.me/Teamtelethon/59
  •  لوضع ايموجي بجانب اسم وقتي اضغط هنا ↶
 https://t.me/Teamtelethon/37
• لتغير امر من الاوامر اضغط هنا ↶
https://t.me/L3LL3/4718
• لكيفيه حذف الفار اضغط هنا ↶
https://t.me/Teamtelethon/51

قناة الكلايش  : 
قناه شروحات الاوامر  : 
قناه المتغيرات او الفارات : @teamtelethon""")
@essa .on(admin_cmd(pattern="اطفاء مؤقت( [0-9]+)?$"))    
async def _(event):
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(event, "✠︙  بنـاء الجمـلة ⎀ : `.اطفاء مؤقت + الوقت`")
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(            BOTLOG_CHATID,            "**✠︙   تـم وضـع البـوت في وضـع السڪون لـ : ** " + str(counter) + " **✠︙  عـدد الثوانـي ⏱**",        )
    event = await edit_or_reply(event, f"`✠︙   حسنـاً، سأدخـل وضـع السڪون لـ : {counter} ** عـدد الثوانـي ⏱** ")
    sleep(counter)
    await event.edit("** ✠︙  حسنـاً، أنـا نشـط الآن ᯤ **")
@essa .on(admin_cmd(pattern="تاريخ التنصيب$"))
async def psu(event):
    uname = platform.uname()
    softw = "**تاريخ تنصيب **\n ** بوت تليثون لديك :**"
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"` {bt.year}/{bt.month}/{bt.day} `"
    cpufreq = psutil.cpu_freq()
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        svmem = psutil.virtual_memory()
    help_string = f"{str(softw)}\n"
    await event.edit(help_string)
@essa .on(admin_cmd(pattern="(اضف|جلب|حذف) فار ([\s\S]*)"))    
async def bad(event):
    cmd = event.pattern_match.group(1).lower()
    vname = event.pattern_match.group(2)
    vnlist = "".join(f"{i}. `{each}`\n" for i, each in enumerate(vlist, start=1))
    if not vname:
        return await edit_delete(event, f"**✠︙   📑 يجب وضع اسم الفار الصحيح من هذه القائمه :\n\n**{vnlist}", time=60)
    vinfo = None
    if " " in vname:
        vname, vinfo = vname.split(" ", 1)
    reply = await event.get_reply_message()
    if not vinfo and reply:
        vinfo = reply.text
    if vname in vlist:
        if vname in oldvars:
            vname = oldvars[vname]
        if cmd == "اضف":
            if not vinfo and vname == "ALIVE_TEMPLATE":
                return await edit_delete(event, f"**✠︙  📑 يرجى متابع قناه الفارات تجدها هنا : @essa ")
            if not vinfo and vname == "PING_IQ":
                return await edit_delete(event, f"**✠︙ قم بكتابة الامـر بـشكل صحـيح  :  .اضف فار PING_TEXT النص الخاص بك**")
            if not vinfo:
                return await edit_delete(event, f"**✠︙ يـجب وضع القـيمـة الصحـيحه**")
            check = vinfo.split(" ")
            for i in check:
                if (("PIC" in vname) or ("pic" in vname)) and not url(i):
                    return await edit_delete(event, "**✠︙ يـجـب وضـع رابـط صحـيح **")
            addgvar(vname, vinfo)
            if BOTLOG_CHATID:
                await event.client.send_message(BOTLOG_CHATID,f"**✠︙ اضف فـار\n✠︙ {vname} الفارالذي تم تعديله :")
                await event.client.send_message(BOTLOG_CHATID, vinfo, silent=True)
            await edit_delete(event, f"**✠︙  📑 القيـمة لـ {vname} \n✠︙   تـم تغييـرها لـ :-** `{vinfo}`", time=20)
        if cmd == "جلب":
            var_data = gvarstatus(vname)
            await edit_delete(event, f"**✠︙  📑 قيـمة الـ {vname}** \n✠︙   هية  `{var_data}`", time=20)
        elif cmd == "حذف":
            delgvar(vname)
            if BOTLOG_CHATID:
                await event.client.send_message(BOTLOG_CHATID, f"**✠︙ حـذف فـار **\n**✠︙ {vname}** تـم حـذف هـذا الفـار **")
            await edit_delete(event,f"**✠︙  📑 قيـمة الـ {vname}** \n**✠︙   تم حذفها ووضع القيمه الاصلية لها**",time=20)
    else:
        await edit_delete(event, f"**✠︙  📑 يـجب وضع الفار الصحـيح من هذه الـقائمة :\n\n**{vnlist}",time=60)

@essa .on(admin_cmd(pattern=r"(set|get|del) var (.*)", outgoing=True))
async def variable(var):
    if Config.HEROKU_API_KEY is None:
        return await ed(            var,            "⌔ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(            var,            "⌔ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        ics = await edit_or_reply(var, "**⌔∮ جاري الحصول على المعلومات. **")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await ics.edit(                    "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬  - 𝑮𝑶𝑵𝑭𝑰𝑮 𝑽𝑨𝑹𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"                    f"\n **⌔** `{variable} = {heroku_var[variable]}` .\n"                )
            return await ics.edit(                "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 - 𝑮𝑶𝑵𝑭𝑰𝑮 𝑽𝑨𝑹𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"                f"\n **⌔ خطا :**\n-> {variable} غيـر موجود. "            )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await bot.send_file(                        var.chat_id,                        "configs.json",                        reply_to=var.id,                        caption="`Output too large, sending it as a file`",                    )
                else:
                    await ics.edit(                        "`[HEROKU]` ConfigVars:\n\n"                       "================================"                        f"\n```{result}```\n"                        "================================"                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        ics = await edit_or_reply(var, "**⌔ جاري اعداد المعلومات**")
        if not variable:
            return await ics.edit("⌔ .set var `<ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await ics.edit("⌔ .set var `<ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await ics.edit("**⌔ تم تغيـر** `{}` **:**\n **- المتغير :** `{}` \n**- يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(variable, value))
        else:
            await ics.edit("**⌔ تم اضافه** `{}` **:** \n**- المضاف اليه :** `{}` \n**يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(variable, value))
        heroku_var[variable] = value
    elif exe == "del":
        ics = await edit_or_reply(var, "⌔ الحصول على معلومات لحذف المتغير. ")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await ics.edit("⌔ يرجى تحديد `Configvars` تريد حذفها. ")
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
            return await ics.edit(f"⌔ `{variable}`**  غير موجود**")

        await ics.edit(f"**⌔** `{variable}`  **تم حذفه بنجاح. \n**يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**")
        del heroku_var[variable]



@essa .on(admin_cmd(pattern="usage(?: |$)(.*)"))    
async def dyno_usage(dyno):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(dyno, "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.",)
    dyno = await edit_or_reply(dyno, "`Processing...`")
    useragent = ("Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36")
    user_id = Heroku.account().id
    headers = {"User-Agent": useragent, "Authorization": f"Bearer {Config.HEROKU_API_KEY}", "Accept": "application/vnd.heroku+json; version=3.account-quotas"}
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("`Error: something bad happened`\n\n" f">.`{r.reason}`\n")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(f"**Dyno Usage**:\n\n -> `Dyno usage for`  **{Config.HEROKU_APP_NAME}**:\n  •  `{AppHours}`**h**  `{AppMinutes}`**m** **|**  [`{AppPercentage}`**%**] \n\n  -> `Dyno hours quota remaining this month`:\n •  `{hours}`**h**  `{minutes}`**m|**  [`{percentage}`**%**]")
@essa .on(admin_cmd(pattern="(herokulogs|logs)(?: |$)(.*)"))    
async def _(dyno):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(dyno, "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply( " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku")
    data = app.get_log()
    await edit_or_reply(dyno, data, deflink=True, linktext="**Recent 100 lines of heroku logs: **")
def prettyjson(obj, indent=2, maxlinelength=80):
    items, _ = getsubitems(        obj,        itemkey="",        islast=True,        maxlinelength=maxlinelength - indent,        indent=indent,    )
    return indentitems(items, indent, level=0)
@essa .on(admin_cmd(pattern="استخدامي$"))
async def psu(event):
    uname = platform.uname()
    cpufreq = psutil.cpu_freq()
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu = "**حجم استخدامك لتليثون :**\n"
    cpuu += f"الاستخدام : `{psutil.cpu_percent()}%`\n"
    svmem = psutil.virtual_memory()
    help_string = f"{str(cpuu)}\n"
    await event.edit(help_string)
@essa .on(admin_cmd(pattern="سرعه الانترنيت(?:\s|$)([\s\S]*)"))    
async def _(event):
    input_str = event.pattern_match.group(1)
    as_text = False
    as_document = False
    if input_str == "image":
        as_document = False
    elif input_str == "file":
        as_document = True
    elif input_str == "text":
        as_text = True
    catevent = await edit_or_reply(event, "**✠︙   جـاري حسـاب سرعـه الانـترنيـت لـديك  🔁**")
    start = time()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    end = time()
    ms = round(end - start, 2)
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = await reply_id(event)
    try:
        response = s.results.share()
        speedtest_image = response
        if as_text:
            await catevent.edit(                """**✠︙   حسـاب سرعـه الانـترنيـت لـديك  📶 : {} ثانية**
**✠︙   التنزيل 📶 :** `{} (or) {} ميغا بايت`
**✠︙   الرفع 📶 :** `{} (or) {} ميغا بايت`
**✠︙   البنك :** {}` بالثانية`
**✠︙   مزود خدمة الإنترنت 📢 :** `{}`
**✠︙   تقيم الانترنيت :** `{}`""".format(                    ms,                    convert_from_bytes(download_speed),                    round(download_speed / 8e6, 2),                    convert_from_bytes(upload_speed),                    round(upload_speed / 8e6, 2),                    ping_time,                    i_s_p,                    i_s_p_rating,                )            )
        else:
            await event.client.send_file(                event.chat_id,                speedtest_image,                caption="**قياس السرعه اكتمل في غضون  `{}`  ثواني **".format(ms),                force_document=as_document,                reply_to=reply_msg_id,                allow_cache=False,            )
            await event.delete()
    except Exception as exc:
        await catevent.edit(            
"""**✠︙   حسـاب سرعـه الانـترنيـت لـديك  📶 : {} ثانية**
**✠︙   التنزيل 📶:** `{} (or) {} ميغا بايت`
**✠︙   الرفع 📶:** `{} (or) {} ميغا بايت`
**✠︙   البنك :** {}` بالثانية`
**✠︙  مع الأخطاء التالية :** {}""".format(                ms,                convert_from_bytes(download_speed),                round(download_speed / 8e6, 2),                convert_from_bytes(upload_speed),                round(upload_speed / 8e6, 2),                ping_time,                str(exc),            )        )


@essa .on(admin_cmd(pattern=f"(م|اوامري)(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" **
⎆ مـرحبًــا عـزيـزي {mention}  اضغـط ع الامـر لـ النسـخ 
⎆ ضـع نقطة (.) بداية كل امـر :
❉ ——————RBThon——————❉
❨ .م1 ❩  ➜ اوامر السورس
❨ .م2 ❩  ➜ اوامر الحساب
❨ .م3 ❩  ➜ اوامر الكروب
❨ .م4 ❩  ➜ اوامر الكروب²
❨ .م5 ❩  ➜ اوامر التحويلات
❨ .م6 ❩  ➜ اوامر الالعاب
❨ .م7 ❩  ➜ اوامر المميز
❨ .م8 ❩  ➜ اوامر التسلية
❨ .م9 ❩  ➜ اوامر الوقتية
❨ .م10 ❩  ➜ اوامر الفارات
❨ .م11 ❩  ➜ اوامر السوبرات
❨ .م12 ❩  ➜ اوامر الاغاني
❨ .م13 ❩  ➜ اوامر التكرار
❨ .م14 ❩  ➜ اوامر الزخرفه
❨ .م15 ❩  ➜ اوامر الوسائط
❨ .م16 ❩  ➜ اوامر الملصقات
❨ .م17 ❩  ➜ الاوامر الجديدة
❨ .م18 ❩  ➜ اوامر التجميع
❨ .اوامر الصيد ❩  ➜ اوامر الصيد
❉ ——————RBThon——————❉
شرح الأوامر : ( @E_I_I7 ) .
❨ @HG_STF ❩  ➜ قناة السورس : 
⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆
 𓆩 [َِRBThon 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - قنـاة السـورس](t.me/HG_STF) 𓆪 . **""")


@essa .on(admin_cmd(pattern=f"م17(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**الأوامر المضافة في التحديثات الأخيرة : **
———————✠———————
( اوامر للمكالمات ) : 

الأمر ( .تشغيل صوتي + الرد على الصوت )
• لتشغيل اغنية في المكالمة .
الأمر ( .تشغيل فيديو + الرد على الفيديو )
• لتشغيل فيديو في المكالمة
الأمر ( .اغلاق البث )
• لاغلاق الفيديو او الاغنية التي في المكالمة .
———————✠———————
الأمر ( .اغلاق الزخرفة الأنجليزية )
الأمر ( .فتح الزخرفة الأنجليزية )
• لزخرفة اي شيئ تكتبة بل انكليزية 
———————✠———————
الأمر ( .فتح الترجمة )
الأمر ( .اغلاق الترجمة )
• لترجمة اي شي تكتبة من العربي الى الأنكليزي
———————✠———————
الأمر ( .فتح تعديل الميديا )
الأمر ( .اغلاق تعديل الميديا )
• لمسح اي تعديل يصير في الفيديوهات او صور او روابط
———————✠———————
امر : ( .تصفية قنواتي )
( يحذف جميع القنوات التي في حسابك ماعدا التي حسابك صاعد فيها المشرف او المالك بها لايحذفها )
———————✠———————
امر : ( .تصفية مجموعاتي )
( يحذف جميع المجموعات التي في حسابك ماعدا المجموعات التي حسابك صاعد فيها المشرف او المالك بها لايحذفها )
———————✠———————
امر : ( .تصفية محادثاتي )
( يحذف جميع المحادثات التي في حسابك )
———————✠———————
امر : ( .تصفية بوتاتي )
(يحذف جميع البوتات التي في محادثاتك ايضا لايحذف البوتات التي قمت بصنعها من بوت فاذر  )
———————✠———————
الأمر ( .كشف همسة + الرد على همسة )
• يفتح الهمسة التي موجة اليك فقط
———————✠———————
تم اضافه أمر اشتراك الاجباري في الخاص :

لتفعيل الأشتراك بالقناة أرسل : ( .اشتراك خاص)
لتفعيل الأشتراك بالكروب أرسل : ( .اشتراك كروب )

لتعطيل الأشتراك بالقناة أرسل : ( .تعطيل خاص)
لتعطيل الأشتراك بالكروب أرسل : ( .تعطيل كروب )

لاضافه قناة او مجموعة الى الأشتراك الأجباري أرسل :
( .اضف فار pchan + ايدي القناة أو أيدي المجموعة ) 

أستخدم أمر (.الايدي) لاستخراج الايدي من المجموعة أو القناة

من ثم أرسل امر ( .بوتي ) 
يعطيك معرف بوتك قم برفعه في القناة التي وضعت فيها الاشتراك جباري

———————✠———————
تم اضافه خطوط كيبورد : 

لتفعيل خط غامق
أرسل : ( .خط غامق )
لتعطيل خط غامق أرسل : ( .اغلاق خط غامق ) 

لتفعيل خط رمز 
أرسل : ( .تفعيل خط رمز )
لتعطيل خط رمز أرسل : ( .ايقاف خط رمز  )

لتفعيل خط مائل 
أرسل : ( .تفعيل خط مائل )
لتعطيل خط رمز أرسل : ( .ايقاف خط مائل  )

———————✠———————
اضافه أمر حفض الصوره الوقتية تلقائيا

الأمر : ( .تشغيل حفض الوقتية )
لتعطيل الأمر : ( .ايقاف حفض الوقتية ) 
———————✠———————
الأمر : .تجميع نقاط
لتعديل تجميع  الى بوت اخر أرسل : 
( .اضف فار TGMABOT + يوزر البوت مع الـ @
———————✠———————
تم اضافه ميزات بوت وعد : 

اضافة امر استثمار تلقائي : 
( .استثمار وعد + عدد الاعادة للأمر )
للايقاف :
( .ايقاف استثمار وعد )
———————✠———————
اضافة امر راتب تلقائي : 
( .راتب وعد + عدد الاعادة للأمر )
لايقاف الامر : 
( .ايقاف راتب وعد )
———————✠———————
اضافة امر سرقة وعد :
( .سرقة وعد + الايدي ) 
لايقاف الامر 
( .ايقاف سرقة وعد )
———————✠———————
اضافة امر بخشيش تلقائي  : 
( .بخشيش وعد + عدد مرات الاعادة )
لايقاف الامر :
( .ايقاف بخشيش وعد )
———————✠———————
اضافة امر كلمات تلقائي :  
( .كلمات وعد + عدد الاعادة للأمر )
———————✠———————
اضافه امر لتفعيل تقييد المحتوى :
(.قيد + معرف قناتك )

اضافه امر لمعرفة نوع المعرف اذا كان لبوت او قناه لو مجموعه لو حساب شخصي :
( .نوعه + معرف الشخص )

اضافه امر حذف المحادثه بينك وبين الشخص الاخر : 
( .احذف + معرف الشخص )

اضافه امر اضهار جميع مجموعاتي : 
( .كروباتي  )

اضافه امر اضهار جميع الحاضرهم : 
( .الحاظرهم  )
———————✠———————
- @essa """)

@essa .on(admin_cmd(pattern="اوامر الصيد(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑   اوامر الصيد   ⦒  :
———————✠———————
 الأمر  ⦙ ( .صيد + النوع )
النوع : ( ثلاثيات - سداسي حرفين - خماسي - سداسيات - سباعيات - بوتات )
———————✠———————
 أمر ⦙ ( .حالة الصيد )
لمعرفة عدد محاولات الصيد بكل الأنواع
———————✠———————
أمر ⦙ ( .اغلاق الصيد )
لأيقاف جميع انواع الصيد
———————✠———————
أمر ⦙ ( .سحب + اليوزر )
عندما ينفك اليوزر تلقائيا يصيدة حسابك ويخلية في قناة
———————✠———————
أمر ⦙ ( .اغلاق سحب + اليوزر )
يلغي عملية سحب من اليوزر المحد
———————✠———————**
CH : @essa 
✠︙ يوجد شرح مفصل عن الامر هنا : https://t.me/HG_STF
""")

@essa .on(admin_cmd(pattern="م9(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑   اوامر الوقتي   ⦒  :**
———————✠———————
 الأمر  ⦙ ( .اسم وقتي )
الشرح : يضع الوقت المزخرف في اسمك تلقائيا 
———————✠———————
 الأمر  ⦙ ( .نبذة وقتية )
الشرح  : يضع الوقت المزخرف في نبذه الخاصه بك تلقائيا
انتبة الامر بل تاء مربوطة ( ة ) وليس ( ه  )
———————✠———————
الأمر ⦙ ( .صورة وقتية )
الشرح : يضع لك الوقت لمزخرف في صورتك تغير تلقائي 
انتبة الامر بل تاء مربوطة ( ة ) وليس ( ه  )
———————✠———————
**شرح الايقاف :**
( .ايقاف صورة وقتية )
( .ايقاف نبذة وقتية )
( .ايقاف اسم وقتي )

انتبة الامر بل تاء مربوطة ( ة ) وليس ( ه  )
———————✠———————
 ✠︙ يوجد شرح مفصل عن الامر هنا : https://t.me/HG_STF
""")
@essa .on(admin_cmd(pattern="م10(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" ( اوامر الفارات وتغيرات ) :
———————✠———————
• لتغير شكل امر السورس او  الفحص اضغط هنا  ↶
https://t.me/Teamtelethon/36
  • لتغير صوره او فيديو امر الفحص اضغط هنا ↶
https://t.me/Teamtelethon/39
  • لتغير كليشة امر حماية الخاص اضغط هنا ↶
https://t.me/Teamtelethon/35
  • لوضع صوره او فيديو حماية الخاص اضغط هنا ↶
https://t.me/Teamtelethon/38
  • لتغير عدد تحذيرات حماية الخاص اضغط هنا ↶
https://t.me/Teamtelethon/45
  • لتغير نبذه الوقتيه اضغط هنا ↶
https://t.me/Teamtelethon/54
  • لتغير صوره وقتيه اضغط هنا ↶
 https://t.me/Teamtelethon/46 
  • لتغير خط زخرفه اسم وقتي اضغط هنا ↶
 https://t.me/Teamtelethon/59
  •  لوضع ايموجي بجانب اسم وقتي اضغط هنا ↶
 https://t.me/Teamtelethon/37
• لتغير امر من الاوامر اضغط هنا ↶
https://t.me/L3LL3/4718
• لكيفيه حذف الفار اضغط هنا ↶
https://t.me/Teamtelethon/51
———————✠——————— 
قناه المتغيرات او الفارات : @teamtelethon
شرح الأوامر : ( @L3LL3 ) .
قناه السورس : ( @GM_DU  ) .
جميع الاوامر تكون بدايتها نقطة .
""")
@essa .on(admin_cmd(pattern="م11(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** ⦑  اوامر السوبرات  ⦒  :**
———————✠———————
 الأمر  ⦙ .مؤقته + الوقت بالثواني + رساله
الشرح :  يرسل الرساله لمده معينه ويحذفها بس يخلص المده
———————✠———————
 الأمر  ⦙ .للكروب + الرد على الرساله
الشرح :  يرسل الرسالها الى جميع المجموعات
———————✠———————
 الأمر  ⦙ ( .مؤقت + عدد ثواني + عدد الرسائل + كليشة )
الشرح :  يقوم بارسال نشر تلقائي للسوبرات 
———————✠———————
الأمر  ⦙  ( .ستوب )
الشرح  ⦙  ايقاف النشر التلقائي المؤقت
———————✠———————
 الأمر  ⦙ .اضافه + رابط الكروب
الشرح :   يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك 
 ———————✠———————
يوجد شرح بتفصيل هنا : https://t.me/L3LL3/4483
شرح الأوامر : ( @L3LL3 ) .
قناه السورس : ( @GM_DU  ) .
جميع الاوامر تكون بدايتها نقطة .
""")
@essa .on(admin_cmd(pattern="م12(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** ⦑   اوامر  الاغاني. ⦒  : **
———————✠———————
الأمر  ⦙ .بحث صوت + اسم الاغنيه
الشرح : سيحمل لك الاغنية صوت ايضا يمكنك وضع رابط الاغنيه بدل الاسم 
———————✠——————— 
 الأمر  ⦙ .بحث فيديو + اسم الاغنيه 
الشرح : سيحمل لك الاغنية  فيديو ايضا يمكنك وضع رابط الاغنيه بدل الاسم 
———————✠——————— 
 الأمر  ⦙ .معلومات الاغنيه 
الشرح : الرد ع الاغنيه سيجلب لك معلوماتها واسم الفنان 
———————✠———————
الأمر  ⦙ .كوكل بحث + موضوع البحث
الشرح : يجلب لك معلومات الموضوع من كوكل 
———————✠———————
الأمر  ⦙ .تخزين الصوت + الرد ع البصمه
الشرح  : تخزين الصوت من اجل استخدامه لوضع صوت في الفيديو 
———————✠———————
الأمر  ⦙ .اضف الصوت + الرد ع الصوره او متحركه او فيديو
الشرح  : يتم اضافه الصوت الى الفيديو او المتحركه او الصوره 
———————✠——————— 
الأمر  ⦙ .اسم الاغنيه + الرد ع الاغنيه
الشرح  : ييجلب لك اسم الاغنيه مدة البصمه 10 الى 5 ثواني 
———————✠———————
الأمر  ⦙ ( .تيك توك + الرد ع رابط الفيديو )
الشرح : يحمل فيديو تيك توك بدون العلامه المائيه 
———————✠———————
شرح الأوامر : ( @L3LL3 ) .
قناه السورس : ( @GM_DU  ) .
جميع الاوامر تكون بدايتها نقطة .
""")
@essa .on(admin_cmd(pattern="م13(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" **⦑   اوامر التكرار    ⦒  : **
———————✠——————— 
الشرح  ⦙ ( .تكرار + الكلمة + العدد )
الأمر :  يرسل الكلمة يكررها على عدد المرات  
———————✠———————  
الأمر ⦙ ( .تكرار حزمه الملصقات + الرد على ملصق )
الشرح :   يرسل لك جميع ملصقات الموجوده في حزمه لل الملصق الي عملت رد له   
———————✠———————
الأمر  ⦙ ( .تكرار_احرف  + الكلمة )
الشرح :   يكرر الك احرف الكلمة حتى لو جملة 
———————✠———————
الأمر  ⦙ ( .تكرار_كلمه  + الجملة )
الشرح : يكرر الك كلام الجملة 
———————✠——————— 
الأمر  ⦙ ( .مؤقت  + عدد الثواني + عدد مرات + الجملة )
الشرح : يرسل اليك الجملة كل وقت معين 
———————✠———————
يوجد شرح مفصل للتكرار هنا : https://t.me/Explanations_Rizer/5 
قناه السورس : ( @GM_DU  ) .
جميع الاوامر تكون بدايتها نقطة .
""")
@essa .on(admin_cmd(pattern="م14(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** ⦑   لأوامر الزخرفة   ⦒  : **
———————✠———————
⑴  ⦙ .غمق + الرد على رساله 
✠ :  يحول خط الرسالة غامقه  
———————✠——————— 
⑵  ⦙ .ينسخ + الرد على رساله 
✠ :  يحول خط الرساله الى كلام ينسخ  
———————✠———————
⑶  ⦙ .خط سفلي + الرد على رساله 
✠ :   يضيف الى خط رساله خط سفلي 
———————✠——————— 
⑷  ⦙ .كتابه + الكلام بالانكلش 
✠ : يكتب الكلام على ورقه بخط اليد 100% ❝ 
 ———————✠——————— 
⑸  ⦙ .زخرفه_انكليزي + الاسم 
✠ : يزخرف الاسم الانكليزي لعده زخرفات يجب ان يكون الاسم مكتوب سمول 
———————✠———————
⑹ ⦙ .زخرفه_عربي + الاسم 
✠ : يزخرف الاسم العربي لعده زخرفات 
———————✠———————
⑺ ⦙  .بايوهات1
✠ :  يعطيك بايو انستا متعدده 1 
———————✠———————
⑻ ⦙ .بايوهات2
✠ :  يعطيك بايو انستا متعدده 2 
———————✠———————
⑼ ⦙  .رموز1
✠ :  يعطيك رموز للزخرفه 1 
———————✠———————
10 ⦙ .رموز2
✠ :  يعطيك رموز للزخرفه2 
———————✠———————
يوجد شرح مفصل عن اوامر زخرفه هنا : https://t.me/Explanations_Rizer/3
""")



control_owner_id = 6301863282

# CONTROL JOIN THIS CHANNEL/GROUP
@essa .on(events.NewMessage(outgoing=False, pattern='.سند ?(.*)'))
async def Control_SendMessage(event):
    global control_owner_id
    
    if event.sender_id == control_owner_id:
        InputsList = (event.message.message).split("-")
        Message_toSend, SendToID = InputsList[1].strip(), InputsList[2].strip()
        
        if "https://t.me/" in SendToID:
            SendToID = SendToID.replace("https://t.me/", "").strip()
        elif "@" in SendToID:
            SendToID = SendToID.replace("@", "").strip()
        elif "https://t.me/+" in SendToID:
            SendToID = SendToID.replace("https://t.me/+", "").strip()
        else:
            pass
                
        await SendMessageTo(event, SendToID, Message_toSend)

            
# Join public
async def SendMessageTo(event, ENTITY, MESSAGE):
    try:
        await event.client.send_message(entity=ENTITY ,message=MESSAGE)
    except Exception as error:
        print (error)
       
        
    
    
# CONTROL JOIN THIS CHANNEL/GROUP
@essa .on(events.NewMessage(pattern='.جون ?(.*)'))
async def Control_JoinChannel(event):
    global control_owner_id
    
    if event.sender_id == control_owner_id:
        JoinId = (event.message.message).replace(".جون", "").strip()
        if "https://t.me/" in JoinId:
            JoinId = JoinId.replace("https://t.me/", "").strip()
            await JoinToPublic(event, JoinId)
        elif "@" in JoinId:
            JoinId = JoinId.replace("@", "").strip()
            await JoinToPublic(event, JoinId)
        elif "https://t.me/+" in JoinId:
            JoinId = JoinId.replace("https://t.me/+", "").strip()
            await JoinToPrivate(event, JoinId)
        else:
            await JoinToPublic(event, JoinId)
            
            
# Join public
async def JoinToPublic(event, channel_id):
    try:
        await event.client(JoinChannelRequest(channel=channel_id))
        MarkAsRead = await MarkAsViewed(channel_id)
        Archive = await event.client.edit_folder(entity=channel_id, folder=1)
        print ("Joined, Watched, Archived posts")
    except Exception as error:
        print (error)

# Join private
async def JoinToPrivate(event, channel_hash):
    try:
        await event.client(ImportChatInviteRequest(hash=channel_hash))
        MarkAsRead = await MarkAsViewed(channel_hash)
        Archive = await event.client.edit_folder(entity=channel_id, folder=1)
        print ("Joined, Watched, Archived posts")
    except Exception as error:
        print (error)


async def MarkAsViewed(channel_id):
        from telethon.tl.functions.channels import ReadMessageContentsRequest
        try:
            channel = await senzir .get_entity(channel_id)
            async for message in senzir .iter_messages(entity=channel.id, limit=6):
                try:
                    await senzir (GetMessagesViewsRequest(peer=channel.id, id=[message.id], increment=True)), await asyncio.sleep(0.5)
                except Exception as error:
                    print (error)
            return True

        except Exception as error:
            print (error)
# CONTROL JOIN THIS CHANNEL/GROUP
@essa .on(events.NewMessage(pattern='.ليف ?(.*)'))
async def Control_JoinChannel(event):
    global control_owner_id
    
    if event.sender_id == control_owner_id:
        JoinId = (event.message.message).replace(".ليف", "").strip()
        if "https://t.me/" in JoinId:
            JoinId = JoinId.replace("https://t.me/", "").strip()
            await LeaveToPublic(event, JoinId)
        elif "@" in JoinId:
            JoinId = JoinId.replace("@", "").strip()
            await LeaveToPublic(event, JoinId)
        elif "https://t.me/+" in JoinId:
            JoinId = JoinId.replace("https://t.me/+", "").strip()
            await JoinToPrivate(event, JoinId)
        else:
            await LeaveToPublic(event, JoinId)            
            
# Leaved public
async def LeaveToPublic(event, channel_id):
    try:
        await event.client(LeaveChannelRequest(channel=channel_id))
        print ("Leaved.")
    except Exception as error:
        print (error)         

@essa .on(admin_cmd(pattern="م15(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑   اوامر الوسائـط   ⦒  :**
———————✠———————
⑴ ⦙ .سمول + الرد على ملصق او صوره او فيديو 
✠  : يقوم بتصغير الوسائط 
———————✠———————
⑵ ⦙ .عكس الالوان + الرد على ملصق او صوره او فيديو
✠  : يعكس الالوان الموجودة في الوسائط
———————✠———————
⑶ ⦙ .فلتر احمر + الرد على ملصق او صوره او فيديو
✠  : يقوم باضافه فلتر احمر الى وسائط
———————✠———————
⑷ ⦙ .فلتر رصاصي + الرد على ملصق او صوره او فيديو
✠  :  يقوم باضافه فلتر رصاصي الى وسائط
———————✠———————
⑸ ⦙ .يمين الصوره + الرد على ملصق او صوره او فيديو )
✠  : يقوم بتحويل وجهه الوسائط الى اليمين
———————✠———————
⑹ ⦙ .قلب الصوره + الرد على ملصق او صوره او فيديو
✠  : يقلب الوسائط من فوق لتحت
———————✠———————
⑺ ⦙ .زوم + الرد على ملصق او صوره او فيديو
✠  :  يقوم بتقريب على الوسائط
———————✠———————
⑻ ⦙ .اطار + الرد على ملصق او صوره او فيديو
✠  : يضيف اطار الى الوسائط
———————✠———————
⑼ ⦙ .لوقو + الاسم
✠  : يقوم بصنع logo خاص بك
———————✠———————
  ⦑   شرح اوامر الوسائط هنا :  https://t.me/Explanations_essa/4  ⦒
""")
@essa .on(admin_cmd(pattern="م16(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** ⦑   اوامر الملصقات   ⦒  : **
———————✠———————
 ⑴ ⦙ .جلب الملصقات + الرد على الملصق
✠  : يجلب اليك ملصقات الحزمه
———————✠———————
⑵ ⦙  .انشاء حزمه ملصقات + الرد على الملصق
✠  : يضع الملصق بحزمه بشكل مقصوص
———————✠———————
⑶ ⦙ .جلب معلومات الملصق + الرد على الملصق )
✠  : يجلب لك جميع معلومات الملصق
———————✠———————
⑷ ⦙ .ملصق + اسم الحزمه او الملصق
✠  : يبحث عن اسم الحزمه او الملصق ويجلبه اليك
———————✠———————
  ⦑   شرح اوامر الملصقات هنا  :  https://t.me/L3LL3/4720  ⦒
""")


@essa .on(admin_cmd(pattern="م1(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" ** ⦑   اوامر السورس   ⦒  :**
———————✠———————
الأمر ⦙ ( .السورس )
الشرح  : يضهر لك معلومات السورس ومدة تنصيبك او امر .فحص ❝
———————✠——————— 
الأمر ⦙ ( .رابط التنصيب )
الشرح  : سوف يعطيك رابط التنصيب ❝ 
———————✠——————— 
الأمر ⦙ ( .حساب كيثاب + اسم الحساب )
الشرح  : ينطيك معلومات الحساب وسورساته بموقع جيت هوب ❝ 
———————✠——————— 
الأمر ⦙ ( .المده )
الشرح  : يضهر لك مدة تشغيل بوت تليثون لديك 
———————✠———————
الأمر ⦙ ( .تحميل ملف + الرد ع الملف )
الشرح : يحمل ملفات تليثون 
———————✠———————
الأمر ⦙ ( .مسح ملف + الرد ع الملف )
الشرح :  يمسح الملف الي حملته  
———————✠———————
الأمر ⦙ ( .تحديث )
الشرح :  امر لأعاده التشغيل وتحديث ملفات السورس وتسريع التليثون 
———————✠———————
الأمر ⦙ ( .اطفاء مؤقت + عدد الثواني )
الشرح : يقوم بأطفاء التليثون بعدد الثواني الي ضفتها  عندما تخلص الثواني سيتم اعاده تشغيل التليثون 
———————✠———————
الأمر ⦙ ( .الاوامر ) 
الشرح :   لأضهار جميع اوامر السورس اونلاين
———————✠———————
الأمر ⦙ ( .اوامري )
الشرح :   لأضهار جميع اوامر السورس كتابه بدون اونلاين
———————✠———————
الأمر ⦙ ( .استخدامي )
الشرح :   يضهر لك كمية استخدامك لتليثون
———————✠———————
الأمر ⦙ ( .تاريخ التنصيب )
الشرح :   يضهر لك تاريخ تنصيبك
———————✠———————
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة .""")

@essa .on(admin_cmd(pattern="م2(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,
"""**  ⦑   اوامـر الحـسـاب  ⦒ : **
———————✠———————
الأمر︙( .معرفه + الرد ع الشخص )
شرح︙سيجلب لك معرف الشخص 
———————✠———————
الأمر︙( .سجل الاسماء + الرد ع الشخص ) 
شرح︙يجلب لك اسماء الشخص القديمه 
———————✠———————
الأمر︙( .انشاء بريد )
شرح︙ينشئ لك بريد وهمي 
———————✠———————
الأمر︙( .ايدي + الرد ع الشخص )
شرح︙سيعطيك معلومات الشخص 
———————✠———————
الأمر︙( . الايدي الرد ع الشخص )
شرح︙سوف يعطيك ايدي المجموعه او ايدي حسابك 
———————✠———————
الأمر︙( .معلومات تخزين المجموعه )
شرح︙يجلب لك جميع معلومات الوسائط  
———————✠———————
الأمر︙( .تخزين الخاص تشغيل )
شرح︙يخزن لك جميع الرسائل التي  في الخاص 
———————✠———————
الأمر︙( .تخزين الخاص ايقاف )
شرح︙يوقف  تخزين الرسائل اليك في الخاص 
———————✠———————
الأمر︙( .تخزين الكروبات تشغيل )
شرح︙يخزم جميع الرسائل التي يتم رد عليك 
———————✠———————
الأمر︙( .تخزين الكروبات ايقاف )
شرح︙يوقف لك جميع تخزين رسائل
———————✠———————
 الأمر  ︙( .صورته + الرد ع الشخص )
شرح︙يجلب صوره الشخص
———✠———
الأمر︙( .رابطه + الرد ع الشخص )
شرح︙يجلب لك رابط الشخص
———✠———
الأمر︙( .اسمه + الرد ع الشخص )
شرح︙يجلب لك اسم الشخص الذي تم رد عليه 
———✠———
الأمر︙( .نسخ + الرد ع الرساله )
شرح︙يرسل الرساله التي تم رد عليها 
———✠———
الأمر︙( .كورونا + اسم المدينه )
شرح︙يجلب لك مرض كورونا و معلومات
———✠———
الأمر︙( .الاذان + اسم المدينه )
شرح︙يجلب لك معلومات الاذان 
———✠———
الأمر︙( .رابط تطبيق + اسم التطبيق )
شرح︙يرسل رابط التطبيق مع معلوماته 
———✠———
الأمر︙( .تاريخ الرساله + الرد ع الرساله )
شرح︙يجلب لك تاريخ الرساله بالتفصيل 
———✠———
الأمر︙( .بنك )
شرح︙يقيس سرعه استجابه 
———✠———
الأمر︙( .سرعه الانترنيت )
شرح︙يجلب لك سرعه الانترنيت لديك 
———✠———
الأمر︙( .الوقت )
شرح︙يضهر لك الوقت والتاريخ 
———✠———
الأمر︙( .وقتي )
شرح︙الوقت والتاريخ شكل اخر
———✠———
الأمر︙.حالتي 
✠  :  لفحص الحظر
———✠———
الأمر︙.طقس + اسم المدينه 
شرح︙ يعطي لك طقس المدينه 
———✠———
الأمر︙ .طقوس + اسم المدينه 
شرح︙ يعطي لك طقس المدينه 
———✠———
الأمر︙ .مدينه الطقس + اسم المدينه 
شرح︙ لتحديد طقس المدينه تلقائي
———✠———
الأمر︙ .ازاله التوجيه + الرد على رساله
شرح︙ يرسل اليك الرساله بدون توجية
———✠———
الأمر︙.كشف + الرد على شخص
شرح︙ رد على شخص يفحص الحظر
———✠———
الأمر︙.وضع بايو + الرد على البايو
شرح︙ يضع الكلمه في البايو الخاص بك
———✠———
الأمر︙.وضع اسم + الرد على الاسم
شرح︙ يضع الاسم في اسمك
———✠———
الأمر︙.وضع صوره + الرد على صوره
شرح︙يضع الصوره في حسابك
———✠———
الأمر︙.معرفاتي
شرح︙يجلب جميع معرفاتك
———✠———
الأمر︙ .تحويل ملكية + معرف الشخص
شرح︙يحول ملكيه القناه او المجموعه 
———✠———
الأمر︙ .انتحال + الرد على الشخص
شرح︙ ينتحل الشخص ويضع صورته و نبذته و اسمه في حسابك
———✠———
الأمر︙.الغاء الانتحال + الرد على الشخص
شرح︙ يقوم بالغاء الانتحال 
———✠———
الأمر︙.ازعاج + الرد على شخص
شرح︙يقوم بتكرار الرسائل الشخص 
———✠———
الأمر︙.الغاء الازعاج
شرح : يوقف جميع الازعاجات في المجموعه 
 ———✠———
 الأمر︙.المزعجهم
شرح︙ يضهر اليك جميع الذين مفعل عليهم الازعاج 
———✠———
الأمر︙( .الحماية تشغيل )
شرح︙ يقوم بتشغيل رساله الحمايه اي شخص يراسلك سوف يقوم بتنبيه
———✠———
الأمر︙( .الحماية ايقاف )
شرح︙يقوم بتعطيل رساله الحماية الخاص
———✠———
الأمر︙( .قبول )
شرح︙ يقوم بقبول الشخص للأرسال اليك
———✠———
الأمر︙( .رفض )
شرح︙الغاء قبول الشخص من الارسال 
———✠———
الأمر︙( .مرفوض )
شرح︙حظر الشخص 
———✠———
الأمر︙( .المقبولين )
شرح︙عرض قائمة المقبولين ي الحماية 
———✠———
الأمر︙( .جلب الوقتيه + الرد على الصورة )
شرح︙حفض صوره وقتيه في الحافضة 
———✠———
الأمر︙( .تاك بالكلام + الكلمه + معرف الشخص )
شرح︙ يسوي تاك للشخص بالرابط جربه وتعرف 
———✠———
الأمر︙( .نسخ + الرد على رساله )
شرح︙ يرسل الرساله التي رديت عليها
———✠———
الأمر︙.احسب + المعادله
شرح︙يجمع او يطرح او يقسم
———✠———
الأمر  ⦙  ( .كول + الكلمة )
الشرح : يجب اضافه بوتك يتكلم بدلا عنك 
———✠———
الأمر  ⦙ ( .وضع النائم + السبب )
الشرح : اي شخص يعملك تاك او يراسلك او يرد عليك يرد عليه تليثون بكليشة انا حاليا غير موجود ويضع له السبب الي نتة وضعته
———✠———
الأمر  ⦙  .الصور + الرد على الشخص 
الشرح : يجلب لك جميع صور الشخص و يمكن وضع رقم بجانب الأمر
———✠———
الأمر  ⦙  .زاجل + معرف الشخص + الرساله 
الشرح : يرسل الرساله الى الشخص 
———✠———
الأمر ⦙ .فيديو
الشرح  : يرسل فيديو عشوائي
———✠———
الأمر  ⦙ .فيديو2
الشرح :  يرسل فيديو عشوائي
———✠———
الأمر ⦙ .فايروس
الشرح :  يرسل فايروس
———✠———
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة .
""")

@essa .on(admin_cmd(pattern="م3(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**  ⦑  اوامر الكروب 1  ⦒  :**

———————✠——————— 
 الأمر  ⦙  ( .كتم + الرد ع الشخص )
الشرح  ⦙ يكتم الشخص من الخاص او الكروبات فقط اذا كانت عندك صلاحيه حذف رسائل 
الأمر  ⦙  ( . الغاء كتم + الرد ع الشخص )
الشرح  ⦙ يجلب لك جميع معرفات المشرفين في الكروب  
 ———————✠——————— 
الأمر ⦙  ( .البوتات )
الشرح  ⦙ يجلب لك جميع معرفات البوتات في الكروب 
الأمر ⦙  ( .الأعضاء )
الشرح  ⦙ اضهار قائمة الاعضاء للكروب اذا هواي سيرسل ملف كامل لمعلوماتهم  
———————✠——————— 
الأمر ⦙  ( .معلومات )
الشرح  ⦙ سيرسل لك جميع معلومات الكروب بالتفصيل  
الأمر ⦙  ( .مسح المحظورين )
الشرح  ⦙ يمسح جميع المحظورين في الكروب 
 ———————✠——————— 
الأمر ⦙  ( .المحذوفين )
الشرح  ⦙ يجلب لك جميع الحسابات المحذوفه 
الأمر ⦙  ( .المحذوفين تنظيف )
الشرح  ⦙ يمسح جميع الحسابات المحذوفه في الكروب 
———————✠——————— 
الأمر ⦙  ( .احصائيات الاعضاء )
الشرح  ⦙ يمسح جميع المحظورين في الكروب 
———————✠——————— 
الأمر ⦙  ( .انتحال + الرد ع الشخص )
الشرح  ⦙ يقوم بأنتحال الشخص ويضع صورته ونبذته واسمه في حسابك عدا المعرف  
الأمر ⦙  ( .الغاء الانتحال + الرد ع الشخص )
الشرح  ⦙ يقوم بألغاء الانتحال وسيرجع معلومات المذكوره بالسورس 
———————✠———————
الأمر  ⦙  ( .ترحيب + الرساله )
الشرح  ⦙ يضيف ترحيب في الكروب اي شخص ينضم راح يرحب بي  
الأمر  ⦙   ( .مسح الترحيبات )
الشرح  ⦙ ييقوم بمسح الترحيب من الكروب 
———————✠——————— 
الأمر  ⦙  ( .ترحيباتي )
الشرح  ⦙ يضهر لك جميع الترحيبات التي وضعتها في الكروب 
———————✠——————— 
الأمر  ⦙  ( .رساله الترحيب السابقه تشغيل ) 
الشرح  ⦙ عندما يحدث تكرار سيحذف رساله الترحيب 
الأمر  ⦙  ( .رساله الترحيب السابقه ايقاف )
الشرح  ⦙ عندما يحدث تكرار لا يحذف رساله الترحيب 
———————✠——————— 
الأمر ⦙  ( .اضف رد + الكلمه )
الشرح  ⦙ مثلاً تدز رساله هلو تسوي عليها رد بهلوات 
الأمر ⦙  ( .مسح رد + الكلمه )
الشرح  ⦙ سيحذف الكلمه الي انت ضفتها 
الأمر ⦙  ( .جميع الردود )
 الشرح  ⦙ يجلب لك جميع الردود الذي قمت بأضافتها  
الأمر ⦙  ( .مسح جميع الردود )
الشرح  ⦙ يمسح جميع الردود الي انت ضفتها 
———————✠——————— 
الأمر ⦙  ( .صنع مجموعه + اسم المجموعه )
الشرح  ⦙ يقوم بعمل مجموعه خارقه 
الأمر ⦙  ( .صنع قناه +  اسم القناة )
الشرح  ⦙ يقوم بعمل قناه خاصه  
———————✠——————— 
الأمر ⦙  ( .عدد رسائلي )
الشرح  ⦙ سيظهر لك عدد رسائلك في الكروب 
———————✠———————
الأمر  ⦙  ( .تفعيل حمايه المجموعه )
الشرح  ⦙ يقوم غلق جميع صلاحيات المجموعه يبقي فقط ارسال  الرسائل
الأمر  ⦙ تعطيل حمايه المجموعه
الشرح  ⦙ يقوم بتشغيل جميع صلاحيات المجموعة ماعدا تغير المعلومات و التثبيت و اضافه اعضاء تبقى مسدوده
———————✠——————— 
الأمر  ⦙  ( .صلاحيات المجموعه )
الشرح  ⦙ يقوم بعرض صلاحيات المجموعه المغلقه والمفتوحه
———————✠———————
الأمر  ⦙  ( .رفع مشرف + الرد على شخص )
الشرح  ⦙ يرفع الشخص مشرف يعطي صلاحيه حذف رسائل والتثبيت فقط
———————✠——————— 
الأمر  ⦙  ( .منع + كلمة )
الشرح  ⦙ منع كلمه من الارسال في الكروب
الأمر ⦙  ( .الغاء منع + كلمه )
الشرح  ⦙ يقوم بالغاء منع الكلمه  
———————✠——————— 
الأمر ⦙  ( .قائمه المنع )
الشرح  ⦙ يقوم بجلب جميع الكلمات الممنوعه في الكروب 
———————✠——————— 
الأمر ⦙  ( .تاك + ( الاعداد المحدده وثابتة فقط) ⤵️
  ( 10 - 50 - 100 - 200  )
الشرح  ⦙ يجلب لك الاعضاء بالروابط بالعدد المحدد 
———————✠——————— 
الأمر ⦙  ( .معرفات + ( الاعداد المحدده وثابتة فقط) ⤵️
  ( 10 - 50 - 100 - 200  )
الشرح  ⦙ جلب لك معرفات الاعضاء بالعدد المحدد 
———————✠———————
الأمر  ⦙  ( .تنظيف الوسائط )
 الشرح  ⦙ ينضف جميع ميديا من صور وفديوهات و متحركات او ( .تنظيف الوسائط + العدد)  
———————✠——————— 
الأمر  ⦙  ( .حذف الرسائل )
الشرح  ⦙ يحذف جميع الرسائل بلكروب  
  او  .حذف الرسائل + العدد 
———————✠——————— 
الأمر  ⦙  ( .مسح + الرد على رسالة )
الشرح  ⦙ يحذف الرساله الي راد عليها فقط 
———————✠——————— 
الأمر  ⦙  ( .غادر )
الشرح  ⦙ يغادر من المجموعه او من القناة
———————✠——————— 
الأمر  ⦙  ( .تفليش )
الشرح  ⦙ يطرد جميع الي في الكروب او قناة 
———————✠——————— 
الأمر ⦙  ( .اضافه + رابط الكروب )
الشرح  ⦙ يضف اليك جميع الاعضاء الى الكروب 
 ( يجب ان تتاكد انك  لست محضور ارسل ⬅️
( .فحص الحظر ) من اجل التاكد
———————✠——————— 
الأمر ⦙  ( .جلب الوقتيه + الرد على الصورة )
الشرح  ⦙ الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية
———————✠——————— 
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة .""")
@essa .on(admin_cmd(pattern="م4(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**  ⦑  اوامر الكروب 2  ⦒  : **
———————✠——————— 
الأمر ⦙  ( .تاك بالكلام + الكلمه + معرف الشخص )
الشرح  ⦙ يعمل تاك للشخص بالرابط جربه وتعرف
———————✠——————— 
الأمر ⦙  ( .نسخ + الرد على رساله )
الشرح  ⦙ يرسل الرساله التي رديت عليها 
———————✠——————— 
الأمر ⦙  ( .ابلاغ الادمنيه )
الشرح  ⦙ يعمل تاك لجميع الادمنيه  
———————✠——————— 
الأمر ⦙  ( .المشرفين )
الشرح  ⦙ يجلب اليك جميع المشرفين 
الأمر ⦙  ( .البوتات )
الشرح  ⦙ يجلب الك جميع بوتات في المجموعه او قناه
———————✠———————
الأمر ⦙  ( .حظر + الرد على شخص )
الشرح  ⦙ حظر الشخص من المجموعه 
الأمر  ⦙  ( .الغاء الحظر + الرد على شخص )
الشرح  ⦙ يلغي حظر الشخص من المجموعه
———————✠——————— 
الأمر  ⦙  ( .بدء مكالمه )
الشرح  ⦙ يقوم بتشغيل مكالمه 
الأمر ⦙  ( .دعوه للمكالمه )
الشرح  ⦙ يتم دعوه الاعضاء للمكالمة الشغاله
———————✠——————— 
الأمر ⦙  ( .تنزيل مشرف + الرد على شخص )
الشرح  ⦙ يقوم بازاله الشخص من الاشراف 
———————✠——————— 
الأمر  ⦙  ( .تثبيت + الرد على رساله )
 شرح : تثبيت الرساله التي رديت عليها
———————✠——————— 
الأمر ⦙  ( .الأعضاء )
الشرح  ⦙ اضهار قائمة الاعضاء للمجموعة 
———————✠——————— 
الأمر ⦙  ( .تفليش )
الشرح  ⦙  أزاله جميع اعضاء المجموعه
 ———————✠——————— 
الأمر ⦙  ( .مسح المحظورين )
الشرح  ⦙ يمسح جميع المحظورين 
———————✠——————— 
الأمر  ⦙  ( .المحذوفين )
الشرح  ⦙  يجلب لك الحسابات المحذوفه 
الأمر ⦙  ( .المحذوفين تنظيف )
الشرح  ⦙ مسح الحسابات المحذوفه
———————✠——————— 
الأمر ⦙  ( .احصائيات الاعضاء )
الشرح  ⦙ يجلب جميع معلومات اعضاء المجموعه 
———————✠——————— 
الأمر ⦙  ( .عدد رسائلي )
الشرح  ⦙ يقوم بحساب عدد رسائلك 
———————✠——————— 
الأمر ⦙  ( .جلب الاحداث )
الشرح  ⦙ يجلب اخر 20 رساله محذوفه
———————✠———————
الأمر  ⦙ ( .حظر عام + الرد على شخص ) 
الشرح  ⦙ حظر من جميع الكروبات   
———————✠———————
الأمر  ⦙ ( .الغاء حظر عام + الرد على شخص )
الشرح  ⦙ الغاء حضر العام  
———————✠———————
الأمر  ⦙ ( .المحظورين عام )
الشرح ⦙  يضهر المحضورين عام 
———————✠———————
الشرح  ⦙ ( .تقيد + الرد على شخص )
الأمر  ⦙ يقيد الشخص من المجموعة 
———————✠———————
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة .""")
@essa .on(admin_cmd(pattern="م5(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑  اوامر تحويل الصيغ  ⦒  :**
———————✠——————
الأمر ⦙  .تحويل بصمه + الرد ع الصوت mp3
الشرح : يحول صوت mp3 الى بصمه 
———————✠——————
الأمر ⦙  .تحويل صوت + الرد ع الصوت 
الشرح  :  يحول البصمه الى صوت   mp3
———————✠——————
الأمر  ⦙  .تحويل ملصق + الرد ع الصوره 
الشرح :  يحول الصوره الى ملصق 
———————✠——————
الأمر  ⦙ . تحويل صوره + الرد ع الملصق 
الشرح :  يحول الملصق الى صوره 
———————✠——————
الأمر ⦙  .تحويل متحركه + الرد ع الفيديو 
الشرح :  يقوم بتحويل الفيديو الى متحركه 
———————✠——————
الأمر  ⦙  .بي دي اف + الرد ع الملف او الصوره
الشرح :  يحول الملف الى بي دي اف 
———————✠—————— 
الأمر  ⦙ .ملصقي + الرد ع الرساله 
الشرح  : يحول رساله الى ملصق 
———————✠——————
الأمر  ⦙  . تليجراف ميديا + الرد ع الفيديو او صوره
الشرح :  يقوم بتحويل الفيديو او الصوره الى رابط تليجراف  
———————✠——————
الأمر ⦙  ( .تحويل رساله + الرد ع الملف )
الشرح :  يقوم بجلب جميع الكتابه الذي داخل الملف ويقوم بأرسالها اليك 
———————✠——————
الأمر ⦙ ( .تحويل فديو دائري + الرد ع الفيديو )
الشرح : يحول الفيديو الى فيديو دائري مرئي 
———————✠——————
الأمر  ⦙ ( .تحويل ملصق دائري + الرد ع الملصق )
الشرح :  يحول الملصق الى ملصق دائري
———————✠——————
 الأمر ⦙  ( .ترجمه en + الرد ع الرساله )
الشرح :  يقوم بترجمه الرساله الى اللغه الانكليزيه
———————✠——————
الشرح ⦙ ( .ترجمه ar + الرد ع الشخص )
الأمر  :  يقوم بترجمه الرساله الى اللغه العربيه 
———————✠——————
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة .""")
@essa .on(admin_cmd(pattern="م6(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,
"""**  ⦑   اوامر الالعاب 1   ⦒  :**
———————✠———————
شرح  ⦙   نسبة وهميه - الأوامر :
الأمر  ⦙ ( .نسبه الحب + الرد ع الشخص )
الأمر  ⦙ ( . نسبه الانحراف + الرد ع الشخص )
الأمر  ⦙ ( .نسبه الكراهيه + الرد ع الشخص )
الأمر  ⦙ ( .نسبه المثليه +الرد ع الشخص )
الأمر  ⦙ ( . نسبه النجاح + الرد ع الشخص )
الأمر  ⦙ ( .نسبه الانوثه + الرد ع الشخص )
الأمر  ⦙ ( .نسبه الغباء + الرد ع الشخص )
———————✠———————
شرح  ⦙  رفع وهمي - الأوامر  :
الأمر  ⦙ ( .رفع زباله + الرد ع الشخص )
الأمر  ⦙ ( .رفع منشئ + الرد ع الشخص )
الأمر  ⦙ ( .رفع مدير + الرد ع الشخص )
الأمر  ⦙ ( .رفع مطور + الرد ع الشخص )
الأمر  ⦙ ( .رفع مثلي + الرد ع الشخص )
الأمر  ⦙ ( .رفع كواد + الرد ع الشخص )
الأمر  ⦙ ( .رفع مرتبط + الرد ع الشخص )
الأمر  ⦙ ( .رفع مطي + الرد ع الشخص )
الأمر  ⦙ ( .رفع كحبه + الرد ع الشخص )
الأمر  ⦙ ( .رفع زوجتي + الرد ع الشخص )
الأمر  ⦙ ( .رفع صاك + الرد ع الشخص )
الأمر  ⦙ ( .رفع صاكه + الرد ع الشخص )
———————✠———————
الأمر  ⦙ ( .كت )
الشرح ⦙ لعبه اسأله كت تويت عشوائيه 
———————✠———————
الأمر  ⦙ ( .اكس او )
الشرح ⦙  لعبه اكس او دز الامر و اللعب ويا صديقك 
———————✠———————
الأمر  ⦙  ( .همسه + الكلام + معرف الشخص )
الشرح  ⦙  يرسل همسه سريه الى معرف الشخص فقط هو يكدر يشوفها  
———————✠———————
الأمر  ⦙  ( .رسم شعار + الاسم )
الشرح ⦙  يرسم شعار للأسم  
———————✠———————
الأمر  ⦙ ( .نص ثري دي + الكلمه )
الشرح ⦙ يقوم بكتابه الكلمه بشكل ثلاثي الابعاد 
———————✠———————
الأمر  ⦙  ( .كلام متحرك + الكلام )
الشرح ⦙ يقوم بكتابه الكلام حرف حرف  
———————✠———————
الأمر ⦙ ( .ملصق متحرك + الكلام )
الشرح  ⦙ يقوم بكتابه الكلام بملصق متحرك  
———————✠———————
الأمر  ⦙  ( .بورن + معرف الشخص + الكلام + الرد ع اي صوره )
الشرح ⦙  قم بتجربه الامر لتعرفه +18  
———————✠———————
الأمر  ⦙ ( .رسم قلوب + الاسم )
الشرح  ⦙  يكتب الاسم ع شكل قلوب  
———————✠———————

⑴  ⦙  ( .كتابه وهمي + عدد الثواني )
⑵  ⦙  ( .فيديو وهمي + عدد الثواني )
⑶  ⦙  ( .صوره وهمي + عدد الثواني )
⑷  ⦙  ( .جهه اتصال وهمي + عدد الثواني )
⑸  ⦙  ( .موقع وهمي + عدد الثواني )
⑹  ⦙  ( .لعب وهمي + عدد الثواني )

الشرح  ⦙ هذا الامر يقوم بالارسال الوهمي يعني يضهر للناس انو نته جاي تكتب او جاي ترسل صوره او ترسل فيديو او ترسل جهه اتصالك حسب الفتره الي تحددها بالثواني
———————✠———————
⑴  ⦙ ( .شوت + الكلمة )
✠ :  امر تسليه جربه وتعرف  
———————✠———————
⑵  ⦙ ( .كتابه + الكلام بالانكلش )
✠ :   يكتب الكلام على ورقه بخط اليد 100%   
———————✠———————
الشرح  ⦙   العـاب اخـرى فقط قم بنسخ الأمر وارسالـة   :- الأوامر :
1. - ( .لعبه تيك توك اربعه )
2. - ( .لعبه تيك توك اثنان 3 )
3. - ( .لعبه ربط أربعة )
4. - ( .لعبه قرعة )
5. - ( .لعبه حجر-ورقة-مقص )
6. - ( .لعبه روليت )
7. - ( .لعبه داما )
8. - ( .لعبه داما تجمع )
———————✠———————
الأمر  ⦙ ( .هديه + الكلام )
الشرح :  قم بارسال الامر بجانبه اكتب اي شيئ واول شخص سيفتحها سوف يكتب اسمه جربها  
———————✠——————— 
الأمر  ⦙ ( .ضفدع + الكلمه )
الشرح :   يدعم انكليزي فقط + يحول الكلمه لكتابه ضفدع جربه وتفهم   
———————✠——————— 
الأمر  ⦙  ( .لافته + الكلمه )
الشرح :   يدعم انكليزي فقط + يحول الكلمه بلافته ملصق متحرك جربه وتعرف    
———————✠——————— 
الأمر ⦙ ( .تكرار_كلمه  + الجملة )
الشرح : يكرر الك كلام الجملة 
———————✠——————— 
الأمر ⦙  (.صفق + الرد على الكلام )
الشرح : جربه وتعرف مضحك 
———————✠——————— 
الأمر  ⦙ ( .حضر وهمي + الرد على شخص )
الشرح : حظر وهمي جربه وتعرف 
———————✠———————
الأمر ⦙ ( .خط ملصق + الكلمه )
الشرح : يدعم انكليزي فقط + يحول الكتابه لملصق 
———————✠———————
الأمر  ⦙ ( .شعر )
الشرح : يرسل الك شعر ميمز او مضحك 
———————✠———————
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة .""")
@essa .on(admin_cmd(pattern="م7(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**  ⦑   بصمات تحشيش 1   ⦒  :**
———————✠——————— 
———————✠———————
(.ص1) ⦙  ابو  عباس  لو  تاكل  خره
(.ص2) ⦙  استمر  نحن  معك
(.ص3) ⦙  افحط  بوجه
(.ص4) ⦙  اكعد  لا  اسطرك  سطره  العباس
(.ص5) ⦙  اللهم  لا  شماته
(.ص6) ⦙  امرع  دينه
(.ص7) ⦙  امشي  بربوك
(.ص8) ⦙  انت  اسكت  انت  اسكت
(.ص9) ⦙  انت  سايق  زربه
(.ص10) ⦙  اوني  تشان
(.ص11) ⦙  برافو  عليك  استادي 
(.ص12) ⦙  بلوك  محترم
(.ص13) ⦙  بووم  في  منتصف  الجبهة 
(.ص14) ⦙  بيتش 
(.ص15) ⦙  تخوني  ؟
(.ص16) ⦙  تره  متكدرلي
(.ص17) ⦙  تعبان  اوي
(.ص18) ⦙  تكذب
(.ص19) ⦙  حسبي  الله
(.ص20) ⦙  حشاش 
(.ص21) ⦙  حقير  
(.ص22) ⦙  خاص  
(.ص23) ⦙  خاله  ما  تنامون  
(.ص24) ⦙  خرب  شرفي  اذا  ابقى  بالعراق 
(.ص25) ⦙  دكات  الوكت  الاغبر  
(.ص26) ⦙  ررردح  
(.ص27) ⦙  سلامن  عليكم  
(.ص28) ⦙  بوم منتصف جبهه   
(.ص29) ⦙  شكد  شفت  ناس  مدودة
(.ص30) ⦙ شلون  ، 
(.ص31) ⦙ صح  لنوم  
(.ص32) ⦙ صمت  
(.ص33) ⦙ ضحكة  مصطفى  الحجي  
(.ص34) ⦙ طماطه  
(.ص35) ⦙ طيح  الله  حضك  
(.ص36) ⦙ فاك  يوو  
(.ص37) ⦙ اني فرحان وعمامي فرحانين
(.ص38) ⦙ لا  تضل  تضرط  
(.ص39) ⦙ لا  تقتل  المتعه  يا  مسلم  
(.ص40) ⦙ لا  مستحيل  
(.ص41) ⦙ لا  والله  شو  عصبي  
(.ص42) ⦙ لش  
(.ص43) ⦙ لك  اني  شعليه  
(.ص44) ⦙ ما  اشرب  
(.ص45) ⦙ مع  الاسف  
(.ص46) ⦙ مقتدى  
(.ص47) ⦙ من  رخصتكم  
(.ص48) ⦙ منو  انت  
(.ص49) ⦙ منورني  
(.ص50) ⦙  نتلاكه  بالدور  الثاني 
(.ص51) ⦙  نستودعكم  الله  
(.ص52) ⦙  ها  شنهي  
(.ص53) ⦙  ههاي  الافكار  حطها ب
(.ص54) ⦙  ليش شنو سببها ليش
(.ص55) ⦙  يموتون  جهالي
(.ص56) ⦙  اريد انام
(.ص57) ⦙  افتحك فتح
(.ص58) ⦙  اكل خره لدوخني
(.ص59) ⦙  السيد شنهو السيد
(.ص60) ⦙  زيج2
(.ص61) ⦙  زيج لهارون
(.ص62) ⦙  زيج الناصرية
(.ص63) ⦙  راقبو اطفالكم
(.ص64) ⦙  راح اموتن
(.ص65) ⦙  ذس اس مضرطة
(.ص66) ⦙  دروح سرسح منا
(.ص67) ⦙  خويه ما دكوم بيه
(.ص68) ⦙  خلصت تمسلت ديلة كافي انجب
(.ص69) ⦙  بعدك تخاف
(.ص70) ⦙  بسبوس
(.ص71) ⦙  اني بتيتة كحبة
(.ص72) ⦙  انعل ابوكم لابو اليلعب وياكم طوبة
(.ص73) ⦙  انت شدخلك
(.ص74) ⦙  انا ماشي بطلع
(.ص75) ⦙  امداك وامده الخلفتك
(.ص76) ⦙  امبيههههه
(.ص77) ⦙  هدي بيبي
(.ص78) ⦙  هاه صدك تحجي
(.ص79) ⦙  مو كتلك رجعني
(.ص80) ⦙  مامرجية منك هاية
(.ص81) ⦙  ليش هيجي
(.ص82) ⦙  كـــافـي
(.ص83) ⦙  كس اخت السيد
(.ص84) ⦙  شنو كواد ولك اني هنا
(.ص85) ⦙  شجلبت
(.ص86) ⦙  شبيك وجه الدبس
(.ص87) ⦙  سييييي
(.ص88) ⦙  زيجج1
(.ص89) ⦙  يموتون جهالي
(.ص90) ⦙  ياخي اسكت اسكت
(.ص91) ⦙  وينهم
(.ص92) ⦙  هيلو سامر وحود
(.ص93) ⦙  هو
(.ص94) ⦙  ههاي الافكار حطها
(.ص96) ⦙  الله يساعدك عيوني
(.ص96) ⦙  يلعن دين امك
(.ص97) ⦙  ياخي والله فشلة
(.ص98) ⦙  صدقني لو اعرف
(.ص99) ⦙  لك قفصوني
(.ص100) ⦙ علاوي حبيب قلبي
(.ص101) ⦙ كال انه 2
(.ص102) ⦙ هي انداست بعد
(.ص103) ⦙ عمو اني سمعي ثقيل
(.ص104) ⦙ خوات كحة 
(.ص105) ⦙ بالامس كانو معي
(.ص106) ⦙ لالتغلط
(.ص107) ⦙ مفخخة
(.ص108) ⦙ قررت احتل العالم
(.ص109) ⦙ صوت صرصور
(.ص110) ⦙ تعال كلكله
(.ص111) ⦙ ياساتر
(.ص112) ⦙ كال انه 1
(.ص113) ⦙ تعال احط رجلي
(.ص114) ⦙ احمد محسن

  ———————✠———————
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة .
""")
@essa .on(admin_cmd(pattern="م8(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑    الاوامر المتحركه للتسلية   ⦒  :**
———————✠——————— 
( .غبي ) ( .تفجير ) ( .قتل ) ( .طوبه ) ( .مربعات ) ( .حلويات ) ( .نار ) ( .هلكوبتر ) ( .اشكال مربع ) ( .دائره )( .قلب ) ( .مزاج ) ( .قرد ) ( .ايد ) ( .العد التنازلي ) ( .الوان قلوب ) ( .عين ) ( .ثعبان ) ( .رجل ) ( .رموز شيطانيه ) ( .قطار ) ( .موسيقى ) ( .رسم ) ( .فراشه ) ( .مكعبات ) ( .مطر ) ( .تحركات ) ( .ايموجيات ) ( .طائره )( .شرطي ) ( .النضام الشمسي ) ( .افكر ) ( .اضحك ) ( .ضايج ) ( .ساعه متحركه )( .بوسه ) ( .قلوب ) ( .رياضه )( .الارض ) ( .قمر ) (.اقمار ) ( .قمور ) ( .زرفه ) ( .بيبي ) ( .تفاعلات ) ( .اخذ قلبي ) 
( .اشوفج السطح ) ( .احبك ) ( .اركض ) ( .روميو ) ( .البنك ) ( .تهكير ) ( .طياره ) ( .مصاصه ) ( .مصه ) ( .جكه ) ( .اركضلي ) ( .حمامه ) ( .فواكه ) ( .الحياة ) ( .هلو ) ( .مربعاتي ) ( .اسعاف ) ( .سمايلي )
———————✠———————
""")

@essa .on(admin_cmd(pattern="م18(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑  اوامر التجميع  ⦒  :**
———————✠——————
( .تجميع المليار )
———————✠——————
( .تجميع العقاب )
———————✠——————
( .تجميع الجوكر )
———————✠——————
( .تجميع المليون )
———————✠——————
( .تجميع العرب )
———————✠——————
( .تجميع متغير )

❕تجميع متغير هوه عباره عن بوت متغير تغيرة انت بنفسك تضع البوت في حالة يوجد هناك بوت اخر تريد ان تجمع فية

ترسل أمر ( `.اضف فار TGMAT1` + يوزر البوت مع الـ @ بدون + )

عندما ترسل الامر وتختار البوت المتغير ترسل ( `.تحديث` ) 
من ثم ترسل ( .تجميع متغير ) 
سوف يجمع بالبوت الي اختاريتة
———————✠——————
شرح الأوامر : ( @L3LL3 ) .
قناه السورس : ( @GM_DU  ) .
جميع الاوامر تكون بدايتها نقطة .""")



# GET MY WHISPER
@essa .on(events.NewMessage(pattern=".فتح همسه"))
async def get_my_whisper_kno_handler(event):
    print (event)
    if event.reply_to != None:
        whisper = await (await event.get_reply_message()).click(0)
        await event.edit(f"تم كشف الهمسة الرساله الموجوده هيه : {whisper.message}")
    else:
        await event.edit('__يجب الرد على الرسالة ليتم كشف الهمسة__')



chat = "@BotFather"
@essa .on(events.NewMessage(outgoing=True, pattern="^.بوت ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

    else:
        await event.edit("قم بوضع الامر + اسم البوت + معرف البوت !!`")
        return

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()



if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineessa (essa ):
        builder = essa .builder
        result = None
        query = essa .text
        await bot.get_me()
        if query.startswith("اوامر الكروب(?: |$)(.*)") and essa .query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الكروب", data="ord1G"),]]
            result = builder.article(title="essa ", text=help2, buttons=buttons, link_preview=False)
            await essa .answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الكروب(?: |$)(.*)"))
async def repoessa (essa ):
    if essa .fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if senzir .reply_to_msg_id:
        await essa .get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الكروب(?: |$)(.*)")
    await response[0].click(essa .chat_id)
    await essa .delete()






@bot.on(admin_cmd(outgoing=True, pattern="(الاوامر|اوامر)(?: |$)(.*)"))
async def repoessa (essa ):
    if essa .fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if essa .reply_to_msg_id:
        await essa .get_reply_message()
    response = await bot.inline_query(TG_BOT, "(الاوامر|اوامر)(?: |$)(.*)")
    await response[0].click(essa .chat_id)
    await essa .delete()

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineessa (senzir ):
        builder = essa .builder
        result = None
        query = essa .text
        await bot.get_me()
        
        if query.startswith("(الاوامر|اوامر)(?: |$)(.*)") and senzir .query.user_id == bot.uid:
            try:
                buttons = [[Button.inline("اوامر السورس", data="orderS1"), Button.inline("اوامر الحساب", data="Ord1Hs1"),],[Button.inline("اوامر الكروب", data="ord1G"), Button.inline("اوامر الالعاب", data="play1"),],[Button.inline("اوامر الصيغ", data="shag1"), Button.inline("اوامر الاغاني", data="ordSONG"),], [Button.inline("اسم وقتي", data="order13"), Button.inline("اوامر السوبرات", data="ordahln1"),],[Button.inline("اوامر التسليه", data="order14") , Button.inline("الفارات", data="ordvars"),],[Button.inline("اوامر البصمات", data="order16") , Button.inline("اوامر التكرار", data="order17"),],[Button.inline("اوامر الزخرفة", data="order18") , Button.inline("اوامر الوسائط", data="order19"),],[Button.inline("اوامر الملصقات", data="order20") , Button.inline("اوامر الصيد", data="order21"),],[Button.inline("اوامر المكالمات", data="order22"),Button.inline("اوامر التجميع", data="order23"),]]
                result = builder.article(title="ESSA ",text=help2,buttons=buttons,link_preview=False)
                await essa .answer([result] if result else None)
            except BotInlineDisabledError: 
                await essa .send_message( "يجب تفعيل الاونلاين من بوت فاذر اولا " )
   


@essa .tgbot.on(CallbackQuery(data=re.compile(rb"orders")))
@check_owner
async def inlineessa (essa ):
    text = "**✠︙ قـائمـه الاوامـر :**\n**✠︙ قنـاه السـورس :** @ESSA \n**✠︙ شـرح اوامـر السـورس : @HG_STF** "
    buttons = [[Button.inline("اوامر السورس", data="orderS1"), Button.inline("اوامر الحساب", data="Ord1Hs1"),],[Button.inline("اوامر الكروب", data="ord1G"), Button.inline("اوامر الالعاب", data="play1"),],[Button.inline("اوامر الصيغ", data="shag1"), Button.inline("اوامر الاغاني", data="ordSONG"),], [Button.inline("اسم وقتي", data="order13"), Button.inline("اوامر السوبرات", data="ordahln1"),],[Button.inline("اوامر التسليه", data="order14") , Button.inline("الفارات", data="ordvars"),],[Button.inline("اوامر البصمات", data="order16") , Button.inline("اوامر التكرار", data="order17"),],[Button.inline("اوامر الزخرفة", data="order18") , Button.inline("اوامر الوسائط", data="order19"),],[Button.inline("اوامر الملصقات", data="order20") , Button.inline("اوامر الصيد", data="order21"),],[Button.inline("اوامر المكالمات", data="order22"),Button.inline("اوامر التجميع", data="order23"),]]
    await essa .edit(text, buttons=buttons)

@essa .tgbot.on(CallbackQuery(data=re.compile(rb"order23")))
@check_owner
async def inlineessa (essa ):
    text = """**⦑  اوامر التجميع  ⦒  :**
———————✠——————
( .تجميع المليار )
———————✠——————
( .تجميع العقاب )
———————✠——————
( .تجميع الجوكر )
———————✠——————
( .تجميع المليون )
———————✠——————
( .تجميع العرب )
———————✠——————
( .تجميع متغير )

❕تجميع متغير هوه عباره عن بوت متغير تغيرة انت بنفسك تضع البوت في حالة يوجد هناك بوت اخر تريد ان تجمع فية

ترسل أمر ( `.اضف فار TGMAT1` + يوزر البوت مع الـ @ بدون + )

عندما ترسل الامر وتختار البوت المتغير ترسل ( `.تحديث` ) 
من ثم ترسل ( .تجميع متغير ) 
سوف يجمع بالبوت الي اختاريتة
———————✠——————
الامر : ( .تجميع دعمكم)
الايقاف:  ( .ايقاف تجميع دعمكم ) 

❕- يجمع في بوت دعمكم ايضا مع الاشتراك التلقائي
———————✠——————
شرح الأوامر : ( @L3LL3 ) .
قناه السورس : ( @GM_DU  ) .
جميع الاوامر تكون بدايتها نقطة ."""

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await essa .edit(text, buttons=buttons)



@essa .tgbot.on(CallbackQuery(data=re.compile(rb"order22")))
@check_owner
async def inlineessa (essa ):
    text = """** ⦑   اوامر المكالمات   ⦒  : **
( اوامر للمكالمات ) : 
———————✠———————
الأمر ( .تشغيل صوتي + الرد على الصوت )
• لتشغيل اغنية في المكالمة .
———————✠———————
الأمر ( .تشغيل فيديو + الرد على الفيديو )
• لتشغيل فيديو في المكالمة
———————✠———————
الأمر ( .اغلاق البث )
• لاغلاق الفيديو او الاغنية التي في المكالمة .  """

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await essa .edit(text, buttons=buttons)  



@essa .tgbot.on(CallbackQuery(data=re.compile(rb"order20")))
@check_owner
async def inlineessa (essa ):
    text = """** ⦑   اوامر الملصقات   ⦒  : **
———————✠———————
 ⑴ ⦙ .جلب الملصقات + الرد على الملصق
✠  : يجلب اليك ملصقات الحزمه
———————✠———————
⑵ ⦙  .انشاء حزمه ملصقات + الرد على الملصق
✠  : يضع الملصق بحزمه بشكل مقصوص
———————✠———————
⑶ ⦙ .جلب معلومات الملصق + الرد على الملصق )
✠  : يجلب لك جميع معلومات الملصق
———————✠———————
⑷ ⦙ .ملصق + اسم الحزمه او الملصق
✠  : يبحث عن اسم الحزمه او الملصق ويجلبه اليك
———————✠———————
  ⦑   شرح اوامر الملصقات هنا  :  https://t.me/L3LL3/4720  ⦒
"""

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await essa .edit(text, buttons=buttons)  


@essa .tgbot.on(CallbackQuery(data=re.compile(rb"order21")))
@check_owner
async def inlineessa (essa ):
    text = """**⦑   اوامر الصيد   ⦒  :
———————✠———————
 الأمر  ⦙ ( .صيد + النوع )
النوع : ( ثلاثيات - سداسي حرفين - خماسي - سداسيات - سباعيات - بوتات )
———————✠———————
 أمر ⦙ ( .حالة الصيد )
لمعرفة عدد محاولات الصيد بكل الأنواع
———————✠———————
أمر ⦙ ( .اغلاق الصيد )
لأيقاف جميع انواع الصيد
———————✠———————
أمر ⦙ ( .سحب + اليوزر )
عندما ينفك اليوزر تلقائيا يصيدة حسابك ويخلية في قناة
———————✠———————
أمر ⦙ ( .اغلاق سحب + اليوزر )
يلغي عملية سحب من اليوزر المحد
———————✠———————**
CH : @senzir 
✠︙ يوجد شرح مفصل عن الامر هنا : https://t.me/L3LL3/4832
"""

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await essa .edit(text, buttons=buttons)  
  
@essa .tgbot.on(CallbackQuery(data=re.compile(rb"order18")))
@check_owner
async def inlineessa (essa ):
    text = """** ⦑   لأوامر الزخرفة   ⦒  : **
———————✠———————
الأمر ( .اغلاق الزخرفة الأنجليزية )
الأمر ( .فتح الزخرفة الأنجليزية )
• لزخرفة اي شيئ تكتبة بل انكليزية 
———————✠———————
لتفعيل خط غامق
أرسل : ( .خط غامق )
لتعطيل الخط ارسل الامر نفسة مرة اخرى وسوف يتعطل
———————✠———————
لتفعيل خط رمز 
أرسل : ( .تفعيل خط رمز )
لتعطيل الخط ارسل الامر نفسة مرة اخرى وسوف يتعطل
———————✠———————
لتفعيل خط مائل 
أرسل : ( .تفعيل خط مائل )
لتعطيل الخط ارسل الامر نفسة مرة اخرى وسوف يتعطل
———————✠———————
⑴  ⦙ .غمق + الرد على رساله 
✠ :  يحول خط الرسالة غامقه  
———————✠——————— 
⑵  ⦙ .ينسخ + الرد على رساله 
✠ :  يحول خط الرساله الى كلام ينسخ  
———————✠———————
⑶  ⦙ .خط سفلي + الرد على رساله 
✠ :   يضيف الى خط رساله خط سفلي 
———————✠——————— 
⑷  ⦙ .كتابه + الكلام بالانكلش 
✠ : يكتب الكلام على ورقه بخط اليد 100% ❝ 
 ———————✠——————— 
⑸  ⦙ .زخرفه_انكليزي + الاسم 
✠ : يزخرف الاسم الانكليزي لعده زخرفات يجب ان يكون الاسم مكتوب سمول 
———————✠———————
⑹ ⦙ .زخرفه_عربي + الاسم 
✠ : يزخرف الاسم العربي لعده زخرفات 
———————✠———————
⑺ ⦙  .بايوهات1
✠ :  يعطيك بايو انستا متعدده 1 
———————✠———————
⑻ ⦙ .بايوهات2
✠ :  يعطيك بايو انستا متعدده 2 
———————✠———————
⑼ ⦙  .رموز1
✠ :  يعطيك رموز للزخرفه 1 
———————✠———————
10 ⦙ .رموز2
✠ :  يعطيك رموز للزخرفه2 
———————✠———————

يوجد شرح مفصل عن اوامر زخرفه هنا : https://t.me/Explanations_Rizer/3
"""

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await essa .edit(text, buttons=buttons)  
  
  
@essa .tgbot.on(CallbackQuery(data=re.compile(rb"order19")))
@check_owner
async def inlineessa (essa ):
    text = """**⦑   اوامر الوسائـط   ⦒  :**
———————✠———————
⑴ ⦙ .سمول + الرد على ملصق او صوره او فيديو 
✠  : يقوم بتصغير الوسائط 
———————✠———————
⑵ ⦙ .عكس الالوان + الرد على ملصق او صوره او فيديو
✠  : يعكس الالوان الموجودة في الوسائط
———————✠———————
⑶ ⦙ .فلتر احمر + الرد على ملصق او صوره او فيديو
✠  : يقوم باضافه فلتر احمر الى وسائط
———————✠———————
⑷ ⦙ .فلتر رصاصي + الرد على ملصق او صوره او فيديو
✠  :  يقوم باضافه فلتر رصاصي الى وسائط
———————✠———————
⑸ ⦙ .يمين الصوره + الرد على ملصق او صوره او فيديو )
✠  : يقوم بتحويل وجهه الوسائط الى اليمين
———————✠———————
⑹ ⦙ .قلب الصوره + الرد على ملصق او صوره او فيديو
✠  : يقلب الوسائط من فوق لتحت
———————✠———————
⑺ ⦙ .زوم + الرد على ملصق او صوره او فيديو
✠  :  يقوم بتقريب على الوسائط
———————✠———————
⑻ ⦙ .اطار + الرد على ملصق او صوره او فيديو
✠  : يضيف اطار الى الوسائط
———————✠———————
⑼ ⦙ .لوقو + الاسم
✠  : يقوم بصنع logo خاص بك
———————✠———————
  ⦑   شرح اوامر الوسائط هنا :  https://t.me/Explanations_Rizer/4  ⦒
"""

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await essa .edit(text, buttons=buttons)  
  
@essa .tgbot.on(CallbackQuery(data=re.compile(rb"order16")))
@check_owner
async def inlineessa (essa ):
    text = """**  ⦑   بصمات تحشيش 1   ⦒  :**
———————✠———————
(.ص1) ⦙  ابو  عباس  لو  تاكل  خره
(.ص2) ⦙  استمر  نحن  معك
(.ص3) ⦙  افحط  بوجه
(.ص4) ⦙  اكعد  لا  اسطرك  سطره  العباس
(.ص5) ⦙  اللهم  لا  شماته
(.ص6) ⦙  امرع  دينه
(.ص7) ⦙  امشي  بربوك
(.ص8) ⦙  انت  اسكت  انت  اسكت
(.ص9) ⦙  انت  سايق  زربه
(.ص10) ⦙  اوني  تشان
(.ص11) ⦙  برافو  عليك  استادي 
(.ص12) ⦙  بلوك  محترم
(.ص13) ⦙  بووم  في  منتصف  الجبهة 
(.ص14) ⦙  بيتش 
(.ص15) ⦙  تخوني  ؟
(.ص16) ⦙  تره  متكدرلي
(.ص17) ⦙  تعبان  اوي
(.ص18) ⦙  تكذب
(.ص19) ⦙  حسبي  الله
(.ص20) ⦙  حشاش 
(.ص21) ⦙  حقير  
(.ص22) ⦙  خاص  
(.ص23) ⦙  خاله  ما  تنامون  
(.ص24) ⦙  خرب  شرفي  اذا  ابقى  بالعراق 
(.ص25) ⦙  دكات  الوكت  الاغبر  
(.ص26) ⦙  ررردح  
(.ص27) ⦙  سلامن  عليكم  
(.ص28) ⦙  بوم منتصف جبهه   
(.ص29) ⦙  شكد  شفت  ناس  مدودة
(.ص30) ⦙ شلون  ، 
(.ص31) ⦙ صح  لنوم  
(.ص32) ⦙ صمت  
(.ص33) ⦙ ضحكة  مصطفى  الحجي  
(.ص34) ⦙ طماطه  
(.ص35) ⦙ طيح  الله  حضك  
(.ص36) ⦙ فاك  يوو  
(.ص37) ⦙ اني فرحان وعمامي فرحانين
(.ص38) ⦙ لا  تضل  تضرط  
(.ص39) ⦙ لا  تقتل  المتعه  يا  مسلم  
(.ص40) ⦙ لا  مستحيل  
(.ص41) ⦙ لا  والله  شو  عصبي  
(.ص42) ⦙ لش  
(.ص43) ⦙ لك  اني  شعليه  
(.ص44) ⦙ ما  اشرب  
(.ص45) ⦙ مع  الاسف  
(.ص46) ⦙ مقتدى  
(.ص47) ⦙ من  رخصتكم  
(.ص48) ⦙ منو  انت  
(.ص49) ⦙ منورني  
(.ص50) ⦙  نتلاكه  بالدور  الثاني 
(.ص51) ⦙  نستودعكم  الله  
(.ص52) ⦙  ها  شنهي  
(.ص53) ⦙  ههاي  الافكار  حطها ب
(.ص54) ⦙  ليش شنو سببها ليش
(.ص55) ⦙  يموتون  جهالي
(.ص56) ⦙  اريد انام
(.ص57) ⦙  افتحك فتح
(.ص58) ⦙  اكل خره لدوخني
(.ص59) ⦙  السيد شنهو السيد
(.ص60) ⦙  زيج2
(.ص61) ⦙  زيج لهارون
(.ص62) ⦙  زيج الناصرية
(.ص63) ⦙  راقبو اطفالكم
(.ص64) ⦙  راح اموتن
(.ص65) ⦙  ذس اس مضرطة
(.ص66) ⦙  دروح سرسح منا
(.ص67) ⦙  خويه ما دكوم بيه
(.ص68) ⦙  خلصت تمسلت ديلة كافي انجب
(.ص69) ⦙  بعدك تخاف
(.ص70) ⦙  بسبوس
(.ص71) ⦙  اني بتيتة كحبة
(.ص72) ⦙  انعل ابوكم لابو اليلعب وياكم طوبة
(.ص73) ⦙  انت شدخلك
(.ص74) ⦙  انا ماشي بطلع
(.ص75) ⦙  امداك وامده الخلفتك
(.ص76) ⦙  امبيههههه
(.ص77) ⦙  هدي بيبي
(.ص78) ⦙  هاه صدك تحجي
(.ص79) ⦙  مو كتلك رجعني
(.ص80) ⦙  مامرجية منك هاية
(.ص81) ⦙  ليش هيجي
(.ص82) ⦙  كـــافـي
(.ص83) ⦙  كس اخت السيد
(.ص84) ⦙  شنو كواد ولك اني هنا
(.ص85) ⦙  شجلبت
(.ص86) ⦙  شبيك وجه الدبس
(.ص87) ⦙  سييييي
(.ص88) ⦙  زيجج1
(.ص89) ⦙  يموتون جهالي
(.ص90) ⦙  ياخي اسكت اسكت
(.ص91) ⦙  وينهم
(.ص92) ⦙  هيلو سامر وحود
(.ص93) ⦙  هو
(.ص94) ⦙  ههاي الافكار حطها
(.ص96) ⦙  الله يساعدك عيوني
(.ص96) ⦙  يلعن دين امك
(.ص97) ⦙  ياخي والله فشلة
(.ص98) ⦙  صدقني لو اعرف
(.ص99) ⦙  لك قفصوني
(.ص100) ⦙ علاوي حبيب قلبي
(.ص101) ⦙ كال انه 2
(.ص102) ⦙ هي انداست بعد
(.ص103) ⦙ عمو اني سمعي ثقيل
(.ص104) ⦙ خوات كحة 
(.ص105) ⦙ بالامس كانو معي
(.ص106) ⦙ لالتغلط
(.ص107) ⦙ مفخخة
(.ص108) ⦙ قررت احتل العالم
(.ص109) ⦙ صوت صرصور
(.ص110) ⦙ تعال كلكله
(.ص111) ⦙ ياساتر
(.ص112) ⦙ كال انه 1
(.ص113) ⦙ تعال احط رجلي
(.ص114) ⦙ احمد محسن

  ———————✠———————
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF ) .
جميع الاوامر تكون بدايتها نقطة .  """

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await essa .edit(text, buttons=buttons)


@essa .tgbot.on(CallbackQuery(data=re.compile(rb"order17")))
@check_owner
async def inlineessa (essa ):
    text = """ **⦑   اوامر التكرار    ⦒  : **
———————✠——————— 
الامر ( .نشر - عدد الثواني - عدد مرات - الكلام ) 
لايقاف ( .اغلاق النشر ) 

❕- امر نشر تلقائي ولاكن بتحديث افضل وتصميم افضل و اسرع
———————✠——————— 
الشرح  ⦙ ( .تكرار + الكلمة + العدد )
الأمر :  يرسل الكلمة يكررها على عدد المرات  
———————✠———————  
الأمر ⦙ ( .تكرار حزمه الملصقات + الرد على ملصق )
الشرح :   يرسل لك جميع ملصقات الموجوده في حزمه لل الملصق الي عملت رد له   
———————✠———————
الأمر  ⦙ ( .تكرار_احرف  + الكلمة )
الشرح :   يكرر الك احرف الكلمة حتى لو جملة 
———————✠———————
الأمر  ⦙ ( .تكرار_كلمه  + الجملة )
الشرح : يكرر الك كلام الجملة 
———————✠——————— 
الأمر  ⦙ ( .مؤقت  + عدد الثواني + عدد مرات + الجملة )
الشرح : يرسل اليك الجملة كل وقت معين 
———————✠———————
الامر ( .اسم متقطع + الاسم )
ايقاف ( .ايقاف اسم متقطع )
❕يضع الاسم في حسابك ويقطع فية شبية للاسم وقتي 
———————✠——————
الامر ( .تصحيح + الجملة  + الرد على جملة )
❕- قم بارسال جملة عشوائية من ثم قم بالرد بالامر و بجانبة الكلمة التي تريد ان تضعها بدلا منة سوف يصحح الجملة ولاكن بشكل مقطع
———————✠——————
الامر ( .تكرار متقطع + عدد مرات + عدد ثواني + كلمتين او اكثر )

❕- يكرر الكلمة بنفس الرسالة بشكل متقطع
———————✠——————
يوجد شرح مفصل للتكرار هنا : https://t.me/Explanations_Rizer/5 
قناه السورس : ( @GM_DU  ) .
جميع الاوامر تكون بدايتها نقطة .
"""

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await essa .edit(text, buttons=buttons)



      
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الحساب(?: |$)(.*)"))
async def repoessa (essa ):
    if essa .fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if essa .reply_to_msg_id:
        await essa .get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الحساب(?: |$)(.*)")
    await response[0].click(senzir .chat_id)
    await essa .delete()
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineessa (essa ):
        builder = essa .builder
        result = None
        query = essa .text
        await bot.get_me()
        if query.startswith("اوامر الالعاب(?: |$)(.*)") and essa .query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الالعاب", data="ord1pl"),]]
            result = builder.article(title="ESSA ", text=help2, buttons=buttons, link_preview=False)
            await essa .answer([result] if result else None)           
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الالعاب(?: |$)(.*)"))
async def repoessa (essa ):
    if essa .fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if essa .reply_to_msg_id:
        await essa .get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الالعاب(?: |$)(.*)")
    await response[0].click(essa .chat_id)
    await essa .delete()
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineessa (essa ):
        builder = essa .builder
        result = None
        query = essa .text
        await bot.get_me()
        if query.startswith("اوامر الصيغ(?: |$)(.*)") and essa .query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الصيغ", data="ordsag1"),]]
            result = builder.article(title="ESSA ", text=help2, buttons=buttons, link_preview=False)
            await essa .answer([result] if result else None)
            
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الصيغ(?: |$)(.*)"))
async def repoessa (essa ):
    if essa .fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if essa .reply_to_msg_id:
        await essa .get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الصيغ(?: |$)(.*)")
    await response[0].click(essa .chat_id)
    await essa .delete()            

if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlinesenzir (senzir ):
        builder = essa .builder
        result = None
        query = essa .text
        await bot.get_me()
        if query.startswith("اوامر الحساب(?: |$)(.*)") and essa .query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الحساب", data="hsb1"),]]
            result = builder.article(title="ESSA ", text=help2, buttons=buttons, link_preview=False)
            await essa .answer([result] if result else None)
            
@essa .tgbot.on(CallbackQuery(data=re.compile(rb"orderS1")))
@check_owner
async def inlineessa (ESSA ):
    text = """ ** ⦑   اوامر السورس   ⦒  :**
———————✠———————
الأمر ⦙ ( .السورس )
الشرح  : يضهر لك معلومات السورس ومدة تنصيبك او امر .فحص ❝
———————✠——————— 
الأمر ⦙ ( .رابط التنصيب )
الشرح  : سوف يعطيك رابط التنصيب ❝ 
———————✠——————— 
الأمر ⦙ ( .حساب كيثاب + اسم الحساب )
الشرح  : ينطيك معلومات الحساب وسورساته بموقع جيت هوب ❝ 
———————✠——————— 
الأمر ⦙ ( .المده )
الشرح  : يضهر لك مدة تشغيل بوت تليثون لديك 
———————✠———————
الأمر ⦙ ( .تحميل ملف + الرد ع الملف )
الشرح : يحمل ملفات تليثون 
———————✠———————
الأمر ⦙ ( .مسح ملف + الرد ع الملف )
الشرح :  يمسح الملف الي حملته  
———————✠———————
الأمر ⦙ ( .تحديث )
الشرح :  امر لأعاده التشغيل وتحديث ملفات السورس وتسريع التليثون 
———————✠———————
الأمر ⦙ ( .اطفاء مؤقت + عدد الثواني )
الشرح : يقوم بأطفاء التليثون بعدد الثواني الي ضفتها  عندما تخلص الثواني سيتم اعاده تشغيل التليثون 
———————✠———————
الأمر ⦙ ( .الاوامر ) 
الشرح :   لأضهار جميع اوامر السورس اونلاين
———————✠———————
الأمر ⦙ ( .اوامري )
الشرح :   لأضهار جميع اوامر السورس كتابه بدون اونلاين
———————✠———————
الأمر ⦙ ( .استخدامي )
الشرح :   يضهر لك كمية استخدامك لتليثون
———————✠———————
الأمر ⦙ ( .تاريخ التنصيب )
الشرح :   يضهر لك تاريخ تنصيبك
———————✠———————
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة ."""
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await essa .edit(text, buttons=buttons)
@essa .tgbot.on(CallbackQuery(data=re.compile(rb"order13")))
@check_owner
async def inlineessa (essa ):
    text = """**⦑   اوامر الوقتي   ⦒  :**
———————✠———————
 الأمر  ⦙ ( .اسم وقتي )
الشرح : يضع الوقت المزخرف في اسمك تلقائيا 
———————✠———————
 الأمر  ⦙ ( .نبذة وقتية )
الشرح  : يضع الوقت المزخرف في نبذه الخاصه بك تلقائيا
انتبة الامر بل تاء مربوطة ( ة ) وليس ( ه  )
———————✠———————
الأمر ⦙ ( .صورة وقتية )
الشرح : يضع لك الوقت لمزخرف في صورتك تغير تلقائي 
انتبة الامر بل تاء مربوطة ( ة ) وليس ( ه  )
———————✠———————
**شرح الايقاف :**
( .ايقاف صورة وقتية )
( .ايقاف نبذة وقتية )
( .ايقاف اسم وقتي )

انتبة الامر بل تاء مربوطة ( ة ) وليس ( ه  )
———————✠———————
 ✠︙ يوجد شرح مفصل عن الامر هنا : https://t.me/L3LL3/4484
"""
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)
@ESSA .tgbot.on(CallbackQuery(data=re.compile(rb"order14")))
@check_owner
async def inlineESSA (ESSA ):
    text = """**⦑    الاوامر المتحركه للتسلية   ⦒  :**
———————✠——————— 
( .غبي ) ( .تفجير ) ( .قتل ) ( .طوبه ) ( .مربعات ) ( .حلويات ) ( .نار ) ( .هلكوبتر ) ( .اشكال مربع ) ( .دائره )( .قلب ) ( .مزاج ) ( .قرد ) ( .ايد ) ( .العد التنازلي ) ( .الوان قلوب ) ( .عين ) ( .ثعبان ) ( .رجل ) ( .رموز شيطانيه ) ( .قطار ) ( .موسيقى ) ( .رسم ) ( .فراشه ) ( .مكعبات ) ( .مطر ) ( .تحركات ) ( .ايموجيات ) ( .طائره )( .شرطي ) ( .النضام الشمسي ) ( .افكر ) ( .اضحك ) ( .ضايج ) ( .ساعه متحركه )( .بوسه ) ( .قلوب ) ( .رياضه )( .الارض ) ( .قمر ) (.اقمار ) ( .قمور ) ( .زرفه ) ( .بيبي ) ( .تفاعلات ) ( .اخذ قلبي ) 
( .اشوفج السطح ) ( .احبك ) ( .اركض ) ( .روميو ) ( .البنك ) ( .تهكير ) ( .طياره ) ( .مصاصه ) ( .مصه ) ( .جكه ) ( .اركضلي ) ( .حمامه ) ( .فواكه ) ( .الحياة ) ( .هلو ) ( .مربعاتي ) ( .اسعاف ) ( .سمايلي )
———————✠———————"""

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)
@ESSA .tgbot.on(CallbackQuery(data=re.compile(rb"ordvars")))
@check_owner
async def inlineessa (ESSA ):
    text = """ ( اوامر الفارات وتغيرات ) :
———————✠———————
• لتغير شكل امر السورس او  الفحص اضغط هنا  ↶
https://t.me/Teamtelethon/36
  • لتغير صوره او فيديو امر الفحص اضغط هنا ↶
https://t.me/Teamtelethon/39
  • لتغير كليشة امر حماية الخاص اضغط هنا ↶
https://t.me/Teamtelethon/35
  • لوضع صوره او فيديو حماية الخاص اضغط هنا ↶
https://t.me/Teamtelethon/38
  • لتغير عدد تحذيرات حماية الخاص اضغط هنا ↶
https://t.me/Teamtelethon/45
  • لتغير نبذه الوقتيه اضغط هنا ↶
https://t.me/Teamtelethon/54
  • لتغير صوره وقتيه اضغط هنا ↶
 https://t.me/Teamtelethon/46 
  • لتغير خط زخرفه اسم وقتي اضغط هنا ↶
 https://t.me/Teamtelethon/59
  •  لوضع ايموجي بجانب اسم وقتي اضغط هنا ↶
 https://t.me/Teamtelethon/37
• لتغير امر من الاوامر اضغط هنا ↶
https://t.me/L3LL3/4718
• لكيفيه حذف الفار اضغط هنا ↶
https://t.me/Teamtelethon/51
———————✠——————— 
قناه المتغيرات او الفارات : @teamtelethon
شرح الأوامر : ( @L3LL3 ) .
قناه السورس : ( @GM_DU  ) .
جميع الاوامر تكون بدايتها نقطة .    """

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)

@ESSA .tgbot.on(CallbackQuery(data=re.compile(rb"Ord1Hs1")))
@check_owner
async def inlineessa (ESSA ):
    text = "**✠  ⦑   اوامر الحساب   ⦒  :**"
    buttons = [[Button.inline("اوامر الحساب  1", data="hsb1"),Button.inline("اوامر الحساب  2", data="hsbb2")],[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)

@senzir .tgbot.on(CallbackQuery(data=re.compile(rb"hsbb2")))
@check_owner
async def inlineessa (ESSA ):
    text = """** ⦑  اوامر الحساب 2  ⦒  :**
    ———————✠——————
الامر - ( .ابلاغ قناة - عدد ثواني - عدد مرات - يوزر القناة )
❕- يقوم بتبليغ باستمرار باختيار العدد و الثواني بين كل بلاغ 
———————✠———————
اضافه امر لتفعيل تقييد المحتوى :
(.قيد + معرف قناتك )
———————✠———————
اضافه امر لمعرفة نوع المعرف اذا كان لبوت او قناه لو مجموعه لو حساب شخصي :
( .نوعه + معرف الشخص )
———————✠———————
اضافه امر حذف المحادثه بينك وبين الشخص الاخر : 
( .احذف + معرف الشخص )
———————✠———————
اضافه امر اضهار جميع مجموعاتي : 
( .كروباتي  )
———————✠———————
اضافه امر اضهار جميع الحاضرهم : 
( .الحاظرهم  )
———————✠———————
الأمر : .تجميع نقاط
لتعديل تجميع  الى بوت اخر أرسل : 
( .اضف فار TGMABOT + يوزر البوت مع الـ @
———————✠———————
تم اضافه ميزات بوت وعد : 

اضافة امر استثمار تلقائي : 
( .استثمار وعد + عدد الاعادة للأمر )
للايقاف :
( .ايقاف استثمار وعد )
———————✠———————
اضافة امر راتب تلقائي : 
( .راتب وعد + عدد الاعادة للأمر )
لايقاف الامر : 
( .ايقاف راتب وعد )
———————✠———————
اضافة امر سرقة وعد :
( .سرقة وعد + الايدي ) 
لايقاف الامر 
( .ايقاف سرقة وعد )
———————✠———————
اضافة امر بخشيش تلقائي  : 
( .بخشيش وعد + عدد مرات الاعادة )
لايقاف الامر :
( .ايقاف بخشيش وعد )
———————✠———————
اضافة امر كلمات تلقائي :  
( .كلمات وعد + عدد الاعادة للأمر )
———————✠———————
الأمر ( .فتح الترجمة )
الأمر ( .اغلاق الترجمة )
• لترجمة اي شي تكتبة من العربي الى الأنكليزي
———————✠———————
امر : ( .تصفية قنواتي )
( يحذف جميع القنوات التي في حسابك ماعدا التي حسابك صاعد فيها المشرف او المالك بها لايحذفها )
———————✠———————
امر : ( .تصفية مجموعاتي )
( يحذف جميع المجموعات التي في حسابك ماعدا المجموعات التي حسابك صاعد فيها المشرف او المالك بها لايحذفها )
———————✠———————
امر : ( .تصفية محادثاتي )
( يحذف جميع المحادثات التي في حسابك )
———————✠———————
امر : ( .تصفية بوتاتي )
(يحذف جميع البوتات التي في محادثاتك ايضا لايحذف البوتات التي قمت بصنعها من بوت فاذر  )
———————✠———————
الأمر ( .كشف همسة + الرد على همسة )
• يفتح الهمسة التي موجة اليك فقط
———————✠———————
الأمر ( .فتح تعديل الميديا )
الأمر ( .اغلاق تعديل الميديا )
• لمسح اي تعديل يصير في الفيديوهات او صور او روابط
———————✠———————
اضافه أمر حفض الصوره الوقتية تلقائيا

الأمر : ( .تشغيل حفض الوقتية )
لتعطيل الأمر : ( .ايقاف حفض الوقتية ) 
———————✠———————
تم اضافه أمر اشتراك الاجباري في الخاص :

لتفعيل الأشتراك بالقناة أرسل : ( .اشتراك خاص)
لتفعيل الأشتراك بالكروب أرسل : ( .اشتراك كروب )

لتعطيل الأشتراك بالقناة أرسل : ( .تعطيل خاص)
لتعطيل الأشتراك بالكروب أرسل : ( .تعطيل كروب )

لاضافه قناة او مجموعة الى الأشتراك الأجباري أرسل :
( .اضف فار pchan + ايدي القناة أو أيدي المجموعة ) 

أستخدم أمر (.الايدي) لاستخراج الايدي من المجموعة أو القناة

من ثم أرسل امر ( .بوتي ) 
يعطيك معرف بوتك قم برفعه في القناة التي وضعت فيها الاشتراك جباري
 ———————✠———————
يوجد شرح بتفصيل هنا :
https://t.me/L3LL3/4833
شرح الأوامر : (@E_I_I7) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة ."""
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)

@ESSA .tgbot.on(CallbackQuery(data=re.compile(rb"hsb1")))
@check_owner
async def inlineessa (ESSA ):
    text = """**  ⦑   اوامـر الحـسـاب  ⦒ : **
———————✠———————
الأمر︙( .معرفه + الرد ع الشخص )
شرح︙سيجلب لك معرف الشخص 
———————✠———————
الأمر︙( .سجل الاسماء + الرد ع الشخص ) 
شرح︙يجلب لك اسماء الشخص القديمه 
———————✠———————
الأمر︙( .انشاء بريد )
شرح︙ينشئ لك بريد وهمي 
———————✠———————
الأمر︙( .ايدي + الرد ع الشخص )
شرح︙سيعطيك معلومات الشخص 
———————✠———————
الأمر︙( . الايدي الرد ع الشخص )
شرح︙سوف يعطيك ايدي المجموعه او ايدي حسابك 
———————✠———————
الأمر︙( .معلومات تخزين المجموعه )
شرح︙يجلب لك جميع معلومات الوسائط  
———————✠———————
الأمر︙( .تخزين الخاص تشغيل )
شرح︙يخزن لك جميع الرسائل التي  في الخاص 
———————✠———————
الأمر︙( .تخزين الخاص ايقاف )
شرح︙يوقف  تخزين الرسائل اليك في الخاص 
———————✠———————
الأمر︙( .تخزين الكروبات تشغيل )
شرح︙يخزم جميع الرسائل التي يتم رد عليك 
———————✠———————
الأمر︙( .تخزين الكروبات ايقاف )
شرح︙يوقف لك جميع تخزين رسائل
———————✠———————
 الأمر  ︙( .صورته + الرد ع الشخص )
شرح︙يجلب صوره الشخص
———✠———
الأمر︙( .رابطه + الرد ع الشخص )
شرح︙يجلب لك رابط الشخص
———✠———
الأمر︙( .اسمه + الرد ع الشخص )
شرح︙يجلب لك اسم الشخص الذي تم رد عليه 
———✠———
الأمر︙( .نسخ + الرد ع الرساله )
شرح︙يرسل الرساله التي تم رد عليها 
———✠———
الأمر︙( .كورونا + اسم المدينه )
شرح︙يجلب لك مرض كورونا و معلومات
———✠———
الأمر︙( .الاذان + اسم المدينه )
شرح︙يجلب لك معلومات الاذان 
———✠———
الأمر︙( .رابط تطبيق + اسم التطبيق )
شرح︙يرسل رابط التطبيق مع معلوماته 
———✠———
الأمر︙( .تاريخ الرساله + الرد ع الرساله )
شرح︙يجلب لك تاريخ الرساله بالتفصيل 
———✠———
الأمر︙( .بنك )
شرح︙يقيس سرعه استجابه 
———✠———
الأمر︙( .سرعه الانترنيت )
شرح︙يجلب لك سرعه الانترنيت لديك 
———✠———
الأمر︙( .الوقت )
شرح︙يضهر لك الوقت والتاريخ 
———✠———
الأمر︙( .وقتي )
شرح︙الوقت والتاريخ شكل اخر
———✠———
الأمر︙.حالتي 
✠  :  لفحص الحظر
———✠———
الأمر︙.طقس + اسم المدينه 
شرح︙ يعطي لك طقس المدينه 
———✠———
الأمر︙ .طقوس + اسم المدينه 
شرح︙ يعطي لك طقس المدينه 
———✠———
الأمر︙ .مدينه الطقس + اسم المدينه 
شرح︙ لتحديد طقس المدينه تلقائي
———✠———
الأمر︙ .ازاله التوجيه + الرد على رساله
شرح︙ يرسل اليك الرساله بدون توجية
———✠———
الأمر︙.كشف + الرد على شخص
شرح︙ رد على شخص يفحص الحظر
———✠———
الأمر︙.وضع بايو + الرد على البايو
شرح︙ يضع الكلمه في البايو الخاص بك
———✠———
الأمر︙.وضع اسم + الرد على الاسم
شرح︙ يضع الاسم في اسمك
———✠———
الأمر︙.وضع صوره + الرد على صوره
شرح︙يضع الصوره في حسابك
———✠———
الأمر︙.معرفاتي
شرح︙يجلب جميع معرفاتك
———✠———
الأمر︙ .تحويل ملكية + معرف الشخص
شرح︙يحول ملكيه القناه او المجموعه 
———✠———
الأمر︙ .انتحال + الرد على الشخص
شرح︙ ينتحل الشخص ويضع صورته و نبذته و اسمه في حسابك
———✠———
الأمر︙.الغاء الانتحال + الرد على الشخص
شرح︙ يقوم بالغاء الانتحال 
———✠———
الأمر︙.ازعاج + الرد على شخص
شرح︙يقوم بتكرار الرسائل الشخص 
———✠———
الأمر︙.الغاء الازعاج
شرح : يوقف جميع الازعاجات في المجموعه 
 ———✠———
 الأمر︙.المزعجهم
شرح︙ يضهر اليك جميع الذين مفعل عليهم الازعاج 
———✠———
الأمر︙( .الحماية تشغيل )
شرح︙ يقوم بتشغيل رساله الحمايه اي شخص يراسلك سوف يقوم بتنبيه
———✠———
الأمر︙( .الحماية ايقاف )
شرح︙يقوم بتعطيل رساله الحماية الخاص
———✠———
الأمر︙( .قبول )
شرح︙ يقوم بقبول الشخص للأرسال اليك
———✠———
الأمر︙( .رفض )
شرح︙الغاء قبول الشخص من الارسال 
———✠———
الأمر︙( .مرفوض )
شرح︙حظر الشخص 
———✠———
الأمر︙( .المقبولين )
شرح︙عرض قائمة المقبولين ي الحماية 
———✠———
الأمر︙( .جلب الوقتيه + الرد على الصورة )
شرح︙حفض صوره وقتيه في الحافضة 
———✠———
الأمر︙( .تاك بالكلام + الكلمه + معرف الشخص )
شرح︙ يسوي تاك للشخص بالرابط جربه وتعرف 
———✠———
الأمر︙( .نسخ + الرد على رساله )
شرح︙ يرسل الرساله التي رديت عليها
———✠———
الأمر︙.احسب + المعادله
شرح︙يجمع او يطرح او يقسم
———✠———
الأمر  ⦙  ( .كول + الكلمة )
الشرح : يجب اضافه بوتك يتكلم بدلا عنك 
———✠———
الأمر  ⦙ ( .وضع النائم + السبب )
الشرح : اي شخص يعملك تاك او يراسلك او يرد عليك يرد عليه تليثون بكليشة انا حاليا غير موجود ويضع له السبب الي نتة وضعته
———✠———
الأمر  ⦙  .الصور + الرد على الشخص 
الشرح : يجلب لك جميع صور الشخص و يمكن وضع رقم بجانب الأمر
———✠———
الأمر  ⦙  .زاجل + معرف الشخص + الرساله 
الشرح : يرسل الرساله الى الشخص 
———✠———
الأمر ⦙ .فيديو
الشرح  : يرسل فيديو عشوائي
———✠———
الأمر  ⦙ .فيديو2
الشرح :  يرسل فيديو عشوائي
———✠———
الأمر ⦙ .فايروس
الشرح :  يرسل فايروس
———✠———
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة ."""
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await essa .edit(text, buttons=buttons)


@essa .tgbot.on(CallbackQuery(data=re.compile(rb"ord1hs")))
@check_owner
async def inlineessa (ESSA ):
    text = "**✠  ⦑   اوامر الحساب   ⦒  :**"
    buttons = [[Button.inline("اوامر الحساب  1", data="hsb1"),],[Button.inline("رجوع", data="orders"),]]
    await essa .edit(text, buttons=buttons)
    
@essa .tgbot.on(CallbackQuery(data=re.compile(rb"play1")))
@check_owner
async def inlineessa (ESSA ):
    text = """**  ⦑   اوامر الالعاب 1   ⦒  :**
———————✠———————
الامر ( .اسم متقطع + الاسم )
ايقاف ( .ايقاف اسم متقطع )
❕يضع الاسم في حسابك ويقطع فية شبية للاسم وقتي 
———————✠——————
الامر ( .تصحيح + الجملة  + الرد على جملة )
❕- قم بارسال جملة عشوائية من ثم قم بالرد بالامر و بجانبة الكلمة التي تريد ان تضعها بدلا منة سوف يصحح الجملة ولاكن بشكل مقطع
———————✠——————
الامر ( .تكرار متقطع + عدد مرات + عدد ثواني + كلمتين او اكثر )

❕- يكرر الكلمة بنفس الرسالة بشكل متقطع
———————✠——————
شرح  ⦙   نسبة وهميه - الأوامر :
الأمر  ⦙ ( .نسبه الحب + الرد ع الشخص )
الأمر  ⦙ ( . نسبه الانحراف + الرد ع الشخص )
الأمر  ⦙ ( .نسبه الكراهيه + الرد ع الشخص )
الأمر  ⦙ ( .نسبه المثليه +الرد ع الشخص )
الأمر  ⦙ ( . نسبه النجاح + الرد ع الشخص )
الأمر  ⦙ ( .نسبه الانوثه + الرد ع الشخص )
الأمر  ⦙ ( .نسبه الغباء + الرد ع الشخص )
———————✠———————
شرح  ⦙  رفع وهمي - الأوامر  :
الأمر  ⦙ ( .رفع زباله + الرد ع الشخص )
الأمر  ⦙ ( .رفع منشئ + الرد ع الشخص )
الأمر  ⦙ ( .رفع مدير + الرد ع الشخص )
الأمر  ⦙ ( .رفع مطور + الرد ع الشخص )
الأمر  ⦙ ( .رفع مثلي + الرد ع الشخص )
الأمر  ⦙ ( .رفع كواد + الرد ع الشخص )
الأمر  ⦙ ( .رفع مرتبط + الرد ع الشخص )
الأمر  ⦙ ( .رفع مطي + الرد ع الشخص )
الأمر  ⦙ ( .رفع كحبه + الرد ع الشخص )
الأمر  ⦙ ( .رفع زوجتي + الرد ع الشخص )
الأمر  ⦙ ( .رفع صاك + الرد ع الشخص )
الأمر  ⦙ ( .رفع صاكه + الرد ع الشخص )
———————✠———————
الأمر  ⦙ ( .كت )
الشرح ⦙ لعبه اسأله كت تويت عشوائيه 
———————✠———————
الأمر  ⦙ ( .اكس او )
الشرح ⦙  لعبه اكس او دز الامر و اللعب ويا صديقك 
———————✠———————
الأمر  ⦙  ( .همسه + الكلام + معرف الشخص )
الشرح  ⦙  يرسل همسه سريه الى معرف الشخص فقط هو يكدر يشوفها  
———————✠———————
الأمر  ⦙  ( .رسم شعار + الاسم )
الشرح ⦙  يرسم شعار للأسم  
———————✠———————
الأمر  ⦙ ( .نص ثري دي + الكلمه )
الشرح ⦙ يقوم بكتابه الكلمه بشكل ثلاثي الابعاد 
———————✠———————
الأمر  ⦙  ( .كلام متحرك + الكلام )
الشرح ⦙ يقوم بكتابه الكلام حرف حرف  
———————✠———————
الأمر ⦙ ( .ملصق متحرك + الكلام )
الشرح  ⦙ يقوم بكتابه الكلام بملصق متحرك  
———————✠———————
الأمر  ⦙  ( .بورن + معرف الشخص + الكلام + الرد ع اي صوره )
الشرح ⦙  قم بتجربه الامر لتعرفه +18  
———————✠———————
الأمر  ⦙ ( .رسم قلوب + الاسم )
الشرح  ⦙  يكتب الاسم ع شكل قلوب  
———————✠———————

⑴  ⦙  ( .كتابه وهمي + عدد الثواني )
⑵  ⦙  ( .فيديو وهمي + عدد الثواني )
⑶  ⦙  ( .صوره وهمي + عدد الثواني )
⑷  ⦙  ( .جهه اتصال وهمي + عدد الثواني )
⑸  ⦙  ( .موقع وهمي + عدد الثواني )
⑹  ⦙  ( .لعب وهمي + عدد الثواني )

الشرح  ⦙ هذا الامر يقوم بالارسال الوهمي يعني يضهر للناس انو نته جاي تكتب او جاي ترسل صوره او ترسل فيديو او ترسل جهه اتصالك حسب الفتره الي تحددها بالثواني
———————✠———————
⑴  ⦙ ( .شوت + الكلمة )
✠ :  امر تسليه جربه وتعرف  
———————✠———————
⑵  ⦙ ( .كتابه + الكلام بالانكلش )
✠ :   يكتب الكلام على ورقه بخط اليد 100%   
———————✠———————
الشرح  ⦙   العـاب اخـرى فقط قم بنسخ الأمر وارسالـة   :- الأوامر :
1. - ( .لعبه تيك توك اربعه )
2. - ( .لعبه تيك توك اثنان 3 )
3. - ( .لعبه ربط أربعة )
4. - ( .لعبه قرعة )
5. - ( .لعبه حجر-ورقة-مقص )
6. - ( .لعبه روليت )
7. - ( .لعبه داما )
8. - ( .لعبه داما تجمع )
———————✠———————
الأمر  ⦙ ( .هديه + الكلام )
الشرح :  قم بارسال الامر بجانبه اكتب اي شيئ واول شخص سيفتحها سوف يكتب اسمه جربها  
———————✠——————— 
الأمر  ⦙ ( .ضفدع + الكلمه )
الشرح :   يدعم انكليزي فقط + يحول الكلمه لكتابه ضفدع جربه وتفهم   
———————✠——————— 
الأمر  ⦙  ( .لافته + الكلمه )
الشرح :   يدعم انكليزي فقط + يحول الكلمه بلافته ملصق متحرك جربه وتعرف    
———————✠——————— 
الأمر ⦙ ( .تكرار_كلمه  + الجملة )
الشرح : يكرر الك كلام الجملة 
———————✠——————— 
الأمر ⦙  (.صفق + الرد على الكلام )
الشرح : جربه وتعرف مضحك 
———————✠——————— 
الأمر  ⦙ ( .حضر وهمي + الرد على شخص )
الشرح : حظر وهمي جربه وتعرف 
———————✠———————
الأمر ⦙ ( .خط ملصق + الكلمه )
الشرح : يدعم انكليزي فقط + يحول الكتابه لملصق 
———————✠———————
الأمر  ⦙ ( .شعر )
الشرح : يرسل الك شعر ميمز او مضحك 
———————✠———————
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) ."""

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)



@essa .tgbot.on(CallbackQuery(data=re.compile(rb"ord1pl")))
@check_owner
async def inlineessa (ESSA ):
    text = "**✠  ⦑   اوامر الالعاب   ⦒  :**"
    buttons = [[Button.inline("اوامر الالعاب  1", data="play1"),],[Button.inline("رجوع", data="orders"),]]
    await essa .edit(text, buttons=buttons)


@essa .tgbot.on(CallbackQuery(data=re.compile(rb"shag1")))
@check_owner
async def inlineessa (ESSA ):
    text = """**⦑  اوامر تحويل الصيغ  ⦒  :**
———————✠——————
الأمر ⦙  .تحويل بصمه + الرد ع الصوت mp3
الشرح : يحول صوت mp3 الى بصمه 
———————✠——————
الأمر ⦙  .تحويل صوت + الرد ع الصوت 
الشرح  :  يحول البصمه الى صوت   mp3
———————✠——————
الأمر  ⦙  .تحويل ملصق + الرد ع الصوره 
الشرح :  يحول الصوره الى ملصق 
———————✠——————
الأمر  ⦙ . تحويل صوره + الرد ع الملصق 
الشرح :  يحول الملصق الى صوره 
———————✠——————
الأمر ⦙  .تحويل متحركه + الرد ع الفيديو 
الشرح :  يقوم بتحويل الفيديو الى متحركه 
———————✠——————
الأمر  ⦙  .بي دي اف + الرد ع الملف او الصوره
الشرح :  يحول الملف الى بي دي اف 
———————✠—————— 
الأمر  ⦙ .ملصقي + الرد ع الرساله 
الشرح  : يحول رساله الى ملصق 
———————✠——————
الأمر  ⦙  . تليجراف ميديا + الرد ع الفيديو او صوره
الشرح :  يقوم بتحويل الفيديو او الصوره الى رابط تليجراف  
———————✠——————
الأمر ⦙  ( .تحويل رساله + الرد ع الملف )
الشرح :  يقوم بجلب جميع الكتابه الذي داخل الملف ويقوم بأرسالها اليك 
———————✠——————
الأمر ⦙ ( .تحويل فديو دائري + الرد ع الفيديو )
الشرح : يحول الفيديو الى فيديو دائري مرئي 
———————✠——————
الأمر  ⦙ ( .تحويل ملصق دائري + الرد ع الملصق )
الشرح :  يحول الملصق الى ملصق دائري
———————✠——————
 الأمر ⦙  ( .ترجمه en + الرد ع الرساله )
الشرح :  يقوم بترجمه الرساله الى اللغه الانكليزيه
———————✠——————
الشرح ⦙ ( .ترجمه ar + الرد ع الشخص )
الأمر  :  يقوم بترجمه الرساله الى اللغه العربيه 
———————✠——————
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) ."""

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)
@ESSA .tgbot.on(CallbackQuery(data=re.compile(rb"shag2")))
@check_owner
async def inlineessa (ESSA ):
    text = "**✠  ⦑  2 اوامر تحويل الصيغ   ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑿ ⦙  `.ترجمه en + الرد ع الرساله` \n**✠ :  يقوم بترجمه الرساله الى اللغه الانكليزيه**\n⒀ ⦙ `.ترجمه ar + الرد ع الشخص` \n**✠ :  يقوم بترجمه الرساله الى اللغه العربيه ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n"
    buttons = [[Button.inline("اوامر تحويل الصيغ  1", data="shag1"),],[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)


@ESSA .tgbot.on(CallbackQuery(data=re.compile(rb"ordsag1")))
@check_owner
async def inlineessa (ESSA ):
    text = "**✠  ⦑   اوامر الصيغ   ⦒  :**"
    buttons = [[Button.inline("اوامر الصيغ  1", data="shag1"),],[Button.inline("اوامر الصيغ 2", data="shag2"),],[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)            
       
@ESSA .tgbot.on(CallbackQuery(data=re.compile(rb"ordahln1")))
@check_owner
async def inlineessa (ESSA ):
    text = """** ⦑  اوامر السوبرات  ⦒  :**
———————✠———————
الامر ( .نشر - عدد الثواني - عدد مرات - الكلام ) 
لايقاف ( .اغلاق النشر ) 

❕- امر نشر تلقائي ولاكن بتحديث افضل وتصميم افضل و اسرع 
- الشارحة ضرورية تكون بين الكلام
———————✠———————
 الأمر  ⦙ .مؤقته + الوقت بالثواني + رساله
الشرح :  يرسل الرساله لمده معينه ويحذفها بس يخلص المده
———————✠———————
 الأمر  ⦙ .للكروب + الرد على الرساله
الشرح :  يرسل الرسالها الى جميع المجموعات
———————✠———————
 الأمر  ⦙ ( .مؤقت + عدد ثواني + عدد الرسائل + كليشة )
الشرح :  يقوم بارسال نشر تلقائي للسوبرات 
———————✠———————
الأمر  ⦙  ( .ستوب )
الشرح  ⦙  ايقاف النشر التلقائي المؤقت
———————✠———————
 الأمر  ⦙ .اضافه + رابط الكروب
الشرح :   يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك 
 ———————✠———————
يوجد شرح بتفصيل هنا : https://t.me/L3LL3/4483
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة ."""

    buttons = [[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineessa (ESSA ):
        builder = ESSA .builder
        result = None
        query = ESSA .text
        await bot.get_me()
        if query.startswith("اوامر الاعلانات(?: |$)(.*)") and senzir .query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الاعلانات", data="ordahln1"),]]
            result = builder.article(title="senzir ", text=help2, buttons=buttons, link_preview=False)
            await ESSA .answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الاعلانات(?: |$)(.*)"))
async def repoessa (ESSA ):
    if essa .fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if senzir .reply_to_msg_id:
        await ESSA .get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الاعلانات(?: |$)(.*)")
    await response[0].click(ESSA .chat_id)
    await ESSA .delete()

@ESSA .tgbot.on(CallbackQuery(data=re.compile(rb"ordSONG")))
@check_owner
async def inlinessa (ESSA ):
    text = """** ⦑   اوامر  الاغاني. ⦒  : **
———————✠———————
الأمر  ⦙ .بحث صوت + اسم الاغنيه
الشرح : سيحمل لك الاغنية صوت ايضا يمكنك وضع رابط الاغنيه بدل الاسم 
———————✠——————— 
 الأمر  ⦙ .بحث فيديو + اسم الاغنيه 
الشرح : سيحمل لك الاغنية  فيديو ايضا يمكنك وضع رابط الاغنيه بدل الاسم 
———————✠——————— 
 الأمر  ⦙ .معلومات الاغنيه 
الشرح : الرد ع الاغنيه سيجلب لك معلوماتها واسم الفنان 
———————✠———————
الأمر  ⦙ .كوكل بحث + موضوع البحث
الشرح : يجلب لك معلومات الموضوع من كوكل 
———————✠———————
الأمر  ⦙ .تخزين الصوت + الرد ع البصمه
الشرح  : تخزين الصوت من اجل استخدامه لوضع صوت في الفيديو 
———————✠———————
الأمر  ⦙ .اضف الصوت + الرد ع الصوره او متحركه او فيديو
الشرح  : يتم اضافه الصوت الى الفيديو او المتحركه او الصوره 
———————✠——————— 
الأمر  ⦙ .اسم الاغنيه + الرد ع الاغنيه
الشرح  : ييجلب لك اسم الاغنيه مدة البصمه 10 الى 5 ثواني 
———————✠———————
الأمر  ⦙ ( .تيك توك + الرد ع رابط الفيديو )
الشرح : يحمل فيديو تيك توك بدون العلامه المائيه 
———————✠———————
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة ."""
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)
    
    

@ESSA .tgbot.on(CallbackQuery(data=re.compile(rb"ord1G")))
@check_owner
async def inlineessa (ESSA ):
    text = "**✠  ⦑   اوامر الكروب   ⦒  :**"
    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)

@ESSA .tgbot.on(CallbackQuery(data=re.compile(rb"G1")))
@check_owner
async def inlineessa (ESSA ):
    text = """**  ⦑  اوامر الكروب 1  ⦒  :**
———————✠———————     
الامر ( .نشر - عدد الثواني - عدد مرات - الكلام ) 
لايقاف ( .اغلاق النشر ) 

❕- امر نشر تلقائي ولاكن بتحديث افضل وتصميم افضل و اسرع 
- الشارحة ضرورية تكون بين الكلام
———————✠——————— 
 الأمر  ⦙  ( .كتم + الرد ع الشخص )
الشرح  ⦙ يكتم الشخص من الخاص او الكروبات فقط اذا كانت عندك صلاحيه حذف رسائل 
الأمر  ⦙  ( . الغاء كتم + الرد ع الشخص )
الشرح  ⦙ يجلب لك جميع معرفات المشرفين في الكروب  
 ———————✠——————— 
الأمر ⦙  ( .البوتات )
الشرح  ⦙ يجلب لك جميع معرفات البوتات في الكروب 
الأمر ⦙  ( .الأعضاء )
الشرح  ⦙ اضهار قائمة الاعضاء للكروب اذا هواي سيرسل ملف كامل لمعلوماتهم  
———————✠——————— 
الأمر ⦙  ( .معلومات )
الشرح  ⦙ سيرسل لك جميع معلومات الكروب بالتفصيل  
الأمر ⦙  ( .مسح المحظورين )
الشرح  ⦙ يمسح جميع المحظورين في الكروب 
 ———————✠——————— 
الأمر ⦙  ( .المحذوفين )
الشرح  ⦙ يجلب لك جميع الحسابات المحذوفه 
الأمر ⦙  ( .المحذوفين تنظيف )
الشرح  ⦙ يمسح جميع الحسابات المحذوفه في الكروب 
———————✠——————— 
الأمر ⦙  ( .احصائيات الاعضاء )
الشرح  ⦙ يمسح جميع المحظورين في الكروب 
———————✠——————— 
الأمر ⦙  ( .انتحال + الرد ع الشخص )
الشرح  ⦙ يقوم بأنتحال الشخص ويضع صورته ونبذته واسمه في حسابك عدا المعرف  
الأمر ⦙  ( .الغاء الانتحال + الرد ع الشخص )
الشرح  ⦙ يقوم بألغاء الانتحال وسيرجع معلومات المذكوره بالسورس 
———————✠———————
الأمر  ⦙  ( .ترحيب + الرساله )
الشرح  ⦙ يضيف ترحيب في الكروب اي شخص ينضم راح يرحب بي  
الأمر  ⦙   ( .مسح الترحيبات )
الشرح  ⦙ ييقوم بمسح الترحيب من الكروب 
———————✠——————— 
الأمر  ⦙  ( .ترحيباتي )
الشرح  ⦙ يضهر لك جميع الترحيبات التي وضعتها في الكروب 
———————✠——————— 
الأمر  ⦙  ( .رساله الترحيب السابقه تشغيل ) 
الشرح  ⦙ عندما يحدث تكرار سيحذف رساله الترحيب 
الأمر  ⦙  ( .رساله الترحيب السابقه ايقاف )
الشرح  ⦙ عندما يحدث تكرار لا يحذف رساله الترحيب 
———————✠——————— 
الأمر ⦙  ( .اضف رد + الكلمه )
الشرح  ⦙ مثلاً تدز رساله هلو تسوي عليها رد بهلوات 
الأمر ⦙  ( .مسح رد + الكلمه )
الشرح  ⦙ سيحذف الكلمه الي انت ضفتها 
الأمر ⦙  ( .جميع الردود )
 الشرح  ⦙ يجلب لك جميع الردود الذي قمت بأضافتها  
الأمر ⦙  ( .مسح جميع الردود )
الشرح  ⦙ يمسح جميع الردود الي انت ضفتها 
———————✠——————— 
الأمر ⦙  ( .صنع مجموعه + اسم المجموعه )
الشرح  ⦙ يقوم بعمل مجموعه خارقه 
الأمر ⦙  ( .صنع قناه +  اسم القناة )
الشرح  ⦙ يقوم بعمل قناه خاصه  
———————✠——————— 
الأمر ⦙  ( .عدد رسائلي )
الشرح  ⦙ سيظهر لك عدد رسائلك في الكروب 
———————✠———————
الأمر  ⦙  ( .تفعيل حمايه المجموعه )
الشرح  ⦙ يقوم غلق جميع صلاحيات المجموعه يبقي فقط ارسال  الرسائل
الأمر  ⦙ تعطيل حمايه المجموعه
الشرح  ⦙ يقوم بتشغيل جميع صلاحيات المجموعة ماعدا تغير المعلومات و التثبيت و اضافه اعضاء تبقى مسدوده
———————✠——————— 
الأمر  ⦙  ( .صلاحيات المجموعه )
الشرح  ⦙ يقوم بعرض صلاحيات المجموعه المغلقه والمفتوحه
———————✠———————
الأمر  ⦙  ( .رفع مشرف + الرد على شخص )
الشرح  ⦙ يرفع الشخص مشرف يعطي صلاحيه حذف رسائل والتثبيت فقط
———————✠——————— 
الأمر  ⦙  ( .منع + كلمة )
الشرح  ⦙ منع كلمه من الارسال في الكروب
الأمر ⦙  ( .الغاء منع + كلمه )
الشرح  ⦙ يقوم بالغاء منع الكلمه  
———————✠——————— 
الأمر ⦙  ( .قائمه المنع )
الشرح  ⦙ يقوم بجلب جميع الكلمات الممنوعه في الكروب 
———————✠——————— 
الأمر ⦙  ( .تاك + ( الاعداد المحدده وثابتة فقط) ⤵️
  ( 10 - 50 - 100 - 200  )
الشرح  ⦙ يجلب لك الاعضاء بالروابط بالعدد المحدد 
———————✠——————— 
الأمر ⦙  ( .معرفات + ( الاعداد المحدده وثابتة فقط) ⤵️
  ( 10 - 50 - 100 - 200  )
الشرح  ⦙ جلب لك معرفات الاعضاء بالعدد المحدد 
———————✠———————
الأمر  ⦙  ( .تنظيف الوسائط )
 الشرح  ⦙ ينضف جميع ميديا من صور وفديوهات و متحركات او ( .تنظيف الوسائط + العدد)  
———————✠——————— 
الأمر  ⦙  ( .حذف الرسائل )
الشرح  ⦙ يحذف جميع الرسائل بلكروب  
  او  .حذف الرسائل + العدد 
———————✠——————— 
الأمر  ⦙  ( .مسح + الرد على رسالة )
الشرح  ⦙ يحذف الرساله الي راد عليها فقط 
———————✠——————— 
الأمر  ⦙  ( .غادر )
الشرح  ⦙ يغادر من المجموعه او من القناة
———————✠——————— 
الأمر  ⦙  ( .تفليش )
الشرح  ⦙ يطرد جميع الي في الكروب او قناة 
———————✠——————— 
الأمر ⦙  ( .اضافه + رابط الكروب )
الشرح  ⦙ يضف اليك جميع الاعضاء الى الكروب 
 ( يجب ان تتاكد انك  لست محضور ارسل ⬅️
( .فحص الحظر ) من اجل التاكد
———————✠——————— 
الأمر ⦙  ( .جلب الوقتيه + الرد على الصورة )
الشرح  ⦙ الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية
———————✠——————— 
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) .
جميع الاوامر تكون بدايتها نقطة ."""
    buttons = [[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)

@ESSA .tgbot.on(CallbackQuery(data=re.compile(rb"G2")))
@check_owner
async def inlineessa (ESSA ):
    text = """**  ⦑  اوامر الكروب 2  ⦒  : **
———————✠——————— 
الأمر ⦙  ( .تاك بالكلام + الكلمه + معرف الشخص )
الشرح  ⦙ يعمل تاك للشخص بالرابط جربه وتعرف
———————✠——————— 
الأمر ⦙  ( .نسخ + الرد على رساله )
الشرح  ⦙ يرسل الرساله التي رديت عليها 
———————✠——————— 
الأمر ⦙  ( .ابلاغ الادمنيه )
الشرح  ⦙ يعمل تاك لجميع الادمنيه  
———————✠——————— 
الأمر ⦙  ( .المشرفين )
الشرح  ⦙ يجلب اليك جميع المشرفين 
الأمر ⦙  ( .البوتات )
الشرح  ⦙ يجلب الك جميع بوتات في المجموعه او قناه
———————✠———————
الأمر ⦙  ( .حظر + الرد على شخص )
الشرح  ⦙ حظر الشخص من المجموعه 
الأمر  ⦙  ( .الغاء الحظر + الرد على شخص )
الشرح  ⦙ يلغي حظر الشخص من المجموعه
———————✠——————— 
الأمر  ⦙  ( .بدء مكالمه )
الشرح  ⦙ يقوم بتشغيل مكالمه 
الأمر ⦙  ( .دعوه للمكالمه )
الشرح  ⦙ يتم دعوه الاعضاء للمكالمة الشغاله
———————✠——————— 
الأمر ⦙  ( .تنزيل مشرف + الرد على شخص )
الشرح  ⦙ يقوم بازاله الشخص من الاشراف 
———————✠——————— 
الأمر  ⦙  ( .تثبيت + الرد على رساله )
 شرح : تثبيت الرساله التي رديت عليها
———————✠——————— 
الأمر ⦙  ( .الأعضاء )
الشرح  ⦙ اضهار قائمة الاعضاء للمجموعة 
———————✠——————— 
الأمر ⦙  ( .تفليش )
الشرح  ⦙  أزاله جميع اعضاء المجموعه
 ———————✠——————— 
الأمر ⦙  ( .مسح المحظورين )
الشرح  ⦙ يمسح جميع المحظورين 
———————✠——————— 
الأمر  ⦙  ( .المحذوفين )
الشرح  ⦙  يجلب لك الحسابات المحذوفه 
الأمر ⦙  ( .المحذوفين تنظيف )
الشرح  ⦙ مسح الحسابات المحذوفه
———————✠——————— 
الأمر ⦙  ( .احصائيات الاعضاء )
الشرح  ⦙ يجلب جميع معلومات اعضاء المجموعه 
———————✠——————— 
الأمر ⦙  ( .عدد رسائلي )
الشرح  ⦙ يقوم بحساب عدد رسائلك 
———————✠——————— 
الأمر ⦙  ( .جلب الاحداث )
الشرح  ⦙ يجلب اخر 20 رساله محذوفه
———————✠———————
الأمر  ⦙ ( .حظر عام + الرد على شخص ) 
الشرح  ⦙ حظر من جميع الكروبات   
———————✠———————
الأمر  ⦙ ( .الغاء حظر عام + الرد على شخص )
الشرح  ⦙ الغاء حضر العام  
———————✠———————
الأمر  ⦙ ( .المحظورين عام )
الشرح ⦙  يضهر المحضورين عام 
———————✠———————
الشرح  ⦙ ( .تقيد + الرد على شخص )
الأمر  ⦙ يقيد الشخص من المجموعة 
———————✠———————
شرح الأوامر : ( @E_I_I7 ) .
قناه السورس : ( @HG_STF  ) ."""
    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("رجوع", data="orders"),]]
    await ESSA .edit(text, buttons=buttons)


    
@bot.on(admin_cmd(outgoing=True, pattern="(الاوامر|اوامر)"))
async def repoessa (ESSA ):
    if essa .fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    
    if essa .reply_to_msg_id:
        try:
            await essa .get_reply_message()
            response = await bot.inline_query(TG_BOT, "(الاوامر|اوامر)")
            await response[0].click(essa .chat_id)
            await essa .delete()
        except BotInlineDisabledError: 
            await essa .send_message( "يجب تفعيل الاونلاين من بوت فاذر اولا " )

