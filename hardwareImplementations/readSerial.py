import os

os.system("ls /dev/tty*")

port = "/dev/tty" + input("\n\nEnter PORT PATH ( /dev/tty* ) : ")
port = "/dev/ttyACM0" if port=="/dev/tty" else port

baudrate = input("Enter baudrate : ")
baudrate = 115200 if baudrate=="" else int(baudrate)

try:
    os.remove("./tty.log")
except Exception as e:
    print(e)

os.system(f"""sudo stty -F {port} {baudrate}""")
os.system(f"""sudo stdbuf -o0 cat {port} | ts '[%Y-%m-%d %H:%M:%.S]' > ./tty.log""")
