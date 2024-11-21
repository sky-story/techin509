# Practice Time!
# __init__ is the class initializer method that is automatically called when a class is instantiated. 
# It initializes instance attributes or performs other necessary setup, allowing !!parameters to be passed during instance creation.
class Phone:
    def __init__(self, name):
       self.name = name
    def call(self, phone_number):
       print(f'Your {self.name} is calling {phone_number}')

    def airdrop(self):
       print(f'Your {self.name} is sending files via airdrop')

    def okay_google(self):
       pass

class iPhone(Phone):
   pass

class Android(Phone):
   pass

phone = iPhone('lnb_iphone')
phone.call('123-123-123')

phone.airdrop()

phone2 = Android('lnb_android')
phone2.call('123-123-456')
phone2.okay_google()