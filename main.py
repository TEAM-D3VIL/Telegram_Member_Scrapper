from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import (PeerFloodError, UserNotMutualContactError ,
                                          UserPrivacyRestrictedError, UserChannelsTooMuchError,
                                          UserBotError, InputUserDeactivatedError)
from telethon.tl.functions.channels import InviteToChannelRequest
import time, os, sys, json
import datetime
now = datetime.datetime.now()
jj=now.strftime("%Y-%m-%d %H:%M:%S")
f = open("Log.txt", "a")
f.write("\n"+jj)
f.close()

with open('pgbmembers.txt', 'w') as fp:
    pass
with open('pgblog.txt', 'w') as fp:
    pass
with open('pgbgroup.session', 'w') as fp:
    pass
with open('pgbgroup.session-journal', 'w') as fp:
    pass
os.remove("tgbmembers.txt")
os.remove("tgblog.txt")
os.remove("tgbgroup.session-journal")
os.remove("tgbgroup.session")
print("JOIN @D3VIL_BOT_SUPPORT FOR MORE INFO AND CONTACT TO OWNER @D3_krish")
print("\n\n© ᴘᴏᴡᴇƦᴅ BY TEAM-D3VIL ")
#print("\nDisclaimers: https://telegra.ph/Disclaimers-for-Members-Adder-10-04")

password = "randompass"

while password!= "TEAM-D3VIL":
  password = input('\nPassword:')
wt = (
    ''' 
     _____     _                                 
              | |                                
          |_ _| |__   __ _ _ __ ___  _   _ _ __  
    ___/ _ | ' \ /  | '__/ _ \| | | | '_ \ 
      | (_| | |_) | (_| | | | (_) | |_| | |_) |
       \__, |_.__/ \__, |_|  \___/ \__,_| .__/ 
        __/ |       __/ |               | |    
       |___/       |___/                |_|
       
      https://telegram.dog/memberaddersoft

 Made By kalpa banuja
    '''
)
COLORS = {
    "re": "\u001b[31;1m",
    "gr": "\u001b[32m",
    "ye": "\u001b[33;1m",
}
re = "\u001b[31;1m"
gr = "\u001b[32m"
ye = "\u001b[33;1m"
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
clearType = input('\nTerminal or Cmd (t/c): ').lower()
if clearType == 't':
    clear = lambda:os.system('clear')
elif clearType == 'c':
    clear = lambda:os.system('cls')
else:
    print('Invalid input!!!')
    sys.exit()
    
if sys.version_info[0] < 3:
    telet = lambda :os.system('pip install -U telethon')
elif sys.version_info[0] >= 3:
    telet = lambda :os.system('pip3 install -U telethon')

telet()
time.sleep(1)
clear()

if os.path.isfile('pgblog.txt'):
    with open('pgblog.txt', 'r') as r:
        data = r.readlines()
    api_id = data[0]
    api_hash = data[1]

else:
    api_id = input('Enter Api Id: ')
    api_hash = input('Enter Api Hash: ')
    with open('pgblog.txt', 'w') as a:
        a.write(api_id + '\n' + api_hash)

client = TelegramClient('pgbgroup', api_id, api_hash)

async def main():
    async def getmem():
        clear()
        print(colorText(wt))
        print('')
        print('')
        
        print(ye+'[+] Choose your channel to Add members.')
        a=0
        for i in channel:
            print(gr+'['+str(a)+']', i.title)
            a += 1
        opt1 = int(input(ye+'Enter a number: '))
        my_participants = await client.get_participants(channel[opt1])
        target_group_entity = InputPeerChannel(channel[opt1].id, channel[opt1].access_hash)
        my_participants_id = []
        for my_participant in my_participants:
            my_participants_id.append(my_participant.id)
        with open('pgbmembers.txt', 'r') as r:
            users = json.load(r)
        count = 1
        i = 0
        for user in users:
            if count%50 == 0:
                clear()
                print(colorText(wt))
                print('')
                print('')
                print(ye+"Please wait for 1 minute...")
                time.sleep(20)
            elif count >= 30000:
                await client.disconnect()
                break
            elif i >= 80000:
                await client.disconnect()
                break
            count+=1
            time.sleep(1)
            if user['uid'] in my_participants_id:
                print(gr+'User present. Skipping.')
                continue
            else:
                try:
                    user_to_add = InputPeerUser(user['uid'], user['access_hash'])
                    add = await client(InviteToChannelRequest(target_group_entity,[user_to_add]))
                    print(gr+'Added ', str(user['uid']))
                    
                except PeerFloodError:
                    print(re+"Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                    i += 1
                except UserPrivacyRestrictedError:
                    print(re+"The user's privacy settings do not allow you to do this. Skipping.")
                    i = 0
                except UserBotError:
                    print(re+"Can't add Bot. Skipping.")
                    i = 0
                except InputUserDeactivatedError:
                    print(re+"The specified user was deleted. Skipping.")
                    i = 0
                except UserChannelsTooMuchError:
                    print(re+"User in too much channel. Skipping.")
                except UserNotMutualContactError:
                    print(re+'Mutual No. Skipped.')
                    i = 0
                except Exception as e:
                    print(re+"Error:", e)
                    print("Trying to continue...")
                    i += 1
                    continue
    
    print(colorText(wt))
    chats = []
    channel = []
    result = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=200,
        hash=0
    ))
    chats.extend(result.chats)
    for a in chats:
        try:
            if True:
                channel.append(a)
        except:
            continue

    a = 0
    print('')
    print('')
    print(ye+'Choose a group to scrape.')
    for i in channel:
        print(gr+'['+str(a)+']', i.title)
        a += 1
    op = input(ye+'Enter a number (or press ENTER to skip): ')
    if op == '':
        print(ye+'Ok. skipping...')
        time.sleep(1)
        await getmem()
        sys.exit()
    else: 
        pass
    opt = int(op)
    print('')
    print(ye+'[+] Fetching Members...')
    time.sleep(1)
    target_group = channel[opt]
    all_participants = []
    mem_details = []
    all_participants = await client.get_participants(target_group)
    for user in all_participants:
        try:
            if user.username:
                username = user.username
            else:
                username = ""
            if user.first_name:
                firstname = user.first_name
            else:
                firstname = ""
            if user.last_name:
                lastname = user.last_name
            else:
                lastname = ""

            new_mem = {
                'uid': user.id,
                'username': username,
                'firstname': firstname,
                'lastname': lastname,
                'access_hash': user.access_hash
            }
            mem_details.append(new_mem)
        except ValueError:
            continue
    
    with open('pgbmembers.txt', 'w') as w:
        json.dump(mem_details, w)
    time.sleep(1)
    print(ye+'Please wait.....')
    time.sleep(3)
    done = input(gr+'[+] Members scraped successfully. (Press enter to Add members)')
    await getmem()

    await client.disconnect()

with client:
    client.loop.run_until_complete(main())
