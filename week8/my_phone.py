# Object
# -> a specify instance of a class

# Class
# -> General definition
class Message:
    content: str
    timestamp: str
    is_read: bool
    def check_is_read(self):
        return self.is_read


class iPhone:
    def __init__(self, name, version, phone_number, color, model):
        self.name = name
        self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model
        self.files = []
        self.messages = []
    
    def check_messages(self):
        pass

    def call(self, number):
        pass

    def airdrop(self, filename, recipient):
        print(f'Dropping {filename}')

        pass

    def airreceive(self):
        pass

    def set_name(self, new_name):
        if len(new_name) < 3:
            print("Name must be longer than 3 character")
        self.name = new_name

# Create an instance of iPhone class
ningbo_iphone = iPhone(
    name = " Ningbo's Phone",
    version = "18",
    phone_number = "425-XXX-XXXX",
    color = "blue",
    model = "16 pro"
    )
ningbo_iphone.name = 'lnb'
ningbo_iphone.set_name('nb')
print(ningbo_iphone.name)
ningbo_iphone.airdrop(filename="notes.pdf", recipient="ch")

