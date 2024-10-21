# Observe & Report

# GOAL FOR THIS APP
# log into the Advent of Code Discord Channel and it will observe the AoC
# leaderboard and report back to the Discord Channel whenever a new member joins the 
# Leaderboard or completes a new challenge.

# not implemented yet
# Another option will be that it downloads the new puzzels at the moment they are available 
# and packages them in a zip file to share with the discord group.

import json
import os
import advent_cli.commands
import advent_cli.config
import advent_cli.utils
import toml
import discord
import advent_cli
import conversations as cons
from datetime import datetime
from discord.ext import commands
from pathlib import Path
# import aocd

log_file = Path("bot_msgs.json")
if not log_file.exists():
    log_file.write_text("{}")

log = json.loads(log_file.read_text())
year = datetime.now().year
aoc_config = advent_cli.config.get_config()



# def get_my_stats(user):
#     token = cfg["aoc"]["user"]["token"]
    
#     result = advent_cli.commands.stats(user, token)
#     print(result)
#     # advent_cli.commands.stats(year)

# def get_leaderboard_stats(year):
#     return advent_cli.commands.private_leaderboard_stats(year)


class Config(dict):
    def __init__(self, path):
        self._path = Path(path)
        self.load()

    def load(self):
        self.update(toml.loads(self._path.read_text())) # load text, convert from toml to dict

    # def add_key(self, key, value):

    def save(self):
        temp = dict(self.copy())
        self._path.write_text(toml.dumps(temp), encoding="utf-8")



# cfg = toml.loads(Path(".env").read_text())
cfg = Config(".env")

# def get_channel(id):
#     return bot.get_channel(id)

# def channel_can_chat(channel):
#     tests = [ 
#              channel in cfg["discord"]["channels"].values(), 
#              channel in cfg["discord"]["forums"].values() 
#              ]
    
#     return all(tests)
    

##################################################################################################
# STEP 1. Get access to the AoC Discord Channel

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# servers = [{s.name: int(s.id)} for s in bot.guilds]

# cfg["servers"] = servers
# Path(".env").write_text(toml.dumps(cfg))
# cfg.save()

# print(f"{bot.user}'s Servers: {', '.join(map(str, servers))}" )


# conversations = {c: get_channel(id) for c, id in cfg["discord"]["channels"].items()}
# forums = {c: get_channel(id) for c, id in cfg["discord"]["forums"].items()}

# def msg_from_servers(msg):
#     return msg.guild.id in servers


def get_file(year, day):
    location = Path("puzzle files")
    filename = f"{year}-{day}.zip"
    return discord.File(location / filename, filename = filename)

 
@bot.event
async def on_ready():
    im_here = f"Hi @everyone!! I'm **{bot.user.name}** and now I'm connected to your Discord!"

    channel = await bot.fetch_channel(cfg["discord"]["channels"]["news"])

    print(im_here)
    # await channel.send(im_here)
    

@bot.event
async def on_member_join(member):
    welcome_channel = await bot.fetch_channel(cfg["discord"]["channels"]["welcome"])
    member_role = discord.utils.get(member.guild.roles, id=cfg["discord"]["roles"]["member"])

    # give new user the member role
    await member.add_roles(member_role)

    # welcome user to server
    await welcome_channel.send(cons.customize_response(member, "welcome"))

    # inform user of commands
    await member.send(cons.customize_response(member, "!help"))


def bot_spoke(message, bot):
    return message.author.id == bot.user.id
    
    
@bot.event
async def on_message(message):
    """Responding to channel & direct messages"""

    if bot_spoke(message, bot):
        return

    respond_chan = message.channel
    respond_memb = message.author

    # if message.channel.id in cons.valid_channels():

    cmds = {cmd for cmd in cons.conversations if cmd in message.content}
    responses = []

    for cmd in cmds:
        if cmd == "!join":
            responses.append( (respond_memb, cons.customize_response(message.author, cmd)) )

        elif cmd in ["!help", "!countdown", "!me", "!stars"]:
            if message.channel.id in cons.valid_channels():
                responses.append( (respond_chan, cons.customize_response(message.author, cmd)) )
            else:
                responses.append( (respond_memb, cons.customize_response(message.author, cmd)) )
        elif cmd == "welcome":
            pass
        
        elif cmd == "!get":
            # PARSE THE MESSAGE FOR THE YEAR AND DAY
            year, day = re.findall(r'\d+', message.content)
            message.content
            
            file_obj =  get_file(year, day)
            


    for target, talkback in responses:
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.update( {f"{stamp} - {message.author.name}" :  talkback} )
        log_file.write_text(json.dumps(log, indent=2, sort_keys=True), encoding="utf-8")
        
        await target.send(talkback)

    






##################################################################################################
# STEP 2. Get a copy of the leaderboard






##################################################################################################
# STEP 3. Observe the leaderboard for changes


##################################################################################################
# STEP 4. Report back to the Discord Channel When a new member appears on the leaderboard or completes a new challenge, 





# Run the app
if __name__ == "__main__":
    os.system("cls")
    
    bot.run(cfg["discord"]["bot_token"])

