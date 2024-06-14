
from Admin import Admin
username=input("enter username:")
password=input("enter password:")
ad = Admin()
if ad.login(username,password):
    print("Welcome to Admin Program")
    print("enter 'exit' to exit")
    while True:
     query=input("what do you want to send:")
     if query=='data':
         ad.sendData()
     elif query=='mail':
         ad.sendMails()
     elif query=='exit':
         print("goodbye")
         break
     else :
        print("command not reconginzed")
