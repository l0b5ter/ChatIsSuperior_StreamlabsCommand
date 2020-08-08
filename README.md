# ChatIsSuperior_StreamlabsCommand
Allow chat to control your keyboard, with maybe a sound! Commands cost currency..                   
ChatIsSuperior_StreamlabsCommand is a twitch script for the streamlabs chatbot that brings the streamer and the viewer closer^^

Script-version: 1.0.0.3                     
Last-modified: 08.08.2020                     
Made by: lobster/loster31345 from WiAD                           
Requested by: Mofker (twitch.tv/mofkerlive).


## Functions:
1. On commands in twicth chat will return a response/message along with keyboard control!
2. Plays mp3 files.
3. Can hold down buttons for a custom time.
3. All commands cost bot currency.
4. Simple and clean way to add and removed.

## Instructions on how to get it up
### Newest way
1. Download zip file from this repository.
2. Install pyautogui (open cmd and type "pip install pyautogui").
3. Open streamlabs and click on import script.
4. Then select the downloaded zip file (this will install every version of this script, so remove the folder outdated versions for only the newest).
5. Click on import scripts and open the "Config" folder, its empty.
6. So Look how the "!hotkey.json" and "!hotkey2" files are formatted in the example forlder and add commands the same way to your "Config" folder.
7. This folder is in a zip-file, so click on import in the streamlabs chat bot "Scripts" tab and select the .zip folder.
8. Yay you done mate, just reload the scripts and see the magic^^

### Old way
1. download .zip
2. Install pyautogui (open cmd and type "pip install pyautogui").
3. Open the .zip folder.
4. Open the "Config" folder, its empty.
5. So Look how the "!hotkey.json" and "!hotkey2" files are formatted in the example forlder and add commands the same way to your "Config" folder.
6. This folder is in a zip-file, so click on import in the streamlabs chat bot "Scripts" tab and select the .zip folder.
7. Yay you done mate, just reload the scripts and see the magic^^

Feel free to take a look at the script "ChatIsSuperior_StreamlabsCommand.py", however if you make a change dont come and say its not working. ill galdly help fix or improve it^^


## File formatting
-The file name is the command, must end with json.

-Inside it have to be formatted as json, ({ "text": "test", "something": "someelse"})

-"Response" is what the bot will respond with in chat, ("Response": "the message here")

-"value" is the price in currency they gotta pay for the command, ("value": "number here")

-"keys" is the keys thats being pressed on command, ("keys": "a b c") 

                Space between letters result in same was as typing, a first, then b and lastly c.
                
                .:. between letters result in them being pressed at the same time, like shift.:.c will be C. 
                Using 4sec will make the script wait 4 sec before pressing the next. and 4sec2 will wait 4 sec before releasing the next.
                
-"SoundFile" is what file the command should play. Leaving it as ("SoundFile": "") will not play anything, while ("SoundFile":                           "test.mp3") will play the file test.mp3 which is inside the "ChatIsSuperior" folder.

## Changelog
|Script-version|Changes|
|:-|:-|
|[v1.0.0.3](https://github.com/l0b5ter/ChatIsSuperior_StreamlabsCommand) |Commands can now also hold down buttons for a custom time.|
|[v1.0.0.2](https://github.com/l0b5ter/ChatIsSuperior_StreamlabsCommand/tree/master/Outdated%20versions/ChatIsSuperior-v1.0.0.2) |Commands can now trigger to play mp3 files.|
|[v1.0.0.0](https://github.com/l0b5ter/ChatIsSuperior_StreamlabsCommand/tree/master/Outdated%20versions/ChatIsSuperior-v1.0.0.0) |Allow chat to control your keyboard! Commands cost currency.. |






#### Wanna support my work?                                                    
[![Become a Patron!](https://i.imgur.com/BbE01dL.png)](https://www.patreon.com/bePatron?u=31657981)
