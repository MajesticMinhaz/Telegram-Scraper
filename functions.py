from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.errors.rpcerrorlist import UserPrivacyRestrictedError
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import InputPeerChannel
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import InviteToChannelRequest
import requests as req  # imported requests as req
import sys
import configparser
import csv
import os
import traceback
import random
import time



# Color Code Section
red = "\033[1;31m"
yellow = "\033[1;33m"
green = "\033[1;32m"
cyan = "\033[1;36m"


# icon theme
icon = f"{yellow}[{cyan}+{yellow}]{cyan}"
second_icon = f"{green}[{red}!{green}]{cyan}"

# banner section
def banner_setup() -> None:
    os.system('clear')
    print(f"""
        {red}╔═╗{cyan}┌─┐┌┬┐┬ ┬┌─┐
        {red}╚═╗{cyan}├┤  │ │ │├─┘
        {red}╚═╝{cyan}└─┘ ┴ └─┘┴
    """)

def banner_scraper():
    source = req.get("https://raw.githubusercontent.com/mdminhaz2003/Telegram-Scraper/master/.version")
    print(f"""

            {red}╔╦╗{cyan}┌─┐┬  ┌─┐{red}╔═╗  ╔═╗{cyan}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
            {red} ║ {cyan}├┤ │  ├┤ {red}║ ╦  ╚═╗{cyan}│  ├┬┘├─┤├─┘├┤ ├┬┘
            {red} ╩ {cyan}└─┘┴─┘└─┘{red}╚═╝  ╚═╝{cyan}└─┘┴└─┴ ┴┴  └─┘┴└─

                        {yellow}version : {source}

    """)


def config_setup() -> None:
    import configparser  # imported configparser
    banner_setup()
    cpass = configparser.RawConfigParser()
    cpass.add_section('cred')
    api_id = input(f"{icon} Enter your App api ID : {red}")
    cpass.set('cred', 'id', api_id)
    hash_id = input(f"{icon} Enter your App api hash : {red}")
    cpass.set('cred', 'hash', hash_id)
    phone_number = input(f"{icon} Enter Your Telegram Phone Number with country code : {red}")
    cpass.set('cred', 'phone', phone_number)
    setup = open('config.data', 'w')
    cpass.write(setup)
    setup.close()
    print(f"{icon} Configuration Setup Completed.")


def install_pip() -> None:
    def csv_lib() -> None:
        banner_setup()
        print(f"{icon} this may take some time ...\n{icon} Please Wait ...")
        os.system("""
            pip3 install cython numpy pandas Telethon==1.24.0 requests==2.26.0 configparser==5.2.0
            python3 -m pip install cython numpy pandas Telethon==1.24.0 requests==2.26.0 configparser==5.2.0
        """)

    banner_setup()
    print(f"{icon} it will take up to 10 minutes to install csv marge.\n{icon} So Please Wait ...")
    input_csv = input(f"{icon} do you want to enable csv merge (y/n): ").lower()
    if input_csv == "y":
        csv_lib()
    else:
        print(f"{icon} You must be Installed Requirements ...")
        print(f"{icon} Run Again for carry on ...")
    print(f"{icon} Requirements Installed !")


def merge_csv() -> None:
    import pandas as pd  # imported pandas as pd
    import sys  # imported sys
    banner_setup()
    file1 = pd.read_csv(sys.argv[2])
    file2 = pd.read_csv(sys.argv[3])
    print(f"{icon} merging {sys.argv[2]} & {sys.argv[3]} ....")
    print(f"{icon} big files can take some time ...")
    merge = file1.merge(file2, on='username')
    merge.to_csv("output.csv", index=False)
    print(f"{icon} saved file as 'output.csv' \n\n")


