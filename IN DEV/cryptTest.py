from cryptography.fernet import Fernet

listKey = [b'a3uo8T5xtcfRIVbWuMmkIDjAiRnFff8ZoBVOagf16xg=']


msg = 'random text'
print(msg)
msgEncode = msg.encode()

f = Fernet(listKey[0])
encrypt = f.encrypt(msgEncode)
print(encrypt)


f2 = Fernet(listKey[0])
decrypt = f2.decrypt(encrypt)
print(decrypt)


msg_EndToEnd = decrypt.decode()
print(msg_EndToEnd)
