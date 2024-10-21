

import datetime
from requests import get
import json, toml
from pathlib import Path
import discord

cfg = toml.loads(Path(".env").read_text())
# load the default conversations
conversations = json.loads(Path("conversations.json").read_text())

# def refresh_conversations():
#     conversations = json.loads(Path("conversations.json").read_text())

def is_command(cmd):
    return cmd.lower().strip() in conversations

# def direct_message(member, msg):
#     await member.send(msg)

def get_day(member, year, day):
    # return day's puzzle.
    # location = Path("puzzle files")
    _reps = {
        "{user}": member.mention,
        "{day}": day,
        "{year}": year,
    }
    if Path(f"puzzle files/AoC {year}-{day}.zip").exists():
        _reps["{filename}"] = f"AoC {year}-{day}.zip",
        message = "Sure thing {user},\nhere's a package called: {filename}\nIt contains the input, the prompt and a python template for the day {day} puzzle."
        can = True
        
    elif year == datetime.datetime.now().year and day > datetime.datetime.now().day:
        message = "Sorry {user}, but it won't unlock for another {unlock}."
        delta = datetime.datetime(year=year, month=12, day=day) - datetime.datetime.now()
        _reps["{unlock}"] = f"{delta.days} day{'s and' if delta.days > 1 else ''} {delta.seconds // 3600:02} hour{'s' if delta.seconds // 3600 > 1 else ''}"
        can = False
    else:
        can = False
        message = "Sorry {user}, but I had an unexpected issue trying to get that puzzle."
        

    for k, v in _reps.items():
        message = message.replace(k, str(v))

    return can, message

    
    

def valid_channels():
    channels = []
    channels.extend( cfg["discord"]["channels"].values() )
    channels.extend( cfg["discord"]["forums"].values() )
    return channels

def customize_response(member, msgkey):
    msg = conversations[msgkey]["msg"]
    _reps = {
             "{user}": member.mention,
             "{year}": datetime.datetime.now().year
             }
    
    if msgkey == "!help":
        parts = [f"{key} {'.' * int( 17 - len(key) )} {conversations[key]['desc'].capitalize()}" for key in conversations if key != "welcome"]
        _reps["{menu}"] = "\n".join(parts)
        for key, val in _reps.items():
            msg = msg.replace(key, str(val))
    
    elif msgkey == "!join":
        _reps["{leaderboard}"] = cfg["aoc"]["private_boards"]["QAoC"]["leaderboard"]
        _reps["{board_code}"] = cfg["aoc"]["private_boards"]["QAoC"]["code"]
        for key, val in _reps.items():
            msg = msg.replace(key, str(val))


    return msg
    
    
    
    
    

# def get_leader_board(member, year):



    