def update_tool() -> None:
    import requests as req  # imported requests as req
    banner_setup()
    source = req.get("https://raw.githubusercontent.com/mdminhaz2003/Telegram-Scraper/master/.version")
    if source.text == '1.0.1':
        print(f"{icon} {red} Currently latest version using ... cary on...")
    else:
        print(f"{icon} Removing Old files ...")
        os.system('rm *.py')
        time.sleep(2)
        print(f"{icon} Getting Latest files from https://www.github.com/mdminhaz2003/Telegram-Scraper/master/ \n")
        os.system("""
            curl -s -O https://raw.githubusercontent.com/mdminhaz2003/Telegram-Scraper/master/functions.py
            curl -s -O https://raw.githubusercontent.com/mdminhaz2003/Telegram-Scraper/master/main.py
            chmod 777 *.py
        """)
        time.sleep(2)
        print(f"{icon} Update Completed.\n")


class Requirements:
    # Requirements Section

    # Config Setup

    # Merge CSV files

    # Update Version
    pass


def scrap_function():
    # configparser
    cpass = configparser.RawConfigParser()
    cpass.read('config.data')

    try:
        api_id = cpass['cred']['id']
        api_hash = cpass['cred']['hash']
        phone_number = cpass['cred']['phone']
        client = TelegramClient(phone_number, int(api_id), api_hash).start()
    except KeyError:
        os.system('clear')
        banner_scraper()
        print(f"{second_icon} run python3 start.py first !!\n")
        sys.exit(1)

    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        os.system('clear')
        banner_scraper()
        client.sign_in(phone_number, input(f"{icon} Enter your Verification Code : {red}"))

    # Native Variable
    chats = []
    last_date = None
    chunk_size = 5000000
    groups = []

    client.connect()
    os.system('clear')
    banner_scraper()
    result = client(
        GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash=0)
    )
    chats.extend(result.chats)
    for chat in chats:
        try:
            groups.append(chat)
        except Exception as e:
            print(f"{second_icon} Channel Not Found ...", e)
    print(f"{icon} Choose a Channel and pick serial number to Scrape Members : {yellow}")
    index = 0
    for group in groups:
        print(f"{green}[{yellow}{str(index + 1)}{green}]{yellow} - {group.title}")
        index += 1
    print('')
    group_index = int(input(f"{icon} Enter your Channel serial Number : {yellow}")) - 1
    target_group = groups[int(group_index)]
    print(f"""

        {green}Channel ID :--------------: {yellow}{target_group.id}
        {green}Channel Name :------------: {yellow}{target_group.title}
        {green}Channel Username :--------: {yellow}{target_group.username}
        {green}Channel Member's Number :-: {yellow}{target_group.participants_count}
        {green}Channel Broadcast :-------: {yellow}{target_group.broadcast}
        {green}Verified Channel :--------: {yellow}{target_group.verified}
        {green}Scam Channel :------------: {yellow}{target_group.scam}
        {green}Giga Group :--------------: {yellow}{target_group.gigagroup}
        {green}Access hash code :--------: {yellow}{target_group.access_hash}

    """)

    print(f"{icon} Fetching Members ...")
    all_participants = client.iter_participants(target_group, aggressive=True)
    time.sleep(2)
    print(f"{icon} Saving in file ...")
    # for user in all_participants:
    #     print(f"{user.id} -> {user.username}")

    with open("members.csv", "w", encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(['Username', 'User ID', 'Access hash', 'Name', 'Group Name', 'Group ID'])
        for user in all_participants:
            if user.username:
                username = user.username
            else:
                username = ""
            if user.first_name:
                first_name = user.first_name
            else:
                first_name = ""
            if user.last_name:
                last_name = user.last_name
            else:
                last_name = ""
            name = f"{first_name} {last_name}".strip()
            writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
    print(f"{icon} Members Scraped Successfully.")


class Scraper:
    pass


def send_sms():
    try:
        cpass = configparser.RawConfigParser()
        cpass.read('config.data')
        api_id = cpass['cred']['id']
        api_hash = cpass['cred']['hash']
        phone_number = cpass['cred']['phone']
    except KeyError:
        os.system('clear')
        banner_scraper()
        print(f"{second_icon} run python3 start.py first !!!\n")
        sys.exit(1)

    client = TelegramClient(phone_number, int(api_id), api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        os.system('clear')
        banner_scraper()
        client.sign_in(phone_number, input(f"{icon} Enter your Verification Code : {red}"))

    os.system('clear')
    banner_scraper()
    input_file = sys.argv[1]
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {'username': row[0], 'id': int(row[1]), 'access_hash': int(row[2]), 'name': row[3]}
            users.append(user)
    print(f"{green}[1] Send SMS by user ID\n[2] Send SMS by username")
    mode = int(input(f"{green}Input your option number : {red}"))
    message = input(f"{icon} Enter your Message : {yellow}")
    for user in users:
        if mode == 2:
            if user['username'] == "":
                continue
            receiver = client.get_input_entity(user['username'])
        elif mode == 1:
            receiver = InputPeerUser(user['id'], user['access_hash'])
        else:
            print(f"{second_icon} Invalid Mode Selected. Please Select ( 1 or 2 )")
            client.disconnect()
            sys.exit()
        # program sleep time
        SLEEP_TIME = 1

        try:
            print(f"{icon} Sending Message to : {user['name']}")
            client.send_message(receiver, message.format(user['name']))
            print(f"{icon} Waiting {format(SLEEP_TIME)} seconds")
            time.sleep(SLEEP_TIME)
        except PeerFloodError:
            print(
                f"{second_icon} Getting Flood Error from telegram.\n{second_icon} Script is stopping now.\n{second_icon} Please try again after some time.")
            client.disconnect()
            sys.exit()
        except Exception as e:
            print(f"{second_icon} Error", e)
            print(f"{second_icon} Trying to continue ...")
            continue
    client.disconnect()
    print("Done ! Message sent to all users.")

def add_to_group():
    cpass = configparser.RawConfigParser()
    cpass.read('config.data')
    try:
        api_id = cpass['cred']['id']
        api_hash = cpass['cred']['hash']
        phone_number = cpass['cred']['phone']
        client = TelegramClient(phone_number, int(api_id), api_hash)
    except KeyError:
        os.system('clear')
        banner_scraper()
        print(f"{second_icon} run python3 start.py first !!\n")
        sys.exit(1)

    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        os.system('clear')
        banner_scraper()
        client.sign_in(phone_number, input(f"{icon} Enter your verification code here : {red}"))

    os.system('clear')
    banner_scraper()
    input_file = sys.argv[1]
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {'username': row[0], 'id': int(row[1]), 'access_hash': int(row[2]), 'name': row[3]}
            users.append(user)

    chats = []
    last_date = None
    chunk_size = 200
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup:
                groups.append(chat)
        except KeyError:
            continue

    i = 0
    for group in groups:
        print(f"{green}[{cyan}{str(i)}{green}]{cyan} - {group.title}")
        i += 1

    print(f"{icon} Choose a group to add members")
    group_index = input(f"{icon} Enter your Group index : {red}")
    target_group = groups[int(group_index)]
    target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)
    print(f"{green}[1] add member by user ID\n[2] add member by username ")
    mode = int(input(f"{green} Input : {red}"))
    n = 0
    for user in users:
        n += 1
        if n % 50 == 0:
            time.sleep(1)
            try:
                print("Adding {}".format(user['id']))
                if mode == 1:
                    if user['username'] == "":
                        continue
                    user_to_add = client.get_input_entity(user['username'])
                elif mode == 2:
                    user_to_add = InputPeerUser(user['id'], user['access_hash'])
                else:
                    sys.exit(f"{second_icon} Invalid Mode Selected. Please Try Again.")
                client(InviteToChannelRequest(target_group_entity, [user_to_add]))
                print(f"{icon} Wait for 5-10 Seconds ...")
                time.sleep(random.randrange(5, 10))
            except PeerFloodError:
                print(f"{second_icon} Getting Flood Error from telegram.\n{second_icon} Script is stopping now.")
                print(f"{second_icon} Please Try Again After Some Time.")
            except UserPrivacyRestrictedError:
                print(f"{second_icon} The user's privacy settings don't allow you to do this.")
                print(f"{red}Skipping !!!")
            except Exception as e:
                traceback.print_exc()
                print(f"{second_icon} Unexpected Error showing.", e)
                continue


