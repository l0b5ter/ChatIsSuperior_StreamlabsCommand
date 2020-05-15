# ChatIsSuperior_StreamlabsCommand
Allow chat to control your keyboard! Commands cost currency..                   
ChatIsSuperior_StreamlabsCommand is a twitch script for the streamlabs chatbot that brings the streamer and the viewer closer^^

Script-version: 1.0.0.2                     
Last-modified: 27.03.2020                     
Made by: lobster/loster31345 from WiAD                           
Requested by: Mofker (twitch.tv/mofkerlive).


## Functions:
1. On commands in twicth chat will return a response/message along with keyboard control!
2. Version 1.0.0.2 can also play a mp3 file.
2. All commands cost bot currency.
3. Simple and clean way to add and removed.

## Instructions on how to get it up
1. download .zip
2. This folder is in a zip-file, so extract it and move the folder ChatIsSuperior
 into the streamlabs chat bot "Scripts" folder.
3. Install pyautogui (open cmd and type "pip install pyautogui").
4. Open the "Config" folder in the script folder, its empty.
5. So Look how the "!hotkey.json" and "!hotkey2" files are formatted in the example forlder and add commands the same way to your "Config" folder.
6. Yay you done mate, just reload the scripts and see the magic^^

Feel free to take a look at the script "ChatIsSuperior_StreamlabsCommand.py", however if you make a change dont come and say its not working. ill galdly help fix or improve it^^


## File formatting
-The file name is the command, must end with json.

-Inside it have to be formatted as json, ({ "text": "test", "something": "someelse"})

-"Response" is what the bot will respond with in chat, ("Response": "the message here")

-"value" is the price in currency they gotta pay for the command, ("value": "number here")

-"keys" is the keys thats being pressed on command, ("keys": "a b c") 

                Space between letters result in same was as typing, a first, then b and lastly c.
                
                .:. between letters result in them being pressed at the same time, like shift.:.c will be C.
                
-"SoundFile" is what file the command should play. Leaving it as ("SoundFile": "") will not play anything, while ("SoundFile": "test.mp3") will play the file test.mp3 which is inside the "ChatIsSuperior" folder.





#### Wanna support my work?                                                    
[![Become a Patron!](https://i.imgur.com/BbE01dL.png)](https://www.patreon.com/bePatron?u=31657981)
