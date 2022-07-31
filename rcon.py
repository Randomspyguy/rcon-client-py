from mctools import RCONClient

from mctools import formattertools

from termcolor import colored

import socket, itertools, threading, sys, colorama, time

colorama.init()

#VARIABLES

HOST = input(colored('Host: \n', 'cyan', attrs=['bold']))                                                                       # Host IP

format = formattertools.DefaultFormatter                                                                                        # Setting Formatter

loading = ["{>      }", "{=>     }", "{==>    }", "{===>   }", "{====>  }", "{=====> }", "{======>}"]                           # Loading Animation Tuple

yellow_arrow = colored(' -->', 'yellow', attrs=['bold'])                                                                        # Stylish Yellow Arrow

while True: #Main Loop
    
    PORT = int(input(colored('Port: \n', 'cyan', attrs=['bold'])))                                                              # Host Port
    
    print('\n')
    
    rcon = RCONClient(HOST, port=PORT)                                                                                          # Setting variable rcon to the open RCON client.

    #DEFINTIONS
    
    def animate():                                                                                                              # Animation for loading.
        
        for c in itertools.cycle(loading):                                                                                      # Take Tuple and cycle thru for 'c'
            
            if done:                                                                                                            # If animation is done, break loop
                break
            c = colored(c, 'white')                                                                                             # Set color of loading animation
            
            sys.stdout.write(colored('\rChecking if port is open... ', 'green') + c)                                            # Writes animation smooth-like.
            
            sys.stdout.flush()
            
            time.sleep(0.5)                                                                                                     # How fast the animation cycles per item in Tuple.
   
    t = threading.Thread(target=animate)
    
    def is_port_open(port: int) -> bool:                                                                                        #Checks PORT on HOST and returns a boolean
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                                                            # Get socket connection
            
            return s.connect_ex((HOST, PORT)) == 0                                                                              # Get Response as boolean
 
    #Loading Animation for Port Check
   
    done = False                                                                                                                # Allow Animation to not break()
    
    t.start()                                                                                                                   # Start Animation

    #CHECK IF PORT IS OPEN 
    
    is_rcon_open = is_port_open(PORT)                                                                                           # Checks port and returns boolean
    
    done = is_rcon_open                                                                                                         # Sets done equal to boolean of is_port_open
    
    if is_rcon_open:                                                                                                            # If rcon port is open
        
        print(yellow_arrow + colored(' PORT IS OPEN', 'green', attrs=['bold', 'blink']))
        
        print('\n')
        
        PASSWORD = input(colored('Password: \n', attrs=['bold']))                                                               # Enter Password
        
        success = rcon.login(PASSWORD)                                                                                          # Boolean for correct passowrd 
        
        print('\n')
        
        if success:                                                                                                             # Correct Password
            
            print(colored('CONNECTED TO:    ' + HOST, 'green'))

        
        #CLIENT
        
        while success:                                                                                                          # Authenticated
            
            command = input('Enter Command: /')                                                                                 # Minecraft command line. Enter 'help or ?'
            
            response = rcon.command(command)                                                                                    # Send Command
            
            clean_res = format.clean(response)                                                                                     # Recieve and clean response using McTools/FormatterTools
            
            print(clean_res)                                                                                                    # Return response
        
        if not success:
            
            print(colored('ERROR: COULD NOT CONNECT TO:    ' + HOST, 'red', attrs=['bold']))                                    # Error bad host/port
            
            print(colored('Check your password, it may be incorrect.',
                        '\nMake sure RCON is speaking to the PORT.',\
                        '\nWithout an RCON client speaking to an the PORT the session will break.',
                        '\nEx: 25565 is default Minecraft Port, it will break the code.', 'magenta'))
            
    else:
        
        print(colored(yellow_arrow) + colored(' PORT IS NOT OPEN', 'red', attrs=['bold']))                                      # Port not open.
        
        done = True
    
    
        
    


