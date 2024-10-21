# Amanda (The QAoC Bot)

```
CURRENTLY OFFLINE UNTIL CODE CAN BE OVERHAULED.
HOPEFULLY WILL BE ONLINE IN TIME FOR 1 DEC 2024.
```

Amanda is my bot for the QAoC server ***Quinte & Area Advent of Code*** discord server. We're just a group of interconnected friends and coders within a few hours drive of Belleville, ON Canada. We use a handful of languages each, sometimes picking a different environment for each solution, depending on their strengths and weaknesses. I'm mostly Python, but I've tried my hand at GO-Lang on older puzzles.

I started the server to gather a few people who would share in my epiphanies and aneurysms. I had a handful of tools for managing my own solutions and files, but I thought that I'd like a real-time helper to set up workspaces and keep my status updated on my AoC github's main [README.md - https://github.com/friargregarious/Advent-of-Code](https://github.com/friargregarious/Advent-of-Code). 

That updater still works very nicely, but I kept upgrading/replaceing/changing the code and now I have a mess of my main repo. Also, constantly going back to the leaderboard to see how I was doing was distracting me from getting things done. **ADHD for the Lose!**

Anyway, if there was someone keeping an eye on the leaderboard, making sure that all the group's members were listed there, and updating us whenever there was a change, automagically making a workspace template available the moment it's available, that would be something wouldn't it!?

Also, maybe I could add some extra functionality like a point system and Trophies for our own amusement, that would be cool.

So, up until thismorning, she automatically awarded `member` roles to new server members, printed a help message and shared the leaderboard joining instructions to anyone who asked. But now she's offline while I reorganize the code and seperate it from my regular workspace. This was all necessary if I wanted the bot to be able to scale with more than this server. Also, I have to migrate her to a home dedicated server. Running it on my laptop doesn't make it very usable to the rest of my guild.

## About AoC

<https://adventofcode.com/>

Brought to you by [Eric Wastl](http://was.tl/).

Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as interview prep, company training, university coursework, practice problems, a speed contest, or to challenge each other.

You don't need a computer science background to participate - just a little programming knowledge and some problem solving skills will get you pretty far. Nor do you need a fancy computer; every problem has a solution that completes in at most 15 seconds on ten-year-old hardware.

[2024/support](https://adventofcode.com/2024/support)

We suggest that you support his cause by donating. Even `US$5` is a paltry fee to pay for the hours of hair-raising frustration, agony and epiphany he's providing for free.

## Discord Bots

<https://discord.com/developers/applications>

Bots are easy enough to make, but at least I'm finding them a challenge to make interesting. Luckily, the Discord dev team have made available [discord.py - https://pypi.org/project/discord.py/](https://pypi.org/project/discord.py/) and their excellent [documentation - https://discord.com/developers/docs/intro](https://discord.com/developers/docs/intro). Only occassionaly have I needed to go looking to other sources for how to do things.

```cmd
pip install discord.py
```

discord.py had an issue with built-in `audioop` module when using newer versions of Python (I'm currently using latest 3.13.0) during import, only workaround at this time is installing audioop-lts to substitute the import issue:

```cmd
pip install audioop-lts
```

## Other AoC related Pkgs

I've added some 3rd party AoC related pkgs to my dependancies or, in some cases they had functionality I craved but were incompatible so I savagely pruned the modules to add their functionality to my app. Here is a list of them and giving their authors credit, because it's only right.

- **advent-of-code-data**: `MIT License` <https://pypi.org/project/advent-of-code-data/> works the backbone of my AoC code, it has some really cool functionality for submitting answers and even grabs the example input data which not many other pkgs will touch. My favorite trick is to pickle the puzzle objects for later use, to avoid getting rate-limited from too many downloads all at once. Thanks to *Wim Jeantine-Glenn* <hey@wimglenn.com> for his maintenance of this little baby.

- **advent-cli**: `GNU GPL-3.0 License` <https://pypi.org/project/advent-cli/> had some nice code for grabbing prompts and leaderboard data, but it was command-line only, so i had to rip the functions out and put them into my code. Thanks go to *Christian Ferguson* for his work, and my apologies for ripping it apart.
