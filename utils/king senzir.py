import importlib
import sys
from pathlib import Path

from essa import CMD_HELP, LOAD_PLUG

from ..Config import Config
from ..core import LOADED_CMDS, PLG_INFO
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..core.session import essa 
from ..helpers.tools import media_type
from ..helpers.utils import _cattools, _catutils, _format, install_pip, reply_id
from .decorators import admin_cmd, sudo_cmd

LOGS = logging.getLogger("———————× IQ")


def load_module(shortname, plugin_path=None):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"essa/plugins/{shortname}.py")
        checkplugins(path)
        name = "essa.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info(f"[تم تحميل : {shortname}]\n")
    else:
        if plugin_path is None:
            path = Path(f"essa/plugins/{shortname}.py")
            name = f"essa.plugins.{shortname}"
        else:
            path = Path((f"essa{plugin_path}/{shortname}.py"))
            name = f"essa{plugin_path}/{shortname}".replace("/", ".")
        checkplugins(path)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = essa 
        mod.LOGS = LOGS
        mod.Config = Config
        mod._format = _format
        mod.tgbot = essa.tgbot
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.reply_id = reply_id
        mod.admin_cmd = admin_cmd
        mod._catutils = _catutils
        mod._cattools = _cattools
        mod.media_type = media_type
        mod.edit_delete = edit_delete
        mod.install_pip = install_pip
        mod.parse_pre = _format.parse_pre
        mod.edit_or_reply = edit_or_reply
        mod.logger = logging.getLogger(shortname)
        mod.borg = essa 
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["essa.plugins." + shortname] = mod
        LOGS.info(f"[تم تحميل : {shortname}] \n ———————× IQ")


def remove_plugin(shortname):
    try:
        cmd = []
        if shortname in PLG_INFO:
            cmd += PLG_INFO[shortname]
        else:
            cmd = [shortname]
        for cmdname in cmd:
            if cmdname in LOADED_CMDS:
                for i in LOADED_CMDS[cmdname]:
                    essa.remove_event_handler(i)
                del LOADED_CMDS[cmdname]
        return True
    except Exception as e:
        LOGS.error(e)
    try:
        for i in LOAD_PLUG[shortname]:
            essa.remove_event_handler(i)
        del LOAD_PLUG[shortname]
    except BaseException:
        pass
    try:
        name = f"essa.plugins.{shortname}"
        for i in reversed(range(len(essa._event_builders))):
            ev, cb = essa._event_builders[i]
            if cb.__module__ == name:
                del essa._event_builders[i]
    except BaseException:
        raise ValueError


def checkplugins(filename):
    with open(filename, "r") as kno:
        filedata = kno.read()
    filedata = filedata.replace("sendmessage", "send_message")
    filedata = filedata.replace("sendfile", "send_file")
    filedata = filedata.replace("editmessage", "edit_message")
    with open(filename, "w") as klanr:
        klanr.write(filedata)
