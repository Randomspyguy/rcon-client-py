# rcon-client-py

An RCON client utilizing mctools. I built this specifically for my Minecraft server.


Hello! Welcome to my attempt at a command line based Python3 RCON client. This open-source tool is simple and provides no security benefit. I made this to use for my docker-contained minecraft server, to access the server-side console.

I am still a novice programmer, any constructive critisim is always appreciated. Any features / upgrade ideas also appreciated.

# Dependancies:
```python
from mctools import RCONClient
from mctools import formattertools
from termcolor import colored
import socket, itertools, threading, sys, colorama, time
```
- mctools does most of the work here, handling the RCON client end.
- mctools/formattertools is a fantastic toolset to modify the response from the command line. Generally the output of an RCON response will be the raw string data for what is presented. Colored text in minecraft requires prefixes to add those colors. This tool translates those prefixes into command line color and beuifies it (using termcolor).

# Features:
- I am a stickler for beauty and usability. I need pretty colors and animation.
- Keeps constant connection without bombarding the server with requests per command.
- This program has a loading animation that was based off of this [thread.](https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running "thread")
The program will check to see if the port is open. 
	- The client does not know if it is an RCON client, just that the port it open. If you enter a port that does not have an RCON client talking, it will let you enter a password, and it will break the program. This will yield no results. Ex: 25565, 80, 53, etc.

- If the port entered is closed then the program will error and ask for the input again.

# To-Do:
- Does not work locally. Searches for a port via INET therefore your server does need to be port-forwarded and HOST ip needs to be public IP address.
- GUI?? For funsies.
- Currently animate() is defined but can only be used for the PORT search. I want to automate this and make it global. Plans include turing this from:
'''python
def animate():
        for c in itertools.cycle(loading):
            if done:
                break
            c = colored(c, 'white')
            sys.stdout.write(colored('\rChecking if port is open... ', 'green') + c)
            sys.stdout.flush()
            time.sleep(0.5)
'''
to:
'''python
def animate(load, load_color, str, str_color, sleep: int):
        for c in itertools.cycle(load):
            if done:
                break
            c = colored(c, load_color)
            sys.stdout.write(colored('\r' + str, str_color) + c)
            sys.stdout.flush()
            time.sleep(sleep)
'''
This allows for almost full customizability with the colors of what is being animated.

