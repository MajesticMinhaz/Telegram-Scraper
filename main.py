"""
You can re-run start.py
if you added some wrong value
"""
import os
import sys  # sys imported

import functions


# Color Code Section
red = "\033[1;31m"
yellow = "\033[1;33m"
green = "\033[1;32m"
cyan = "\033[1;36m"


# icon theme
icon = f"{yellow}[{cyan}+{yellow}]{cyan}"
second_icon = f"{green}[{red}!{green}]{cyan}"


# print theme
selected = f"{icon} Selected Module : {red}{sys.argv[1]}"


# Main Function
try:
    if any([sys.argv[1] == 'merge', sys.argv[1] == 'm']):
        print(f"{icon} Selected Module : {red}{sys.argv[1]} {sys.argv[2]} {sys.argv[3]}")
        functions.merge_csv()
    elif any([sys.argv[1] == 'update', sys.argv[1] == 'u']):
        print(selected)
        functions.update_tool()
    elif any([sys.argv[1] == 'install', sys.argv[1] == 'i']):
        functions.install_pip()
        functions.config_setup()
    elif any([sys.argv[1] == 'scraper', sys.argv[1] == 's']):
        functions.scrap_function()
    elif any([sys.argv[1] == 'message', sys.argv[1] == 'sms']):
        file_name = input(f"{icon} Enter your CSV file name without extension (.csv): ")
        sys.argv[1] = f"{file_name}.csv"
        functions.send_sms()
    elif any([sys.argv[1] == 'add', sys.argv[1] == 'a']):
        file_name = input(f"{icon} Enter your CSV file name without extension (.csv): ")
        sys.argv[1] = f"{file_name}.csv"
        functions.add_to_group()
    elif any([sys.argv[1] == 'help', sys.argv[1] == 'h']):
        print("""
        
                $ python3 main.py -m file1.csv file2.csv
            
            ( install / i ) install requirements
            ( scraper / s ) scrape a Channel
            ( message / sms ) to send message
            ( add     / a ) add members to a group
            ( merge   / m ) merge 2 .csv files in one
            ( update  / u ) update tool to latest version
            ( help    / h ) for help  

        """)

    else:
        print(f"\n{icon} Unknown Argument : {sys.argv[1]}")
        print(f"{second_icon} for help use : {green} $ python3 start.py -h \n")
except IndexError:
    print(f"\n{second_icon} No Argument Given : {sys.argv[1]}")
    print(f"{second_icon} for help use : ")
    print(f"{second_icon} https://github.com/mdminhaz2003/Telegram-Scraper#-how-to-install-and-use")
    print(f"{green}$ python3 main.py -h\n")
