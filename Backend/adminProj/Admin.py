from Data_sender import Data_sender
from Mail_sender import Mail_sender
class Admin():
    def __init__(self):
        self.username='adham12345'
        self.password='pass'
    def login(self,name,password):
        if (self.username == name and password==self.password):
            return True
        else :
         return False
    def sendMails(self):
        ms = Mail_sender()
        ms.sendMails()
        pass

    def sendData(self):
        ds = Data_sender()
        ds.sendData()
        pass