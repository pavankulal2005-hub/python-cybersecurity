import base64

msg = input(" Enter message : ")

enc = base64.b64encode(msg.encode())
print(" Encoded       :", enc.decode())

dec = base64.b64decode(enc).decode()
print(" Decoded       :", dec)
