#---------------------------
#   Import Libraries
#---------------------------
import os
import sys
sys.platform = "win32"
import os, threading, json, codecs, traceback, time
import re
import pyautogui
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#   Import your Settings class
from Settings_Module import MySettings
#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "ChatIsSuperior"
Website = "https://github.com/l0b5ter/ChatIsSuperior_StreamlabsCommand"
Description = "Chat can now control your keyboard!"
Creator = "lobster/loster31345"
Version = "1.0.0.0"

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    global CommandFileList
    directory = os.path.join(os.path.dirname(__file__), "Config")
    if not os.path.exists(directory):
        os.makedirs(directory)
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    if data.IsChatMessage() and data.GetParam(0).lower(): 
        try:
            CommandFile = os.path.join(os.path.dirname(__file__), 'Config/' + data.GetParam(0).lower() + '.json')
            CommandFileList = MySettings(CommandFile)
            if Parent.GetPoints(data.User) > int(CommandFileList.value):
                ResponseString = CommandFileList.Response
                ResponseString = ResponseString.replace("$character", data.User)
                ResponseString = ResponseString.replace("$value", CommandFileList.value)
                SendResp(data, ResponseString)
                Parent.RemovePoints(data.User, data.UserName, int(CommandFileList.value))
                KeyArray = CommandFileList.keys.split(' ')
                for i in KeyArray:
                    if str(len(i)) > "1":
                        HoldKey = i.split('.:.')
                        for x in HoldKey:
                            pyautogui.keyDown(x)
                        for y in HoldKey:
                            pyautogui.keyUp(y)
                    else:
                        pyautogui.press(i) 
            else:
                SendResp(data, "You to poor mate, it cost " + CommandFileList.value)
        except:
            return
    return


#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return


#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------
def ReloadSettings(jsonData):
    return

#---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#---------------------------
def Unload():
    return

#---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
#---------------------------
def ScriptToggled(state):
    return



def SendResp(data, Message):

    if not data.IsFromDiscord() and not data.IsWhisper():
        Parent.SendStreamMessage(Message)

    if not data.IsFromDiscord() and data.IsWhisper():
        Parent.SendStreamWhisper(data.User, Message)

    if data.IsFromDiscord() and not data.IsWhisper():
        Parent.SendDiscordMessage(Message)

    if data.IsFromDiscord() and data.IsWhisper():
        Parent.SendDiscordDM(data.User, Message)
    return
