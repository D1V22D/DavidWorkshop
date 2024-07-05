import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server = server.bind(("58:1c:f8:93:17:3b", 4))
server.listen(1)

client, address = server.accept()

try:
    while True:
        message = input("ENTER MESSAGE :")
        client.send(message.encode("utf-8"))
        data = client.recv(1024)
        if not data:
            break
        print(f"Message :{data.decode('utf-8')}")

except OSError as e:
    pass

client.close()
server.close()
