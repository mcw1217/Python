from pythonping import ping
from time import sleep

with open("./send_logo.png", "rb") as f:
    while True:
        byte = f.read(1024)
        if byte == b"":  # EOF, NULL
            ping("192.168.219.105", verbose=True, count=1, payload=b"EOF")
            break
        ping("192.168.219.105", verbose=True, count=1, payload=byte)
        sleep(0.5)
