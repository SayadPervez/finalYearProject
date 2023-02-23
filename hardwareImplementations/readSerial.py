port = "/dev/tty" + input("Enter PORT PATH ( /dev/tty* ) : ")
baudrate = int(input("Enter baudrate : "))

import os

os.system(f"""sudo stty -F {port} {baudrate}""")
os.system(f"""sudo stdbuf -o0 cat {port} | ts '[%Y-%m-%d %H:%M:%S]' > /home/zorin/Desktop/tty.log""")
