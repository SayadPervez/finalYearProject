import os

os.system("ls /dev/tty*")

port = "/dev/tty" + input("\n\nEnter PORT PATH ( /dev/tty* ) : ")
baudrate = int(input("Enter baudrate : "))

try:
    os.remove("./tty.log")
except Exception as e:
    print(e)

os.system(f"""sudo stty -F {port} {baudrate}""")
os.system(f"""sudo stdbuf -o0 cat {port} | ts '[%Y-%m-%d %H:%M:%S]' > ./tty.log""")
