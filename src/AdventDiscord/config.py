import os
import sys
import toml
from threading import local
from termcolor import colored
from pathlib import Path

local_config = toml.loads(Path(".env").read_text())

def get_config():
    config = {}

    if 'ADVENT_PRIV_BOARDS' in os.environ:
        config['private_leaderboards'] = os.environ['ADVENT_PRIV_BOARDS'].split(',')
    elif "private_boards" in local_config["aoc"]:
        config['private_leaderboards'] = local_config['aoc']['private_boards']["QAoC"]["leaderboard"]
    else:
        config['private_leaderboards'] = []
        
    if 'ADVENT_DISABLE_TERMCOLOR' in os.environ:
        config['disable_color'] = (os.environ['ADVENT_DISABLE_TERMCOLOR'] == '1')
    else:
        config['disable_color'] = False

    if 'ADVENT_SESSION_COOKIE' in os.environ:
        config['session_cookie'] = os.environ['ADVENT_SESSION_COOKIE']
    elif "token" in local_config["aoc"]:
        config['session_cookie'] = local_config["aoc"]["token"]
    else:
        # this is to avoid importing colored() from utils.py, resulting in a circular import
        error_message = ('Session cookie not set.\nGrab your AoC session cookie from a browser'
                         ' and store it in an environment variable ADVENT_SESSION_COOKIE.')
        if not config['disable_color']:
            error_message = '\n'.join([colored(s, 'red') for s in error_message.split('\n')])
        print(error_message)
        sys.exit(1)

    return config
